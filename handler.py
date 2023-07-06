import signal


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    

def exit_gracefully():
    signal.signal(signal.SIGINT, signal_handler)
    