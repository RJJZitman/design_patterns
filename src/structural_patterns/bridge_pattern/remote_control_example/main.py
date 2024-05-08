from devices import TV, Radio
from remotes import BasicRemote, AdvancedRemote


if __name__ == "__main__":
    # Using Basic Remote with TV
    tv = TV()
    basic_remote = BasicRemote(tv)

    basic_remote.power()
    basic_remote.set_channel(5)

    # Using Advanced Remote with Radio
    radio = Radio()
    advanced_remote = AdvancedRemote(radio)

    advanced_remote.power()
    advanced_remote.set_channel(101.5)
