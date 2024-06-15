from light import Light
from invoker import RemoteControl
from commands import LightOnCommand, LightOffCommand, CompositeCommand


if __name__ == "__main__":
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    composite_command = CompositeCommand()

    # Adding commands to the composite command
    composite_command.add(light_on)
    composite_command.add(light_off)

    # Invoker
    remote = RemoteControl()

    # Executing composite command
    remote.execute_command(composite_command)

    # Undoing last command (composite command)
    remote.undo_last_command()
