from devices import TV, Stereo
from device_controller import RemoteControl, MethodCommand

if __name__ == "__main__":

    tv_commands = [
        MethodCommand(method="change_channel", **{"channel": 5}),
        MethodCommand(method="adjust_volume", **{"volume": 20}),
    ]

    stereo_commands = [
        MethodCommand("adjust_volume", 20),
    ]

    tv_remote = RemoteControl(TV())
    with tv_remote:
        tv_remote.operate(tv_commands)

    with RemoteControl(Stereo()) as stereo_remote:
        stereo_remote.operate(stereo_commands)

    with TV() as tv:
        tv.change_channel(channel=4)
