from .. import db
from app.main.model.order import OrderDTO, Order
from flask_restx import Namespace, fields


class Orderline(db.Model):
    __tablename__ = "orderline"

    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, nullable=False)
    contractual_partner_id = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def as_dict(self):
        return {
            "id": self.id,
            "brand_id": self.brand_id,
            "contractual_partner_id": self.contractual_partner_id,
            "completed": self.completed
        }


class OrderlineDTO:
    api = Namespace("orderline", description="orderline operations")

    def __init__(self, brand_id: int, contractual_partner_id: int, completed: bool, orders=None) -> None:
        if orders is None:
            orders = []

        self.id = id
        self.brand_id = brand_id
        self.contractual_partner_id = contractual_partner_id
        self.completed = completed
        self.orders = orders

    def as_dict(self):
        return {
            "id": self.id,
            "brand_id": self.brand_id,
            "contractual_partner_id": self.contractual_partner_id,
            "completed": self.completed,
            "orders": []
        }

    @staticmethod
    def as_new_orderline():
        dto = OrderlineDTO.api.model("orderline", {
            "brand_id": fields.Integer(required=True),
            "contractual_partner_id": fields.Integer(required=True),
            "completed": fields.Integer(required=True),
        })
        return dto

    @staticmethod
    def as_existing_orderline():
        dto = OrderlineDTO.api.model("orderline", {
            "id": fields.Integer(requried=True),
            "brand_id": fields.Integer(required=True),
            "contractual_partner_id": fields.Integer(required=True),
            "completed": fields.Boolean(required=True, default=False),
            "orders": fields.List(fields.Nested(OrderDTO.as_dto()))
        })
        return dto
