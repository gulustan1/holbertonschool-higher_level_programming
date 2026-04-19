#!/usr/bin/python3
"""Obyekti JSON formatında fayla yazan modul"""
import json


def save_to_json_file(my_obj, filename):
    """Python obyektini JSON təmsili ilə fayla qeyd edir"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
