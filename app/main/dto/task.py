from flask_restx import Namespace, fields
from ..util.enum import TaskType, TaskStatus


class TaskDTO:
    api = Namespace("task", description="Task related operations")

    model = api.model("Task DTO", {
        "date_issued":
            fields.DateTime(required=True,
                            desription="The date the task has been issued"),
        "status":
            fields.String(enum=[status.name for status in TaskStatus],
                          required=True,
                          desription="The current status of the Task",
                          default=TaskStatus.INCOMPLETE.name),
        "evidence_id":
            fields.Integer(required=True,
                           desription="The ID of the evidence for this task"),
        "type":
            fields.String(enum=[type.name for type in TaskType],
                          required=True,
                          desription="The type of task"),
        "order_code":
            fields.String(required=True,
                          desription="The order code this task belongs to")
    })

    status_options = api.model("Task status options", {
        "status":
            fields.String(enum=[status.name for status in TaskStatus])
    })

    type_options = api.model("Task type options", {
        "type":
            fields.String(enum=[type.name for type in TaskType])
    })
