from .enums import CommandType, DeviceType


class Command:
    def __init__(self, device_type: DeviceType, command_type: CommandType):
        self.device_type = device_type
        self.command_type = command_type

    @staticmethod
    def from_dict(command: dict) -> 'Command':
        device_type = command['device_type']
        command_type = command['command_type']

        command = Command.parse(command)

        return Command(device_type, command_type)

    @staticmethod
    def parse(command: dict) -> dict:

        result_data = {}
        try:
            if command['device_type'].lower() in DeviceType.values:
                result_data['device_type'] = command['device_type'].lower()
        except:
            raise Exception('Device type not found in command')

        try:
            if command['command_type'].lower() in CommandType.values:
                result_data['command_type'] = command['command_type'].lower()
        except:
            raise Exception('Command type not found in command')

        return result_data
