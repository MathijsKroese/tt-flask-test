import enum
from app.main import db
from flask_restx import Namespace, fields


class OrderStepType(enum.Enum):
    DYEING = "dyeing"
    GINNING = "ginning"
    CONFECTIONING = "confectioning"
    PRINTING = "printing"
    CUTTING = "cutting"
    ACCESSORIES = "accessories"
    IMPORTING = "importing"
    SEWING = "sewing"
    ASSEMBLING = "assembling"
    WAREHOUSING = "warehousing"
    TANNING = "tanning"
    PACKING = "packing"
    FINISHING = "finishing"
    FABRIC_TRADING = "fabric trading"
    TRIMS = "trims"
    DESIGN_DEVELOPMENT = "design & development"
    YARN_TRADING = "yarn trading"
    RECYCLED_MATERIAL = "recycled material"
    MATERIAL_TRADING = "material trading"
    TRANSPORT = "transport"
    EXPORTING = "exporting"
    RETAILING = "retailing"
    MAN_MADE_MATERIAL = "man-made material"
    LABELLING = "labelling"


class OrderStep(db.Model):
    __tablename__ = "orderstep"

    id = db.Column(db.Integer, primary_key=True)
    step_type = db.Column(db.Enum(OrderStepType), nullable=False)
    supplier_id = db.Column(db.Integer, nullable=False)
    order_code = db.Column(db.String(25), nullable=False)


class OrderStepDTO:
    api = Namespace("task", description="Task operations")

    def __init__(self, step_type: OrderStepType, supplier_id: int, order_code: str):
        self.id = id
        self.step_type = step_type
        self.supplier_id = supplier_id
        self.order_code = order_code

    def as_dict(self):
        return{
            "id": self.id,
            "step_type": self.step_type.value,
            "supplier_id": self.supplier_id,
            "order_code": self.order_code
        }

    @staticmethod
    def as_dto():
        dto = OrderStepDTO.api.model("orderstep", {
            "id": fields.Integer(required=True),
            "step_type": fields.String(OrderStepType, required=True),
            "supplier_id": fields.Integer(required=True),
            "order_code": fields.String(required=True)
        })
        return dto
