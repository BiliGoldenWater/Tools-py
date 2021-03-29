import pymouse.windows as py_mouse_windows
import pykeyboard.windows as py_keyboard_windows
import time
import json


class GenshinImpactPiano:
    def __init__(self, name: str = "",
                 bpm: int = 100,
                 sections_sequence: list = [],
                 sections_name: list = [],
                 sections: list = []):
        self.mouse = py_mouse_windows.PyMouse()
        self.keyboard = py_keyboard_windows.PyKeyboard()

        self.pos_calc = {"-1": [610, 1310],
                         "-2": [835, 1310],
                         "-3": [1060, 1310],
                         "-4": [1280, 1310],
                         "-5": [1505, 1310],
                         "-6": [1725, 1310],
                         "-7": [1950, 1310],
                         "1": [610, 1130],
                         "2": [835, 1130],
                         "3": [1060, 1130],
                         "4": [1280, 1130],
                         "5": [1505, 1130],
                         "6": [1725, 1130],
                         "7": [1950, 1130],
                         "8": [610, 950],
                         "9": [835, 950],
                         "+": [1060, 950],
                         '-': [1280, 950],
                         '*': [1505, 950],
                         '/': [1725, 950],
                         '=': [1950, 950]}
        self.pos = {"-1": [610, 1310],
                    "-2": [835, 1310],
                    "-3": [1060, 1310],
                    "-4": [1280, 1310],
                    "-5": [1505, 1310],
                    "-6": [1725, 1310],
                    "-7": [1950, 1310],
                    "1": [610, 1130],
                    "2": [835, 1130],
                    "3": [1060, 1130],
                    "4": [1280, 1130],
                    "5": [1505, 1130],
                    "6": [1725, 1130],
                    "7": [1950, 1130],
                    "+1": [610, 950],
                    "+2": [835, 950],
                    "+3": [1060, 950],
                    '+4': [1280, 950],
                    '+5': [1505, 950],
                    '+6': [1725, 950],
                    '+7': [1950, 950]}
        self.keys = {"-1": 'z',
                     "-2": 'x',
                     "-3": 'c',
                     "-4": 'v',
                     "-5": 'b',
                     "-6": 'n',
                     "-7": 'm',
                     "1": 'a',
                     "2": 's',
                     "3": 'd',
                     "4": 'f',
                     "5": 'g',
                     "6": 'h',
                     "7": 'j',
                     "+1": 'q',
                     "+2": 'w',
                     "+3": 'e',
                     '+4': 'r',
                     '+5': 't',
                     '+6': 'y',
                     '+7': 'u'}
        self.keys_calc = {"-1": 'z',
                          "-2": 'x',
                          "-3": 'c',
                          "-4": 'v',
                          "-5": 'b',
                          "-6": 'n',
                          "-7": 'm',
                          "1": 'a',
                          "2": 's',
                          "3": 'd',
                          "4": 'f',
                          "5": 'g',
                          "6": 'h',
                          "7": 'j',
                          "8": 'q',
                          "9": 'w',
                          "+": 'e',
                          '-': 'r',
                          '*': 't',
                          '/': 'y',
                          '=': 'u'}

        self.bpm = bpm
        self.name = name
        self.sections_sequence = sections_sequence
        self.sections_name = sections_name
        self.sections = sections

        self.t = 60 / 160
        self.t = self.t * 1000

    def click(self, note):
        self.mouse.click(self.pos[note][0], self.pos[note][1])

    def click_keyboard(self, note):
        self.keyboard.tap_key(self.keys[note])

    def play_notes(self, notes, is_keyboard):
        up_down = [1, '', '+', '-']
        if not is_keyboard:
            for note in notes:
                for char in note[0]:
                    if char != '0' and char != ' ' and char != '+' and char != '-':
                        print(up_down[up_down[0]] + char, note[1])
                        self.click(up_down[up_down[0]] + char)
                        up_down[0] = 1
                        time.sleep(note[1] / 1000)
                    elif char == '0':
                        up_down[0] = 1
                        time.sleep(note[1] / 1000)
                    elif char == '+':
                        up_down[0] = 2
                    elif char == '-':
                        up_down[0] = 3
        else:
            for note in notes:
                for char in note[0]:
                    if char != '0' and char != ' ' and char != '+' and char != '-':
                        print(up_down[up_down[0]] + char, note[1])
                        self.click_keyboard(up_down[up_down[0]] + char)
                        up_down[0] = 1
                        time.sleep(note[1] / 1000)
                    elif char == '0':
                        up_down[0] = 1
                        time.sleep(note[1] / 1000)
                    elif char == '+':
                        up_down[0] = 2
                    elif char == '-':
                        up_down[0] = 3

    def play(self, is_keyboard: bool):
        for now in self.sections_sequence:
            self.play_notes(self.sections[now], is_keyboard)

    def write_to_file(self):
        with open("Spectrum/{}.json".format(self.name, self.name), mode="w", encoding="utf-8") as f:
            json_data = {
                "name": self.name,
                "sections_sequence": self.sections_sequence,
                "sections_name": self.sections_name,
                "sections": self.sections
            }

            f.write(json.dumps(json_data))

    def load_from_file(self, name):
        with open("Spectrum/{}.json".format(name, name), mode="r", encoding="utf-8") as f:
            json_str = f.read()
            json_data = json.loads(json_str)
            self.name = json_data["name"]
            self.sections_sequence = json_data["sections_sequence"]
            self.sections_name = json_data["sections_name"]
            self.sections = json_data["sections"]


t = (60 / 100) * 1000

# ["", t],

notes_1 = [
    # row 1
    # 1
    ["-1", t],
    ["-5 1", 0], ["0", t],
    ["1 3", 0], ["0", t],
    # 2
    ["-1", t],
    ["-5 1", 0], ["0", t],
    ["13", 0], ["0", t],
    # 3
    ["-1", t],
    ["-5 1", 0], ["0", t],
    ["13", 0], ["0", t],
    # 4
    ["-1", t],
    ["-5 1", 0], ["0", t],
    ["13 +1", 0], ["0 +2", t / 2],
    # 5
    ["-1 +3", 0], ["0 +1", t / 2],
    ["-5 1 +5", 0], ["0", t],
    ["13 +5", 0], ["0 +3", t / 2],
    # 6
    ["-1 +2", 0], ["0", t],  # --7
    ["-7 2 +5", 0], ["0", t],
    ["25 +2", 0], ["0", t],
    # row 2
    # 7
    ["-1 +1", 0], ["06", t / 2],  # -1 = --6
    ["-6 1 +3", 0], ["0", t],
    ["13 +3", 0], ["0 +1", t / 2],
    # 8
    ["-3 7", 0], ["0", t],
    ["-7 3", 0], ["0", t],
    ["-5 -7 7", 0], ["0", t],
    # 9
    ["-4 6", 0], ["0", t],
    ["-6 1 7", 0], ["0", t],
    ["14 +1", 0], ["0 +2", t / 2],
    # 10
    ["-3 5", 0], ["0", t],
    ["-5 1 +1", 0], ["0", t],
    ["13 +2", 0], ["0 +3", t / 2],
    # 11
    ["-2 +4", 0], ["0", t],
    ["-6 2 +4", 0], ["0 +3", t / 2],
    ["24 +2", 0], ["0 +1", t / 2],
    # 12
    ["-1 +2", 0], ["0", t],
    ["-7 2", 0], ["0", t],
    ["24 +1", 0], ["0 +2", t / 2],
    # row 3
    # 13
]

piano = GenshinImpactPiano("AlwaysWithYou",
                           130,
                           [0],
                           ["notes_1"],
                           [notes_1])

time.sleep(3)

# piano = GenshinImpactPiano()
# piano.load_from_file("SenbonZakura")
# piano.load_from_file("GokurakuJodo")

piano.play(True)
piano.write_to_file()
