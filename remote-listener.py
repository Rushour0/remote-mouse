from pynput.keyboard import Key, Controller as KeyboardController,  Listener as KeyboardListener
from pynput.mouse import Button, Controller as MouseController, Listener as MouseListener

from threading import Thread
import time
import sys
import os
import subprocess
import socket
import pickle
import pyautogui


class RemoteListener:

    def __init__(self, port=2300):

        self.connected = False
        self.port = port
        self.mouse = MouseController()
        self.keyboard = KeyboardController()

        self.socket = socket.socket()
        self.socket.connect(('127.0.0.1', port))

    def background_executor(self):
        
        command = self.socket.recv((1024)).decode()

        if command == 'mouse':
            self.mouse.move(1, 1)
