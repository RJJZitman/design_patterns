from light import Light
from invoker import RemoteControl
from commands import LightOnCommand, LightOffCommand


if __name__ == "__main__":
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    remote = RemoteControl()

    remote.execute_command(light_on)
    remote.execute_command(light_off)
    remote.undo_last_command()
    remote.undo_last_command()
