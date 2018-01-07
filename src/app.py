from flask import Flask, g, jsonify

from src.common.database import get_connection
import src.common.exceptions as exc


def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.TestConfig')
    return app


def configure_api():
    from src.api import api
    from src.api.resources.network.resource import api as ns_network
    from src.api.resources.network.resource import IPv4Address

    api.add_namespace(ns_network, '/network')
    ns_network.add_resource(IPv4Address, '/ipv4_address')

    return api


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
api = configure_api()
api.init_app(app)


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
    print app.url_map
    app.run(debug=app.config['DEBUG'])

