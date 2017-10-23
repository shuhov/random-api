from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.BaseConfig')

    configure_api(app)

    return app


def configure_api(app):

    from src.api import api, api_bp
    from src.api.resources.network.ipv4_address import IPv4Address

    api.add_resource(IPv4Address, '/ipv4_address', endpoint='ipv4_address', methods=['GET'])
    app.register_blueprint(api_bp)


app = create_app()


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])

