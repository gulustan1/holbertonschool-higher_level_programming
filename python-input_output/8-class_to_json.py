#!/usr/bin/python3
"""Class-dan JSON lüğətinə çevirmə modulu"""


def class_to_json(obj):
    """Obyektin atributlarının lüğət təsvirini qaytarır"""
    return obj.__dict__
