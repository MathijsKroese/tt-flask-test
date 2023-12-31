from flask import request
from flask_restx import Resource
from app.main.service.orderline_service import add_new_orderline, get_all_orderlines, get_orderline_by_id
from app.main.service.auth_service import requires_auth, requires_scope
from app.main.model.orderline import Orderline, OrderlineDTO
from typing import Dict, Tuple

api = OrderlineDTO.api
new_dto = OrderlineDTO.as_new_orderline()
existing_dto = OrderlineDTO.as_existing_orderline()

@api.route('/')
# @requires_auth
class OrderlineList(Resource):
    @api.marshal_list_with(existing_dto, envelope="order lines")
    def get(self):
        return get_all_orderlines()

    @api.expect(new_dto)
    @api.response(201, "orderline created")
    def post(self) -> Tuple[Dict[str, str], int]:
        data = request.json
        return add_new_orderline(data)


@api.route('/<orderline_id>')
class OrderLineById(Resource):
    @api.marshal_list_with(existing_dto, envelope="order lines")
    def get(self, orderline_id):
        return get_orderline_by_id(orderline_id)
