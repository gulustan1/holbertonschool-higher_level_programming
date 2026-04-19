#!/usr/bin/python3
"""
Terminal arqumentlərini Python siyahısına əlavə edən
və JSON faylında yadda saxlayan skript.
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Köhnə siyahını yükləməyə çalış, yoxdursa boş siyahı yarat
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# 2. Terminaldan gələn arqumentləri siyahıya əlavə et
# sys.argv[0] skriptin adıdır, ona görə [1:]-dən başlayırıq
items.extend(sys.argv[1:])

# 3. Yenilənmiş siyahını fayla yadda saxla
save_to_json_file(items, filename)
