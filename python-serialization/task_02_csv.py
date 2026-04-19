#!/usr/bin/env python3
"""CSV məlumatlarını JSON formatına çevirən modul"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    CSV faylını oxuyur və məlumatları data.json faylına yazır.
    
    Args:
        csv_filename (str): Oxunacaq CSV faylının adı.
        
    Returns:
        bool: Uğurlu olarsa True, xəta baş verərsə False.
    """
    try:
        data = []
        # 1. CSV faylını oxu və DictReader ilə lüğətlərə çevir
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)
        
        # 2. Siyahını JSON formatında data.json-a yaz
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
            
        return True
        
    except FileNotFoundError:
        # Fayl tapılmadıqda False qaytar
        return False
    except Exception:
        # Digər gözlənilməz xətalar zamanı False qaytar
        return False
