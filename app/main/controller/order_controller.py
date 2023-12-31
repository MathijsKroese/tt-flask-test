from flask import request
from app.main.model.order import OrderDTO
from app.main.service import order_service as _os
from flask_restx import Resource

api = OrderDTO.api
new_dto = OrderDTO.as_dto()


@api.route('/orderline/<orderline_id>')
class OrderByOrderline(Resource):
    @api.marshal_list_with(new_dto, envelope="orders")
    def get(self, orderline_id):
        return _os.get_orders_by_orderline(orderline_id)

    @api.expect(new_dto)
    @api.response(201, "order created")
    def post(self, orderline_id):
        data = request.json
        return _os.assign_to_orderline(orderline_id, data)


@api.route('/<order_code>')
class OrderByCode(Resource):
    @api.marshal_list_with(new_dto, envelope="orders")
    def get(self, order_code):
        return _os.get_by_order_code(order_code)
