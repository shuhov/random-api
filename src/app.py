from flask import Flask, g, jsonify, Response
from flask_restplus import Namespace, Resource

# from src.common.database import get_connection
import src.common.exceptions as exc
from src.api import RolesConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.TestConfig')

    # @app.before_request
    # def set_current_user():
    #     user = UserRole(roles=[anonymous])
    #     g.current_user = user

    return app


def configure_api():
    from src.api import api
    from src.api.resources.network.resource import api as ns_network
    from src.api.resources.network.resource import IPv4Address

    configure_rbac(app, api)

    api.add_namespace(ns_network, '/network')
    ns_network.add_resource(IPv4Address, '/ipv4_address')

    return api


def configure_rbac(app, api):

    from src.api.roles import Role, User

    rbac = RolesConfig().init(app)

    anonymous_role = Role('anonymous')
    anonymous_user = User(roles=[anonymous_role])

    rbac.set_role_model(Role)
    rbac.set_user_model(User)
    rbac.set_user_loader(lambda: anonymous_user)

    @app.route('/d')
    @rbac.deny(roles=['anonymous'], methods=['GET'])
    def d():
        return Response('Hello from /d')

    class E(Resource):

        def get(self):
            return Response('Hello from /e')

    e = Namespace('e', description='e')
    api.add_namespace(e, '/e')
    e.add_resource(E, '/e')

    resource = app.view_functions.get('e_e', None)
    role = rbac._role_model.get_by_name('anonymous')
    rbac.acl.deny(role, 'GET', resource)


def configure_hook(app):

    @app.teardown_appcontext
    def close_db(error):
        if hasattr(g, 'pg_conn'):
            g.pg_conn.close()


# def configure_cli(app):
#
#     @app.cli.command('initdb')
#     def init_db():
#         conn = get_connection()
#         with app.open_resource('init_db.sql', mode='r') as f:
#             conn.execute(f.read(), commit=True)
#         print('Database has been initialized')

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

