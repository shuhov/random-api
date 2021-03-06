from flask import current_app, g
from random_api.common.pg_connector import Connector


def connect_db():
    return Connector(
        current_app.config["DB_URI"], schema=current_app.config["DB_SCHEMA"]
    )


def get_connection():
    if not hasattr(g, "pg_conn"):
        g.pg_conn = connect_db()
    return g.pg_conn
