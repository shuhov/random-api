import logging
import sys
from collections import defaultdict

from flask import Flask, g, jsonify
from werkzeug.contrib.cache import MemcachedCache

import project.src.common.exceptions as exc
from project.src.common.database import get_connection


# Add configure logging, hook, cli
def create_app():
    app = Flask(__name__)
    app.config.from_object('project.src.config.BaseConfig')

    configure_api(app)

    return app


def configure_api(app):

    from project.src.api import api, api_bp
    from project.src.api.resources.network import IPv4Address

    api.prefix = '/api/v1/random'
    api.add_resource(IPv4Address, '/network/ipv4_address', endpoint='ipv4_address', methods=['GET'])
    app.register_blueprint(api_bp)


def configure_logging(app):
    app.logger.setLevel(logging.INFO)

    sh = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter(
        fmt='[%(asctime)s] - %(name)s:%(lineno)s - [%(levelname)s] - : %(message)s',
        datefmt='%d.%m.%y %H:%M:%S'
    )
    sh.setFormatter(formatter)
    sh.setLevel(logging.DEBUG)
    app.logger.addHandler(sh)


def configure_hook(app):

    @app.teardown_appcontext
    def close_db(error):
        if hasattr(g, 'pg_conn'):
            g.pg_conn.close()


def configure_cli(app):

    @app.cli.command('initdb')
    def init_db():
        conn = get_connection()
        with app.open_resource('init_db.sql', mode='r') as f:
            conn.execute(f.read(), commit=True)
        print('Database has been initialized')


def configure_cache(app):
    sql = """select status_id, available_status_id from status_scheme"""
    with app.app_context():
        rs = get_connection().execute(sql)
    status_scheme = defaultdict(list)
    for status in rs:
        status_scheme[status['status_id']].append(status['available_status_id'])

    cache = MemcachedCache([app.config['MEMCACHED_SOCKET']])
    cache.set('status_scheme', status_scheme)
    return cache


app = create_app()


@app.errorhandler(exc.MissingParameters)
@app.errorhandler(exc.ResourceDoesNotExist)
@app.errorhandler(exc.InternalError)
@app.errorhandler(exc.IncorrectStatus)
@app.errorhandler(exc.DatabaseError)
def error_handler(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])

