#!/usr/bin/python3
"""Faylın sonuna mətn əlavə edən modul"""


def append_write(filename="", text=""):
    """UTF8 formatında faylın sonuna mətn əlavə edir və simvol sayını qaytarır"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
