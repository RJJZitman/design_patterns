from typing import Type

from i_service import IService
from i_task import ITask, TaskState


class WorkflowMediator:
    _services: dict[str, IService] = {}

    def __init__(self):
        self.tasks: list[ITask] = []

    def add_task(self, task: ITask):
        self.tasks.append(task)

    @staticmethod
    def register_service(task_type: Type[ITask], service: IService):
        print(WorkflowMediator._services)
        if task_type.__name__ not in list(WorkflowMediator._services):
            WorkflowMediator._services[task_type.__name__] = service
        print(f"task type: {task_type} is registered under key {task_type.__name__}.")

    @staticmethod
    def notify(task: ITask, event: str):
        if event == "execute":
            task.state = TaskState.IN_PROGRESS
            service = WorkflowMediator._services[task.__class__.__name__]
            try:
                service.perform_task(task=task)
                task.state = TaskState.COMPLETED
            except Exception as e:
                task.state = TaskState.FAILED
                print(f"Task '{task.name}' failed: {e}")

    def run(self):
        for task in self.tasks:
            if task.state == TaskState.PENDING:
                task.execute(self)
