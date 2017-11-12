import logging
import sys

from flask import Flask, g, jsonify, redirect
from src.common.database import get_connection

import src.common.exceptions as exc


def create_app():
    app = Flask(__name__, static_folder='../static')
    app.config.from_object('src.config.DockerConfig')

    configure_api(app)

    return app


def configure_api(app):

    from src.api import api, api_bp
    from src.api.resources.network import IPv4Address

    api.add_resource(IPv4Address, '/network/ipv4_address', endpoint='ipv4_address', methods=['GET'])

    @app.route('/docs')
    def docs():
        return redirect('/static/docs.html')

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

