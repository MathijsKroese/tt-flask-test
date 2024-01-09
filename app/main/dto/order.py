from flask_restx import Namespace, fields
from ..dto.step import StepDTO
from ..dto.task import TaskDTO


class OrderDTO:
    api = Namespace("order", description="Order related operations")
    request_model = api.model("Order Request Model", {
        "style_number":
            fields.String(required=True,
                          description="Identifier of the style number for this order"),
        "brand_id":
            fields.Integer(required=True,
                           description="ID of the issuer for this order"),
        "final_client_id":
            fields.Integer(required=True,
                           description="The ID of the final client for this order")
    })

    response_model = api.model("Order Response Model", {
        "id":
            fields.Integer(required=True,
                           description="ID of the current order"),
        "order_code":
            fields.String(required=True,
                          description="Public identifier for this order"),
        "style_number":
            fields.String(required=True,
                          description="Public identifier of the style number"),
        "brand_id":
            fields.Integer(required=True,
                           description="ID of the issuing brand"),
        "final_client_id":
            fields.Integer(required=True,
                           description="The ID of the final client for this order"),
        "tasks":
            fields.List(fields.Nested(TaskDTO.model),
                        description="An overview of the tasks assigned to this order",
                        default=[]),
        "steps":
            fields.List(fields.Nested(StepDTO.response_model),
                        description="An overview of the steps involved in this Order",
                        default=[])
    })
