#!/usr/bin/python3
"""Serialization və Deserialization dəstəkləyən Student klası"""


class Student:
    """Tələbə məlumatlarını saxlayan, filtrləyən və bərpa edən klas"""

    def __init__(self, first_name, last_name, age):
        """Student instansiyasını başladır"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Student obyektinin lüğət təsvirini qaytarır"""
        if (isinstance(attrs, list) and
                all(isinstance(s, str) for s in attrs)):
            res = {}
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """Lüğətdəki bütün atributları Student obyektinə yükləyir"""
        for key, value in json.items():
            setattr(self, key, value)
