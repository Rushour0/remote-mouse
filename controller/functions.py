from pynput.keyboard import Controller, Key
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


def parse_key_string(key_string):
    keyboard = Controller()
    keys = key_string.split('+')

    for key in keys:
        key = key.strip().lower()

        if key == '':
            continue

        if key in key_map:
            key_action = key_map[key]
            if key_action == Key.enter:
                keyboard.press(key_action)
                keyboard.release(key_action)
            else:
                keyboard.press(key_action)
        else:
            # If the key is not found in the key_map, assume it is a printable character
            keyboard.press(key)

    for key in reversed(keys):
        key = key.strip().lower()

        if key == '':
            continue

        if key in key_map and key_map[key] != Key.enter:
            key_action = key_map[key]
            keyboard.release(key_action)
        else:
            # If the key is not found in the key_map, assume it is a printable character
            keyboard.release(key)

if __name__ == "__main__":
    print(parse_key_string('ctrl+shift+a'))
