from i_task import ITask, TaskState
from workflow_mediator import WorkflowMediator


class PrintTask(ITask):
    def __init__(self, name: str, message: str):
        super().__init__(name)
        self.message = message

    def execute(self, mediator: WorkflowMediator):
        if all(dep.state == TaskState.COMPLETED for dep in self.dependencies):
            mediator.notify(task=self, event="execute")
        else:
            print(f"Task '{self.name}' is waiting for dependencies to complete")
