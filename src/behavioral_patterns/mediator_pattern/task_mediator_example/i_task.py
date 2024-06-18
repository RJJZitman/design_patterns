from enum import Enum
from abc import ABC, abstractmethod


class TaskState(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED = "Failed"


class ITask(ABC):
    def __init__(self, name: str):
        self.name = name
        self.state = TaskState.PENDING
        self.dependencies = []

    def add_dependency(self, task):
        self.dependencies.append(task)

    @abstractmethod
    def execute(self, mediator):
        pass
