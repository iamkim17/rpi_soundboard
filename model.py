import json
import os

from consts import *
from pathlib import Path


class JsonFileCreateException(Exception):
    """ raised when json model could not be created """
    pass


class JsonFileOpenException(Exception):
    """ raised when json model could not be opened """
    pass


class JsonFileWriteException(Exception):
    """ raised when json model could not be written """
    pass


class DirCreationException(Exception):
    """ raised when """
    pass

class CopyFileException(Exception):
    """ raised when """
    pass


class Model():
    def __init__(self, data_path):

        self.data_path = data_path

        # check if ~/.FILE_NAME exists
        if not self.data_path.is_dir(): 
            # try to create ~/.FILE_NAME dir
            try:
                os.mkdir(self.data_path)
            except Exception as e:
                raise DirCreateException



        # check if data.json exists
        self.json_path = Path.joinpath(self.data_path, 'data.json') 

        self.data = dict()
        
        if not self.json_path.is_file():
            # try to create the json model
            try:
                with open(self.json_path.resolve(), 'w') as json_file:

                    self.data = { "template": "template" }
                
                    json.dump(self.data, json_file, sort_keys=True, indent=4)

            except Exception as e:
                raise JsonFileCreateException 

        # read config
        else: 
            with open(self.json_path.resolve(), 'r') as json_file:
                self.data = json.load(json_file)

        self.observers = []


    def register_observer(self, observer):
        self.observers.append(observer)

    def __notify_observers(self):
        for observer in self.observers:
            observer.notify()

    def get_gpio_pin_default_name(self):
        return "Not Assigned"
    
    def get_gpio_pin_names(self):
        return [self.get_gpio_pin_default_name(),
                "3 (GPIO 2/SDA)", 
                "5 (GPIO 3/SCL)", 
                "7 (GPIO 4/GPCLK0)",
                "8 (GPIO 14/TXD)",
                "10 (GPIO 15/RXD)",
                "11 (GPIO 17)",
                "12 (GPIO 18/PCM_CLK)",
                "13 (GPIO 27)",
                "15 (GPIO 22)",
                "16 (GPIO 23)",
                "18 (GPIO 24)",
                "19 (GPIO 10/MOSI)",
                "21 (GPIO 9/MISO)",
                "23 (GPIO 11/SCLK)",
                "24 (GPIO 8/CE0)",
                "26 (GPIO 7/CE1)",
                "27 (GPIO 0/ID_SD)",
                "28 (GPIO 1/ID_SC)",
                "29 (GPIO 5)",
                "31 (GPIO 6)",
                "32 (GPIO 12/PWM0)",
                "33 (GPIO 13/PWM1)",
                "35 (GPIO 19/PCM_FS)",
                "36 (GPIO 16)",
                "37 (GPIO 26)",
                "38 (GPIO 20/PCM_DIN)",
                "40 (GPIO 21/PCM_DOUT)"
                ]
