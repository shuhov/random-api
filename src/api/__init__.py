from flask_restplus import Api
from flask_rbac import RBAC

from src.api.roles import Role, User

api = Api(
    prefix='/random',
    title='Random API',
    version='1.0',
)


class RolesConfig:
    __instance = None

    def __init__(self):
        self.rbac = RBAC()

    def init(self, app):
        self.rbac.init_app(app)
        return self.rbac

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(RolesConfig, cls).__new__(cls)
        return cls.__instance





