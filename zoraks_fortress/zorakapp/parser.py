from zorakapp.common import *
from typing import Dict, Union, List
from string import punctuation
import sys


class Parser:
    def __init__(self, raw_cmd: str = ""):
        self.raw_cmd = raw_cmd.lower().strip()
        self.initialize()
        self.clean_command()
        self.separate_parts()
        self.neutralize_verb()

    def initialize(self):
        # Initialize Parts
        self.verb = ""
        self.dir_obj_phrase = []
        self.preposition = ""
        self.obj_of_p_phrase = []

    def clean_command(self):
        # Remove Punctuation
        cmd = self.raw_cmd.translate(self.raw_cmd.maketrans("", "", punctuation))

        # Remove Sentence Articles (e.g. a, an, the, these...)
        self.raw_cmd = [word for word in cmd.split() if word not in ARTS]

    def get_direction(self, direction: str) -> str:
        dirs = {0: "north", 1: "south", 2: "east", 3: "west", 4: ""}
        i = next((xi for xi, d in dirs.items() if d.startswith(direction)), 4)
        self.preposition = "to"
        return [dirs[i]]

    def separate_parts(self):
        words = self.raw_cmd

        if words:
            # Get Verb
            if words[0] in DIRS:
                self.verb = "go"
                self.obj_of_p_phrase = self.get_direction(words[0])
                return
            self.verb = words[0]
            words = words[1:]

            # Find Preposition & Object of the Preposition
            index = next((i for i, item in enumerate(words) if item in PREP), None)
            if index is not None:
                self.obj_of_p_phrase = words[index:]
                words = words[:index]
                self.preposition = self.obj_of_p_phrase.pop(0)

            # Find Direct Object
            if words and words[0] in DIRS:
                self.obj_of_p_phrase = self.get_direction(words[0])
                return
            self.dir_obj_phrase = words

    def neutralize_verb(self):
        if self.verb not in CMDS and self.verb != "start":
            self.initialize()
            return

        for word, arr in CHART.items():
            if self.verb in arr:
                self.verb = word
                break

    def get_parts(self) -> Dict[str, Union[str, List[str]]]:
        return {
            "verb": self.verb,
            "direct_obj": self.dir_obj_phrase,
            "preposition": self.preposition,
            "obj_of_prep": self.obj_of_p_phrase,
        }

    def __str__(self) -> str:
        return f"{self.verb} {' '.join(self.dir_obj_phrase)} {self.preposition} {' '.join(self.obj_of_p_phrase)}".strip()
