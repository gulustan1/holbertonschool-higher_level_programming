#!/usr/bin/python3
"""Paskal üçbucağı modulu"""


def pascal_triangle(n):
    """n ölçülü Paskal üçbucağını qaytaran funksiya"""
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        # Yeni sətrin başlanğıcı həmişə 1-dir
        current_row = [1]

        # Aradakı elementləri hesabla
        for i in range(len(prev_row) - 1):
            current_row.append(prev_row[i] + prev_row[i + 1])

        # Yeni sətrin sonuna 1 əlavə et
        current_row.append(1)
        
        triangle.append(current_row)

    return triangle
