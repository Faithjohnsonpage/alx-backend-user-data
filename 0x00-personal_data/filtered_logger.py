#!/usr/bin/env python3
"""This module implements personal data security"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """This function returns the log message obfuscated"""
    for field in fields:
        pattern = f"{field}=.*?{separator}"
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)
    return message
