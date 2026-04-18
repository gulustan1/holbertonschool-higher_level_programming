#!/usr/bin/python3
"""Faylı oxuyan və çap edən modul"""


def read_file(filename=""):
    """UTF8 formatlı faylı oxuyur və stdout-a çap edir"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
