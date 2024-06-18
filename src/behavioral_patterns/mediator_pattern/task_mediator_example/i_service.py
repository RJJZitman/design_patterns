from abc import ABC, abstractmethod


class IService(ABC):
    @abstractmethod
    def perform_task(self, task):
        pass
