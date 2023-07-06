import time
from controller.keyboard_command import KeyboardCommand
from controller.enums import CommandType, DeviceType

if __name__ == "__main__":
    keyboard_handler = KeyboardCommand()

    keyboard_handler.execute()

    keyboard_handler.modified_execute(
        {'device_type': DeviceType.KEYBOARD, 'command_type': CommandType.PRESS, 'key': 'a'})
