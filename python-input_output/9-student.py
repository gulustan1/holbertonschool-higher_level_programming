#!/usr/bin/python3
"""Student klasını təyin edən modul"""


class Student:
    """Tələbə məlumatlarını saxlayan klas"""

    def __init__(self, first_name, last_name, age):
        """Student instansiyasını başladır"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Student obyektinin lüğət təsvirini qaytarır"""
        return self.__dict__
