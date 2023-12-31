from app.main import db
from app.main.model.orderstep import OrderStep, OrderStepDTO
from app.main.service import order_service as _os


def get_step_by_order(order_code: str):
    # TODO: check to util service
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
        for step in OrderStep.query.filter_by(order_code=order_code):
            result.append(OrderStepDTO.as_dict(step))
        return result

# TODO: overkill -> delete
def add_new_step(data) -> None:
    new_step = OrderStep(
        step_type=data["step_type"],
        supplier_id=data["supplier_id"],
        order_code=data["order_code"]
    )
    save(new_step)


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
        add_new_step(data)

# TODO: save to util service
def save(data: OrderStep) -> None:
    db.session.add(data)
    db.session.commit()
