from .. import db
from app.main.model.order import Order, OrderDTO
from app.main.model.orderline import Orderline
from app.main.model.task import Task, TaskDTO


def get_all_orders():
    return Order.query.all()


def get_orders_by_orderline(orderline_id):
    result = []
    for order in Order.query.filter_by(orderline_id=orderline_id):
        result.append(OrderDTO.as_dict(order))

    return result


def get_by_order_code(order_code):
    target = Order.query.filter_by(order_code=order_code).first()
    if target:
        return add_tasks_to_dto(target)
    else:
        # TODO: response to util service
        response = {
            "status": "failed",
            "message": "No Orders found for the given ID"
        }
        statuscode = 404
        return response, statuscode

# Todo: overkill -> delete
def add_new_order(data) -> None:
    new_order = Order(
        order_code=data["order_code"],
        orderline_id=data["orderline_id"],
        orderline_pos=data["orderline_pos"],
        style_number=data["style_number"],
        brand_id=data["brand_id"],
        contractual_partner_id=data["contractual_partner_id"],
        final_client_id=data["final_client_id"]
    )
    save(new_order)


# TODO: response to util service
def assign_to_orderline(orderline_id, data):
    orderline = Orderline.query.get(orderline_id)

    if not orderline:
        response = {
            "status": "failed",
            "message": "No Orderline found for the given ID"
        }
        statuscode = 404
        return response, statuscode

    if order_code_exists(data["order_code"]):
        response = {
            "status": "failed",
            "message": "An order with this code already exists"
        }
        statuscode = 404
        return response, statuscode

    else:
        data["orderline_id"] = orderline_id
        add_new_order(data)

        response = {
            "status": "success",
            "message": f"new order added to orderline{orderline_id}"
        }
        statuscode = 201
        return response, statuscode


def order_code_exists(order_code) -> bool:
    target = Order.query.filter_by(order_code=order_code).first()
    if target:
        return True
    else:
        return False


def add_tasks_to_dto(target: Order) -> Order:
    current_order = OrderDTO.as_dict(target)
    attached_tasks = Task.query.filter_by(order_code=target.order_code)

    result = []
    for task in attached_tasks:
        task_dict = TaskDTO.as_dict(task)
        result.append(task_dict)
    current_order["tasks"] = result

    return current_order


def order_exists(order_code: str) -> bool:
    target = Order.query.filter_by(order_code=order_code)
    if target:
        return True
    else:
        return False


def save(data: Order) -> None:
    db.session.add(data)
    db.session.commit()
