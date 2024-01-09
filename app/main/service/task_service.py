from .. import db
from ..model.task import Task
from ..model.order import Order
from ..util.enum import TaskType, TaskStatus


def get_tasks_by_order_code(order_code: str):
    return Task.query.filter_by(order_code=order_code).all()


def assign_to_order(order_code: str, data):
    data["order_code"] = order_code
    current_status = TaskStatus.INCOMPLETE
    current_task = TaskType.READ
    new_task = Task(
        status=current_status,
        evidence_id=data["evidence_id"],
        type=current_task,
        order_code=data["order_code"]
    )
    save(new_task)


def update_task(task_id: int, data):
    if not task_exists(task_id):
        # TODO: response to util service
        response = {
            "status": "failed",
            "message": "No Task found for the given ID"
        }
        statuscode = 404
        return response, statuscode
    else:
        target = Task.query.first(task_id)
        new_status = data["status"]
        target.status = new_status


def task_exists(task_id: int):
    target = Task.query.filter_by(id=task_id)
    if target:
        return True
    else:
        return False


# TODO: save to util service
def save(data: Order) -> None:
    db.session.add(data)
    db.session.commit()
