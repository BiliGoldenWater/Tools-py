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


# t = (60 / 140) * 1000
#
# # ["", t],
#
# notes_1 = [
#     # row 1
#     # 1
#     ["0035", t / 2],
#     # 2
#     ["60056005", t / 2],
#     # 3
#     ["6 +1 563035", t / 2],
#     # 4
#     ["60056005", t / 2],
#     # 5
#     ["6 +3 +1 +2 6035", t / 2],
#     # row 2
#     # 1
#     ["60056005", t / 2],
#     # 2
#     ["6 +1 563512", t / 2],
#     # 3
#     ["3 +1 6 +3", t],
#     # 4
#     ["+2", t / 2],
#     ["+3 +2", t / 4],
#     ["+1 +2", t / 2],
#     ["60", t],
# ]
#
# notes_2 = [
#     # row 3
#     # 1
#     ["666", t],
#     ["6 +1 +2 +3", t / 4],
#     # 2
#     ["66", t],
#     ["6556", t / 2],
#     # 3
#     ["666", t],
#     ["6 +1 +2 +3", t / 4],
#     # 4
#     ["66", t],
#     ["6 +4 +4 +3", t / 2],
#     # row 4
#     # 1
#     ["666", t],
#     ["6 +1 +2 +3", t / 4],
#     # 2
#     ["66", t],
#     ["6556", t / 2],
#     # 3
#     ["666", t],
#     ["6 +1 +2 +3", t / 4],
#     # 4
#     ["+6", t + (t / 2)],
#     ["556", t / 2],
#     ["6", t],
#     # row 5
#     # 1
#     ["0", t],
#     ["066", t / 2],
#     ["55", t / 4],
#     ["56", t / 2],
#     # 2
#     ["533", t / 2],
#     ["53", t / 4],
#     ["30", t],
#     # 3
#     ["0", t],
#     ["066567", t / 2],
#     # 4
#     ["+1 7", t],
#     ["6", t / 2],
#     ["76", t / 4],
#     ["5", t],
#     # row 6
#     # 1
#     ["0", t],
#     ["06655", t / 2],
#     ["65", t / 4],
#     # 2
#     ["533", t / 2],
#     ["53", t / 4],
#     ["3", t],
#     ["05", t / 2],
#     # 3
#     ["5605560", t / 2],
#     ["67", t / 4],
#     # 4
#     ["+1 +2", t],
#     ["6335", t / 2],
#     # row 7
#     # 1
#     ["560 +3", t / 2],
#     ["+2", t],
#     ["06", t / 2],
#     # 2
#     ["066 +3", t / 2],
#     ["+2 0", t],
#     # 3
#     ["0 +2 +2 +1 +2", t / 2],
#     ["+1 6", t / 4],
#     ["65", t / 2],
#     # 4
#     ["55566335", t / 2],
#     # row 8
#     # 1
#     ["560 +3", t / 2],
#     ["+2", t],
#     ["06", t / 2],
#     # 2
#     ["066 +3", t / 2],
#     ["+2 0", t],
#     # 3
#     ["0 +2 +2 +1 +2", t / 2],
#     ["+1 6 6 3", t / 4],
#     ["5", t / 2],
#     # 4
#     ["5665", t / 2],
#     ["6", t],
#     ["0", t / 2],
#     ["35", t / 4],
#     # row 9
#     # 1
#     ["666 +3", t / 2],
#     ["+3", t],
#     ["0", t / 2],
#     ["7 +1", t / 4],
#     # 2
#     ["+2", t / 2],
#     ["+1 +2", t],
#     ["+2 +3", t / 2],
#     ["6", t],
#     ["0", t / 2],
#     ["55", t / 2],
#     # 3
#     ["6", t],
#     ["+3", t / 2 + (t / 2 / 2)],
#     ["+3", t / 4],
#     ["+2 +1 65", t / 2],
#     # 4
#     ["6", t / 2 + (t / 2 / 2)],
#     ["6", t / 4],
#     ["6 +1 +2 0", t / 2],
#     # row 10
#     # 1
#     ["6", t / 2],
#     ["66", t / 4],
#     ["6", t / 2],
#     ["55", t / 4],
#     ["6 +3 0 +1", t / 2],
#     # 2
#     ["+2", t / 2],
#     ["+1 +2", t / 4],
#     ["+2 +3", t / 2],
#     ["+3", t],
#     ["0 5", t / 2],
#     # 3
#     ["6 +1 056 +3 0", t / 2],
#     ["+3 +2", t / 4],
#     # 4
#     ["+1 7655", t / 2],
#     ["6", t],
#     ["0", t / 2],
# ]
#
# notes_3 = [
#     # row 11
#     # 1
#     ["0653231 -5", t / 2],
#     # 2
#     ["-6 -5 -6 0", t / 2],
#     ["-6 0", t],
#     # 3
#     ["-6 0 -7 0", t],
#     # 4
#     ["-6 -7", t / 4],
#     ["-6", t / 2],
#     ["-6 -7", t / 4],
#     ["-6", t / 2],
#     ["10", t],
#     # 5
#     ["-7 653231 -5", t / 2],
#     # row 12
#     # 1
#     ["-6 -5 -6 0", t / 2],
#     ["-6 0", t],
#     # 2
#     ["-6 0 -7 0", t],
#     # 3
#     ["-6 -7", t / 4],
#     ["-6", t / 2],
#     ["-6 -7", t / 4],
#     ["-6", t / 2],
#     ["10", t],
#     # 4
#     ["-7 -5", t],
#     ["65321 -6 21", t / 4],
#     # row 13
#     # 1
#     ["6565 +1 765", t / 2],
#     # 2
#     ["532132", t / 2],
#     ["1 -6 -5 -6", t / 4],
#     # 3
#     ["-5", t + (t / 2)],
#     ["-3 -2", t / 4],
#     ["-3 0", t],
#     # 4
#     ["-2 -3 -4 -5 -6 -7 12234567 +1 +2", t / 4],
#     # row 14
#     # 1
#     ["+3", t / 2],
#     ["+3", t + (t / 2)],
#     ["+3", t],
#     ["+2 +1", t / 2],
#     # 2
#     ["7", t / 2],
#     ["+1", t],
#     ["+2 7", t / 2],
#     ["5", t],
#     ["2", t / 2],
#     # 3
#     ["+2", t + (t / 2)],
#     ["+1", t],
#     ["75", t],
#     # 4
#     ["70", t],
#     ["6335", t / 2],
#     # row 15
#     # 1
#     ["560 +3", t / 2],
#     ["+2", t],
#     ["06", t / 2],
#     # 2
#     ["066 +3", t / 2],
#     ["+2 0", t],
#     # 3
#     ["+1", t + (t / 2)],
#     ["+2 +3 +5 +3 +5", t / 2],
#     # 4
#     ["+7", t],
#     ["+6 +5 +3 335", t / 2],
#     # row 16
#     # 1
#     ["560 +3", t / 2],
#     ["+2", t],
#     ["06", t / 2],
#     # 2
#     ["066 +3", t / 2],
#     ["+2 0", t],
#     # 3
#     ["0 +2 +2 +1 +2", t / 2],
#     ["+1 6", t / 4],
#     ["6", t / 2],
#     ["35", t / 4],
#     # 4
#     ["5665", t / 2],
#     ["6", t],
#     ["0", t / 2],
#     ["35", t],
#     # row 17
#     # 1
#     ["666 +3", t / 2],
#     ["+3", t],
#     ["0", t / 2],
#     ["7 +1", t / 4],
#     # 2
#     ["+2", t / 2],
#     ["+1 +2", t / 4],
#     ["+2 +3", t / 2],
#     ["6", t],
#     ["0", t / 2],
#     ["55", t / 4],
#     # 3
#     ["6", t],
#     ["+3", t / 2 + (t / 2 / 2)],
#     ["+3", t / 4],
#     ["+2 +1 65", t / 2],
#     # 4
#     ["+6", t / 2 + (t / 2 / 2)],
#     ["6", t / 4],
#     ["6 +1", t / 2],
#     ["+2 0", t],
#     # row 18
#     # 1
#     ["6", t / 2],
#     ["66", t / 4],
#     ["6", t / 2],
#     ["55", t / 4],
#     ["6 +3 0 +1", t / 2],
#     # 2
#     ["+2", t / 2],
#     ["+1 +2", t / 4],
#     ["+2 +3", t / 2],
#     ["+3", t],
#     ["0 +3", t / 2],
#     # 3
#     ["+2 +2 0 +1 +2 +2 0", t / 2],
#     ["+3 +2", t / 4],
#     # 4
#     ["+1 7655605", t / 2],
#     # row 19
#     # 1
#     ["6 +1 056 +5 0", t / 2],
#     ["+3 +2", t / 4],
#     # 2
#     ["+2 +2 +3 +5", t / 2],
#     ["+5 +6", t],
#     # 3
#     ["666", t],
#     ["6 +1 +2 +3", t / 4],
#     # 4
#     ["66", t],
#     ["6556", t / 2],
#     # row 20
#     # 1
#     ["666", t],
#     ["6 +1 +2 +3", t / 4],
#     # 2
#     ["66", t],
#     ["6 +4 +4 +3", t / 2],
#     # 3
#     ["666", t],
#     ["6 +1 +2 +3", t / 4],
#     # 4
#     ["66", t],
#     ["6556", t / 2],
#     # row 21
#     # 1
#     ["666", t],
#     ["6 +1 +2 +3", t / 4],
#     # 2
#     ["+6", t + (t / 2)],
#     ["556", t / 2],
#     ["6", t],
#
# ]
#
# piano = GenshinImpactPiano("GokurakuJodo",
#                            160,
#                            [0, 1, 1, 2],
#                            ["notes_1", "notes_2", "notes_3"],
#                            [notes_1, notes_2, notes_3])

time.sleep(3)

piano = GenshinImpactPiano()
# piano.load_from_file("SenbonZakura")
piano.load_from_file("GokurakuJodo")

piano.play(True)
piano.write_to_file()
