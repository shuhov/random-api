class BaseApiException(Exception):
    def __init__(self, message=None, status_code=None):
        Exception.__init__(self)
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message, status=self.status_code)


class MissingParameters(BaseApiException):
    message = "Not enough parameters"
    status_code = 400


class ResourceDoesNotExist(BaseApiException):
    message = "Resource not found"
    status_code = 404


class InternalError(BaseApiException):
    message = "Internal error"
    status_code = 500


class IncorrectStatus(BaseApiException):
    message = "Incorrect status"
    status_code = 400


class DatabaseError(BaseApiException):
    message = "Database error"
    status_code = 500
