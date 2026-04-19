#!/usr/bin/env python3
"""Təməl JSON serializasiya modulu"""
import json


def serialize_and_save_to_file(data, filename):
    """Python lüğətini JSON formatında fayla yazır"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """JSON faylından məlumatı oxuyub Python lüğətinə çevirir"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
