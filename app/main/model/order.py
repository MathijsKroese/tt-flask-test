from .. import db


class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    order_code = db.Column(db.String(15), nullable=False)
    # orderline_pos = db.Column(db.Integer, nullable=False)
    # brand_id = db.Column(db.Integer, nullable=False)
    style_number = db.Column(db.String(15), nullable=False)
    final_client_id = db.Column(db.Integer, nullable=False)