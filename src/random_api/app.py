from flask import Flask, g, jsonify

from random_api.common import exceptions as exc


def create_app():
    app = Flask(__name__)
    return app


def configure_api():
    from random_api.api import api
    from random_api.api.resources.network import ns_network
    from random_api.api.resources.network.resource import IPv4Address
    from random_api.api.resources.images import ns_images
    from random_api.api.resources.images.resource import BaseImage, OTPImage

    api.add_namespace(ns_network, '/network')
    ns_network.add_resource(IPv4Address)

    api.add_namespace(ns_images, '/images')
    ns_images.add_resource(BaseImage)
    ns_images.add_resource(OTPImage)

    return api


def configure_hook(app):

    @app.teardown_appcontext
    def close_db(error):
        if hasattr(g, 'pg_conn'):
            g.pg_conn.close()


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
    print(app.url_map)
    app.run(debug=app.config['DEBUG'])

