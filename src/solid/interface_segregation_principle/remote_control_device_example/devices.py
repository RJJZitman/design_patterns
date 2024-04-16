from interfaces import ChannelChangeable, VolumeControllable


class TV(ChannelChangeable, VolumeControllable):
    def turn_on(self):
        print("TV turned on")

    def turn_off(self):
        print("TV turned off")

    def change_channel(self, channel):
        print(f"TV channel changed to {channel}")

    def adjust_volume(self, volume):
        print(f"TV volume adjusted to {volume}")


class Stereo(VolumeControllable):
    def turn_on(self):
        print("Stereo turned on")

    def turn_off(self):
        print("Stereo turned off")

    def adjust_volume(self, volume):
        print(f"Stereo volume adjusted to {volume}")
