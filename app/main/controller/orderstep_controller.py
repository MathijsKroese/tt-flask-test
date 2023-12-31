from flask import request
from flask_restx import Resource
from app.main.model.orderstep import OrderStep, OrderStepDTO
from app.main.service import orderstep_service as _ss


api = OrderStepDTO.api
new_dto = OrderStepDTO.as_dto()


@api.route('/order/<order_code>')
class OrderstepsByOrderCode(Resource):
    @api.marshal_list_with(new_dto, envelope="steps")
    def get(self, order_code):
        return _ss.get_step_by_order(order_code)

    @api.expect(new_dto)
    @api.response(201, "step created")
    def post(self, order_code):
        data = request.json
        return _ss.assign_to_order(order_code, data)