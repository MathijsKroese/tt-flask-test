from flask_restx import Api
from flask import Blueprint
# TODO: imports to utility service
from app.main.controller.orderline_controller import api as ol_ns
from app.main.controller.order_controller import api as o_ns
from app.main.controller.task_controller import api as t_ns
from app.main.controller.orderstep_controller import api as s_ns
from app.main import create_app

blueprint = Blueprint("api", __name__)

# TODO: Check which is correct
# api = Api(
#     blueprint,
#     title="some title",
#     version="0.1",
#     description="some description",
#     # authorizations=authorizations,
#     # security="apikey"
# )


app = create_app("dev")
api = Api(app)

api.add_namespace(ol_ns, path="/orderline")
api.add_namespace(o_ns, path="/order")
api.add_namespace(t_ns, path="/task")
api.add_namespace(s_ns, path="/step")



