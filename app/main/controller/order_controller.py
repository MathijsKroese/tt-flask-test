from flask import request
from flask_restx import Resource
from ..service import order_service as _os
from ..dto.order import OrderDTO


api = OrderDTO.api
_request_dto = OrderDTO.request_model
_response_dto = OrderDTO.response_model

@api.route('/')
class GetAl(Resource):
    @api.response(200, "success")
    @api.marshal_list_with(_response_dto, envelope="orders")
    def get(self):
        return _os.get_all_orders()


@api.route('/<order_code>')
class OrderByOrderline(Resource):
    # @api.response(200, "success")
    @api.marshal_list_with(_response_dto, envelope="orders")
    def get(self, order_code):
        return _os.get_by_order_code(order_code)

    @api.expect(_request_dto)
    @api.marshal_list_with(_response_dto, envelope="orders")
    # @api.response(201, "order created")
    def post(self, order_code):
        data = request.json
        return _os.add_new_order(data=data, order_code=order_code)

    # @api.param("order_code", "The identifier code to be retrieved")
    @api.marshal_list_with(_response_dto, envelope="orders")
    def get(self, order_code):
        return _os.get_by_order_code(order_code)
