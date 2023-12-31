from flask import request
from flask_restx import Resource
from app.main.model.task import TaskDTO
from app.main.service import task_service as _ts

api = TaskDTO.api
new_dto = TaskDTO.as_dto()

@api.route('/order/<order_code>')
class TasksByOrderCode(Resource):
    @api.marshal_list_with(new_dto, envelope="tasks")
    def get(self, order_code):
        return _ts.get_tasks_by_order_code(order_code)

    @api.expect(new_dto)
    @api.response(201, "task created")
    def post(self, order_code):
        data = request.json
        return _ts.assign_to_order(order_code, data)
