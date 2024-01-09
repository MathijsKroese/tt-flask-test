from .. import db
from ..model.step import Step
from ..service import order_service as _os


def get_steps_by_order_code(order_code: str):
    return Step.query.filter_by(order_code=order_code).all()


# TODO: overkill -> delete
def add_new_step(data) -> None:
    new_step = Step(
        type=data["type"],
        orderline_pos=data["orderline_pos"],
        supplier_id=data["supplier_id"],
        order_code=data["order_code"]
    )
    save(new_step)


def assign_to_order(order_code, data):
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
        add_new_step(data)


# TODO: save to util service
def save(data: Step) -> None:
    db.session.add(data)
    db.session.commit()
