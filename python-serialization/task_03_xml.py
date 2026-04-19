#!/usr/bin/env python3
"""XML formatında serializasiya və deserializasiya modulu"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Python lüğətini XML faylına çevirir və yadda saxlayır"""
    # Kök elementi yaradırıq <data>
    root = ET.Element("data")

    # Lüğətin elementlərini alt teqlər kimi əlavə edirik
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML daxilində bütün dəyərlər string olmalıdır

    # XML ağacını yaradırıq və fayla yazırıq
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """XML faylından məlumatları oxuyur və lüğətə çevirir"""
    try:
        # Faylı parse edirik (təhlil edirik)
        tree = ET.parse(filename)
        root = tree.getroot()

        # Elementləri lüğətə yığırıq
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict

    except FileNotFoundError:
        return None
    except Exception:
        return None
