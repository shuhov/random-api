import logging

import psycopg2
import psycopg2.extras

logger = logging.getLogger(__file__)


class Connector:
    def __init__(self, db_uri, schema=None):
        self.db_uri = db_uri
        self.schema = schema
        self.connection = psycopg2.connect(self.db_uri)
        logger.debug("Database connection has been established")
        cursor = self.connection.cursor()
        if schema:
            cursor.execute("set schema '{0}'".format(schema))
            logger.debug("Schema {} has been opened successfully".format(schema))

    def execute(self, query, bindings=None, commit=False):
        cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        try:
            cursor.execute(query, bindings)
            if commit:
                self.connection.commit()
            return cursor.fetchall()
        except psycopg2.ProgrammingError as e:
            logger.exception(e)
        except psycopg2.IntegrityError as e:
            logger.exception(
                "Exception while executing query: {0}.\nException: {1}".format(query, e)
            )
        finally:
            cursor.close()

    def close(self):
        self.connection.close()

    def __str__(self):
        return "{0}: {1}; schema={2}".format(
            self.__class__.__name__, self.db_uri, self.schema
        )
