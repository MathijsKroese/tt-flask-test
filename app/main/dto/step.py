from flask_restx import Namespace, fields
from ..util.enum import StepTypes


class StepDTO:
    api = Namespace("step", description="Step related operations")

    request_model = api.model("Step Request Model", {
        "type":
            fields.String(enum=[type.name for type in StepTypes],
                          required=True,
                          description="Description representing the type of step"),
        "orderline_pos":
            fields.Integer(required=True,
                           description="Position of the step in the order line",
                           default=1),
        "supplier_id":
            fields.Integer(required=True,
                           description="The ID of the supplier that has to perform the step"),
    })

    response_model = api.model("Step Response Model", {
        "id":
            fields.Integer(required=True,
                           description = "The ID for this Step"),
        "order_code":
            fields.String(requred=True,
                          description="Identifier for the order this step belongs to"),
        "orderline_pos":
            fields.Integer(required=True,
                           description="Position of the step in the order line",
                           default=1),
        "type":
            fields.String(enum=[type.name for type in StepTypes],
                          required=True,
                          description="Description representing the type of step"),
        "supplier_id":
            fields.Integer(required=True,
                           description="The ID of the supplier that has to perform the step"),
    })

    step_types = api.model("Step Type Options", {
        "type":
            fields.String(enum=[type.name for type in StepTypes])
    })
