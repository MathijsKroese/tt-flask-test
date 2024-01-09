from .. import db
from ..util.enum import StepTypes


class Step(db.Model):
    __tablename__ = "step"

    id = db.Column(db.Integer, primary_key=True)
    order_code = db.Column(db.String(25), nullable=False)
    orderline_pos = db.Column(db.Integer, nullable=False, default=1)
    type = db.Column(db.Enum(StepTypes), nullable=False)
    supplier_id = db.Column(db.Integer, nullable=False)
