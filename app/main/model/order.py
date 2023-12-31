from .. import db
from flask_restx import Namespace, fields
from app.main.model.task import TaskDTO


class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    order_code = db.Column(db.String(15), nullable=False)
    orderline_id = db.Column(db.Integer, nullable=False)
    orderline_pos = db.Column(db.Integer, nullable=False)
    style_number = db.Column(db.Integer, nullable=False)
    brand_id = db.Column(db.Integer, nullable=False)  # Company --> Brand
    contractual_partner_id = db.Column(db.Integer, nullable=False)  # Company --> Contractual Partner
    completed = db.Column(db.Boolean, default=False)
    final_client_id = db.Column(db.Integer, nullable=False)


class OrderDTO:
    api = Namespace("order", description="Order operations")

    def __init__(self, order_code: str, orderline_id: int, orderline_pos: int, style_number: int, brand_id: int,
                 contractual_partner_id: int, completed: bool, final_client_id: int,
                 tasks=None, ordersteps=None) -> None:
        if tasks is None:
            tasks = []
        if ordersteps is None:
            ordersteps = []

        self.id = id
        self.order_code = order_code
        self.orderline_id = orderline_id
        self.orderline_pos = orderline_pos
        self.style_number = style_number
        self.brand_id = brand_id
        self.contractual_partner_id = contractual_partner_id
        self.completed = completed
        self.final_client_id = final_client_id
        self.tasks = tasks
        self.ordersteps = ordersteps

    def as_dict(self):
        return{
            "id": self.id,
            "order_code": self.order_code,
            "orderline_id": self.orderline_id,
            "orderline_pos": self.orderline_pos,
            "style_number": self.style_number,
            "brand_id": self.brand_id,
            "contractual_partner_id": self.contractual_partner_id,
            "completed": self.completed,
            "final_client_id": self.final_client_id,
            "tasks": [],
            "ordersteps": []
        }

    @staticmethod
    def as_dto():
        dto = OrderDTO.api.model("order", {
            "id": fields.Integer(),
            "order_code": fields.String(),
            "orderline_id": fields.Integer(required=True),
            "orderline_pos": fields.Integer(required=True),
            "style_number": fields.Integer(required=True),
            "brand_id": fields.Integer(required=True),
            "contractual_partner_id": fields.Integer(required=True),
            "completed": fields.Boolean(required=True, default=False),
            "final_client_id": fields.Integer(required=True),
            "tasks": fields.List(fields.Nested(TaskDTO.as_dto()), default=[]),
            "ordersteps": fields.List(fields.String, default=[])
        })
        return dto
