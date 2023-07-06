class CommandType:
    CLICK = 'click'
    MOVE = 'move'
    PRESS = 'press'
    RELEASE = 'release'
    TAP = 'tap'
    TYPE = 'type'
    SCROLL = 'scroll'
    # complex commands are commands that are not a single command, but a combination of commands
    COMPLEX = 'complex'
    values = {CLICK, MOVE, PRESS, RELEASE, TYPE, SCROLL, COMPLEX}


class DeviceType:
    MOUSE = 'mouse'
    KEYBOARD = 'keyboard'
    values = {MOUSE, KEYBOARD}
