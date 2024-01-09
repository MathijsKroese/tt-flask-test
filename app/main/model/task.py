from .. import db
from ..util.enum import TaskType, TaskStatus


class Task(db.Model):
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)
    date_issued = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.Enum(TaskStatus), default=TaskStatus.INCOMPLETE.name)
    evidence_id = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Enum(TaskType), nullable=False)
    order_code = db.Column(db.String(25), nullable=False)
