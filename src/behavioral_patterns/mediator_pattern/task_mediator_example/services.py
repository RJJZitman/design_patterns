from tasks import PrintTask
from i_task import ITask
from i_service import IService


class PrintService(IService):
    def perform_task(self, task: ITask):
        if isinstance(task, PrintTask):
            print(f"Executing task '{task.name}': {task.message}")
