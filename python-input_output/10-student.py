#!/usr/bin/python3
"""Filtrləmə imkanı olan Student klası"""


class Student:
    """Tələbə məlumatlarını saxlayan və filtrləyən klas"""

    def __init__(self, first_name, last_name, age):
        """Student instansiyasını başladır"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Student obyektinin lüğət təsvirini (seçilmiş atributlarla) qaytarır"""
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            res = {}
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res
        return self.__dict__
