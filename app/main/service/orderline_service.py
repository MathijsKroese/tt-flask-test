from app.main import db
from app.main.model.orderline import Orderline, OrderlineDTO
from app.main.model.order import Order
from app.main.service import order_service as _os

def add_new_orderline(data):
    attached_orders = data["orders"]
    new_orderline = Orderline(
        brand_id=data["brand_id"],
        contractual_partner_id=data["contractual_partner_id"],
    )
    save(new_orderline)
    current_orderline_id = new_orderline.id

    for order in attached_orders:
        order["orderline_id"] = current_orderline_id
        _os.add_new_order(order)
    # TODO: response to util service
    response = {
        "status": "success",
        "message": "new orderline created"
    }
    statuscode = 201
    return response, statuscode


def get_all_orderlines():
    result = []

    for orderline in Orderline.query.all():
        result.append((add_orders_to_dto(orderline)))

    return result


def get_orderline_by_id(orderline_id):
    target = Orderline.query.get(orderline_id)
    if target:
        return add_orders_to_dto(target)
    else:
        # TODO: response to util service
        response = {
            "status": "failed",
            "message": "No order line found for the given ID"
        }
        statuscode = 404
        return response, statuscode


def add_orders_to_dto(target: Orderline) -> Orderline:
    current_orderline = OrderlineDTO.as_dict(target)
    attached_orders = Order.query.filter_by(orderline_id=target.id)

    result = []
    for order in attached_orders:
        result.append(order)
    current_orderline["orders"] = result

    return current_orderline


def save(data: Orderline) -> None:
    db.session.add(data)
    db.session.commit()
