from flask_restx import Api
from flask import Blueprint
from .main.controller.order_controller import api as order_ns
from .main.controller.task_controller import api as task_ns
from .main.controller.step_controller import api as step_ns


blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='Tex.Tracer Order Microservice',
    version='1.0',
    description='The backend code for the microservice related to orders',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(order_ns, path="/order")
api.add_namespace(task_ns, path="/task")
api.add_namespace(step_ns, path="/step")
