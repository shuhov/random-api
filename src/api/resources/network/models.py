from flask_restplus import fields

from src.api import api


model = api.model('Model', {
    'name': fields.String,
    'value': fields.String,
})
