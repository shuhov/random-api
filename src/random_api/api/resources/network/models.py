from flask_restplus import fields

from random_api.api import api


model = api.model('Model', {
    'name': fields.String,
    'value': fields.String,
})
