#!/usr/bin/python3
"""JSON string-ini Python obyektinə çevirən modul"""
import json


def from_json_string(my_str):
    """JSON mətni tərəfindən təmsil olunan Python obyektini qaytarır"""
    return json.loads(my_str)
