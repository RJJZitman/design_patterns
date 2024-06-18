from tasks import PrintTask
from services import PrintService
from workflow_mediator import WorkflowMediator


if __name__ == "__main__":
    mediator = WorkflowMediator()
    mediator.register_service(task_type=PrintTask, service=PrintService())

    # Create tasks with dependencies
    task1 = PrintTask(name="Task1", message="Print this message")
    task2 = PrintTask(name="Task2", message="Print another message")
    task3 = PrintTask(name="Task3", message="This message depends on Task1 and Task2")

    task3.add_dependency(task=task1)
    task3.add_dependency(task=task2)

    mediator.add_task(task=task1)
    mediator.add_task(task=task3)
    mediator.add_task(task=task2)

    # Run the workflow
    mediator.run()
    print(task3.state)
    mediator.run()  # Run again to check if dependent tasks execute after their dependencies complete
