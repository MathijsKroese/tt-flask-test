from app.main import db
from app.main.model.task import Task, TaskDTO
from app.main.model.order import Order
from app.main.service import order_service as _os


def get_tasks_by_order_code(order_code: str):
    if not _os.order_exists(order_code):
        # TODO: response to util service
        response = {
            "status": "failed",
            "message": "No order found for the given ID"
        }
        statuscode = 404
        return response, statuscode
    else:
        result = []
        for task in Task.query.filter_by(order_code=order_code):
            result.append(TaskDTO.as_dict(task))
        return result


def assign_to_order(order_code: str, data):
    if not _os.order_exists(order_code):
        # TODO: response to util service
        response = {
            "status": "failed",
            "message": "No order found for the given ID"
        }
        statuscode = 404
        return response, statuscode

    else:
        data["order_code"] = order_code
        new_task = Task(
            evidence_id=data["evidence_id"],
            task_type=data["type"],
            order_code=data["order_code"]
        )
        save(new_task)

# TODO: save to util service
def save(data: Order) -> None:
    db.session.add(data)
    db.session.commit()
