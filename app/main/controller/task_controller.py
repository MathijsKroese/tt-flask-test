from flask import request
from flask_restx import Resource
from ..dto.task import TaskDTO
from ..service import task_service as _ts
from ..util.enum import TaskStatus
from typing import Dict, Tuple

api = TaskDTO.api
_dto = TaskDTO.model
_status_options = TaskDTO.status_options

@api.route('/<order_code>')
class TasksByOrderCode(Resource):
    # @api.param("order_code", "The order associated with this task")
    @api.marshal_list_with(_dto, envelope="tasks")
    def get(self, order_code):
        return _ts.get_tasks_by_order_code(order_code)

    @api.expect(_dto)
    # @api.param("order_code", "The order associated with this task")
    @api.response(201, "task created")
    def post(self, order_code) -> Tuple[Dict[str, str], int]:
        data = request.json
        return _ts.assign_to_order(order_code=order_code, data=data)


@api.route('/<task_id>')
class UpdateTaskStatus(Resource):
    @api.expect(_status_options)
    # @api.param("task_id", "The identifier for a specific task")
    @api.response(201, "task status updated")
    def put(self, task_id):
        data = request.json
        return _ts.update_task(task_id, data)
