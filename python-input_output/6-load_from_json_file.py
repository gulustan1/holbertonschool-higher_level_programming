#!/usr/bin/python3
"""JSON faylından obyekti yükləyən modul"""
import json


def load_from_json_file(filename):
    """JSON faylından Python obyekti yaradır"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
