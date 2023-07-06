from pynput.keyboard import Key, Controller
from .command import Command, DeviceType, CommandType


class KeyboardCommand(Command):

    key_map = {
        'alt': Key.alt,
        'ctrl': Key.ctrl,
        'shift': Key.shift,
        'esc': Key.esc,
        'enter': Key.enter,
        'space': Key.space,
        'tab': Key.tab,
        'up': Key.up,
        'down': Key.down,
        'left': Key.left,
        'right': Key.right,
        'backspace': Key.backspace,
        'caps_lock': Key.caps_lock,
        'delete': Key.delete,
        'end': Key.end,
        'f1': Key.f1,
        'f2': Key.f2,
        'f3': Key.f3,
        'f4': Key.f4,
        'f5': Key.f5,
        'f6': Key.f6,
        'f7': Key.f7,
        'f8': Key.f8,
        'f9': Key.f9,
        'f10': Key.f10,
        'f11': Key.f11,
        'f12': Key.f12,
        'home': Key.home,
        'insert': Key.insert,
        'num_lock': Key.num_lock,
        'page_down': Key.page_down,
        'page_up': Key.page_up,
        'pause': Key.pause,
        'print_screen': Key.print_screen,
        'scroll_lock': Key.scroll_lock,
        'shift_r': Key.shift_r,
        'shift_l': Key.shift_l,
        'super': Key.cmd,
        'super_l': Key.cmd_l,
        'super_r': Key.cmd_r,
        'alt_l': Key.alt_l,
        'alt_r': Key.alt_r,
        'ctrl_l': Key.ctrl_l,
        'ctrl_r': Key.ctrl_r,
        'menu': Key.menu
    }

    def __init__(self, command_type: CommandType = CommandType.TAP, key: str = ''):
        super().__init__(DeviceType.KEYBOARD, command_type)
        self.key: str = key

    @staticmethod
    def parse(command: dict) -> dict:
        """
        This method parses a command dictionary and returns a dictionary with the device type, command type, and key.

        Format:
            device_type: keyboard
            command_type: press, release, tap, type
            key: key to press, release, tap, or type


        Args:
            command (dict): Command Dictionary to parse

        Returns:
            dict: Validated command dictionary
        """
        try:
            base_result = Command.parse(command)
        except Exception as e:
            raise e

        if base_result['device_type'] != DeviceType.KEYBOARD:
            raise Exception('Command device is not valid')

        try:
            base_result['key'] = command['key']
        except:
            raise Exception('Key not found in command')

        return base_result

    @staticmethod
    def from_dict(command: dict):
        command = KeyboardCommand.parse(command)
        base_result = Command.from_dict(command)

        result = KeyboardCommand(base_result.command_type, command['key'])

        return result

    def __execute_command(self):
        """
        This method executes the command on the keyboard.

        Functionality:
            Complex commands
            Presses a key
            Releases a key
            Taps a key
            Types a key
        """
        key = self.key
        command_type = self.command_type
        
        if key == '' or key is None:
            return

        if command_type == CommandType.COMPLEX:
            self.__execute_complex_command()
            return

        keyboard = Controller()

        if key in KeyboardCommand.key_map:
            key_action = KeyboardCommand.key_map[key]

            if command_type == CommandType.PRESS:
                keyboard.press(key_action)

            elif command_type == CommandType.RELEASE:
                keyboard.release(key_action)

            elif command_type == CommandType.TAP:
                keyboard.tap(key_action)

            elif command_type == CommandType.TYPE:
                raise Exception(
                    'Cannot type a key that is not a printable character')

        else:
            if command_type == CommandType.TYPE:
                keyboard.type(key)

            if command_type == CommandType.PRESS:
                keyboard.press(key)

            if command_type == CommandType.RELEASE:
                keyboard.release(key)

            if command_type == CommandType.TAP:
                keyboard.tap(key)

    def __execute_complex_command(self):
        """
        This method parses a string of keys and performs the corresponding actions on the keyboard.

        Format:
            press_<key> - Presses the key
            release_<key> - Releases the key
            tap_<key> - Taps the key
            <key> - Types the key

        Functionality:
            Complex commands parsing and execution
        """

        key_string = self.key

        keyboard = Controller()
        keys = key_string.split('+')
        length = len(keys)

        for i in range(length):
            key = keys[i].strip().lower()

            if key == '':
                continue

            if key.startswith('press_'):
                key = key.replace('press_', '')
                if key in KeyboardCommand.key_map:
                    key = KeyboardCommand.key_map[key]
                keyboard.press(key)

            elif key.startswith('release_'):
                key = key.replace('release_', '')
                if key in KeyboardCommand.key_map:
                    key = KeyboardCommand.key_map[key]
                keyboard.release(key)

            elif key.startswith('tap_'):
                key = key.replace('tap_', '')
                if key in KeyboardCommand.key_map:
                    key = KeyboardCommand.key_map[key]
                keyboard.tap(key)

            else:
                if key in KeyboardCommand.key_map:
                    key = KeyboardCommand.key_map[key]
                keyboard.type(key)

    def execute(self):
        self.__execute_command()

    def modified_execute(self, command: dict):
        parsed_command = KeyboardCommand.parse(command)
        self.key = parsed_command['key']
        self.command_type = parsed_command['command_type']
        self.execute()
