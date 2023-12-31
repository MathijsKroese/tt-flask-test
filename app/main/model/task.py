from datetime import datetime

from app.main import db
from flask_restx import Namespace, fields
import enum


class TaskType(enum.Enum):
    UPLOAD = "Upload Evidence"
    REVIEW = "Review Evidence"
    READ = "Read Document"
    SIGN = "Sign Document"
    

class TaskStatus(enum.Enum):
    COMPLETE = "Task Completed"
    INCOMPLETE = "Task Incomplete"
    PAUSE = "Task Paused"


class Task(db.Model):
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)
    date_issued = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.Enum(TaskStatus), default=TaskStatus.INCOMPLETE)
    evidence_id = db.Column(db.Integer, nullable=False)
    task_type = db.Column(db.Enum(TaskType), nullable=False)
    order_code = db.Column(db.String(25), nullable=False)


class TaskDTO:
    api = Namespace("task", description="Task operations")

    def __init__(self, date_issued: datetime, status: TaskType, evidence_id: int, task_type: TaskType,
                 order_code: str) -> None:
        self.id = id
        self.date_issued = date_issued
        self.status = status
        self.evidence_id = evidence_id
        self.task_type = task_type
        self.order_code = order_code

    def as_dict(self):
        return {
            "id": self.id,
            "date_issued": self.date_issued,
            "status": self.status.value,
            "evidence_id": self.evidence_id,
            "task_type": self.task_type.value,
            "order_code": self.order_code
        }

    @staticmethod
    def as_dto():
        dto = TaskDTO.api.model("task", {
            "id": fields.Integer(required=True),
            "date_issued": fields.DateTime(required=True),
            "status": fields.String(TaskStatus, required=True),
            "evidence_id": fields.Integer(required=True),
            "task_type": fields.String(TaskType, required=True),
            "order_code": fields.String(required=True)
        })
        return dto
