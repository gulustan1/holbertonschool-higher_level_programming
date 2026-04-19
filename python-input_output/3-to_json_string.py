#!/usr/bin/python3
"""Obyekti JSON string-inə çevirən modul"""
import json


def to_json_string(my_obj):
    """Obyektin JSON təmsilini (string) geri qaytarır"""
    return json.dumps(my_obj)
