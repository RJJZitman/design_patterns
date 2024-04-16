from devices import TV, Stereo
from device_controller import RemoteControlDevice, DeviceMethodCommand

if __name__ == "__main__":

    tv_commands = [
        DeviceMethodCommand("change_channel", 5),
        DeviceMethodCommand("adjust_volume", 20),
    ]
    stereo_commands = [
        DeviceMethodCommand("adjust_volume", 20),
    ]

    tv_remote = RemoteControlDevice(TV())
    with tv_remote:
        tv_remote.operate(tv_commands)

    with RemoteControlDevice(Stereo()) as stereo_remote:
        stereo_remote.operate(stereo_commands)
