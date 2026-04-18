#!/usr/bin/python3
"""Fayla mətn yazan modul"""


def write_file(filename="", text=""):
    """UTF8 formatında fayla mətn yazır və simvol sayını qaytarır"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
