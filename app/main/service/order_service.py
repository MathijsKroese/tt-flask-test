from .. import db
from ..model.order import Order
from ..model.task import Task
from ..dto.order import OrderDTO

def get_all_orders():
    return Order.query.all()

def get_by_order_code(order_code):
    return Order.query.filter_by(order_code=order_code).first()


# Todo: overkill -> delete
def add_new_order(data, order_code) -> None:
    new_order = Order(
        order_code=order_code,
        style_number=data["style_number"],
        # brand_id=data["brand_id"],
        final_client_id=data["final_client_id"]
    )
    save(new_order)


def order_exists(order_code) -> bool:
    target = Order.query.filter_by(order_code=order_code).first()
    if target:
        return True
    else:
        return False


def save(data: Order) -> None:
    db.session.add(data)
    db.session.commit()

