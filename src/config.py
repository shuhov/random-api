class BaseConfig(object):
    DEBUG = False
    DB_NAME = 'postgres'
    DB_USER = 'postgres'
    DB_PASS = '111'
    DB_SERVICE = 'localhost'
    DB_PORT = 5432
    DB_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
            DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )
    DB_SCHEMA = 'public'
    MEMCACHED_SOCKET = '127.0.0.1:11211'


class TestConfig(BaseConfig):
    DEBUG = True


class DockerConfig(TestConfig):
    DB_PASS = 'postgres'
    DB_SERVICE = 'postgres'
    DB_PORT = 5434
    DB_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        TestConfig.DB_USER, DB_PASS, DB_SERVICE, DB_PORT, TestConfig.DB_NAME
    )
