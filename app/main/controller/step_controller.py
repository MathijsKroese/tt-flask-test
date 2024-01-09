from flask import request
from flask_restx import Resource
from ..dto.step import StepDTO
from ..service import step_service as _os

api = StepDTO.api
_request_dto = StepDTO.request_model
_response_dto = StepDTO.response_model


@api.route('/order/<order_code>')
class OrderstepsByOrderCode(Resource):
    @api.marshal_list_with(_response_dto, envelope="steps")
    def get(self, order_code):
        return _os.get_steps_by_order_code(order_code)

    @api.expect(_request_dto)
    # @api.response(201, "step created")
    def post(self, order_code):
        data = request.json
        return _os.assign_to_order(order_code, data)
