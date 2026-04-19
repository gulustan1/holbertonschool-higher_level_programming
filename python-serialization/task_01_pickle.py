#!/usr/bin/env python3
"""Pickle modulu vasitəsilə obyektlərin serializasiyası"""
import pickle


class CustomObject:
    """Xüsusi atributları olan obyekt klası"""

    def __init__(self, name: str, age: int, is_student: bool):
        """Atributları başladır"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Obyektin məlumatlarını formatlı şəkildə çap edir"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Obyektin cari instansiyasını ikili fayla kopyalayır"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Fayldan obyekti oxuyur və bərpa edir"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
        except Exception:
            return None
