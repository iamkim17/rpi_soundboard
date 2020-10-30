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

                    self.data = { 
                            "sounds": [
                                    {
                                        "number": 1,
                                        "pin": self.get_gpio_pin_default_name(),
                                        "file_path": None,
                                        "volume": 0.8
                                    },
                                    {
                                        "number": 2,
                                        "pin": self.get_gpio_pin_default_name(),
                                        "file_path": None,
                                        "volume": 0.8
                                    },
                                    {
                                        "number": 3,
                                        "pin": self.get_gpio_pin_default_name(),
                                        "file_path": None,
                                        "volume": 0.8
                                    },
                                    {
                                        "number": 4,
                                        "pin": self.get_gpio_pin_default_name(),
                                        "file_path": None,
                                        "volume": 0.8
                                    },
                                    {
                                        "number": 5,
                                        "pin": self.get_gpio_pin_default_name(),
                                        "file_path": None,
                                        "volume": 0.8
                                    },
                                    {
                                        "number": 6,
                                        "pin": self.get_gpio_pin_default_name(),
                                        "file_path": None,
                                        "volume": 0.8
                                    },
                                    {
                                        "number": 7,
                                        "pin": self.get_gpio_pin_default_name(),
                                        "file_path": None,
                                        "volume": 0.8
                                    }
                                ]
                            } 
                
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

    def __save_json(self):
        try:
            with open(self.json_path.resolve(), 'w') as json_file:
                json.dump(self.data, json_file, sort_keys=True, indent=4)

        except Exception as e:
            raise JsonFileWriteException

    def get_num_sounds(self):
        return len(self.data['sounds'])

    def get_pin_for_sound(self, sound_number):
        for sound in self.data['sounds']:
            if sound['number'] == sound_number:
                return sound['pin']

    def set_pin_for_sound(self, sound_number, pin):
        for sound in self.data['sounds']:
            if sound['number'] == sound_number:
                sound['pin'] = pin

        self.__save_json()
        self.__notify_observers()

    def get_file_path_for_sound(self, sound_number):
        for sound in self.data['sounds']:
            if sound['number'] == sound_number:
                if sound['file_path'] is None:
                    return ""
                return sound['file_path']

    def set_file_path_for_sound(self, sound_number, file_path):
        for sound in self.data['sounds']:
            if sound['number'] == sound_number:
                sound['file_path'] = file_path

        self.__save_json()
        self.__notify_observers()

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

    def get_unassigned_gpio_pin_names(self):
        gpio_pin_names = self.get_gpio_pin_names()
        assigned_gpio_pin_names = []

        for sound in self.data['sounds']:
            assigned_gpio_pin_names.append(sound['pin'])

        filtered_gpio_pin_names = [x for x in gpio_pin_names if x not in assigned_gpio_pin_names]

        if self.get_gpio_pin_names() not in filtered_gpio_pin_names:
            return self.get_gpio_pin_names() + filtered_gpio_pin_names

        return filtered_gpio_pin_names


    def get_volume_for_sound(self, sound_number):
        for sound in self.data['sounds']:
            if sound['number'] == sound_number:
                return sound['volume']

    def set_volume_for_sound(self, sound_number, volume):
        for sound in self.data['sounds']:
            if sound['number'] == sound_number:
                sound['volume'] = volume

        self.__save_json()

