#!/usr/bin/env python3
"""This module implements personal data security"""
import logging
import re
from typing import List, Tuple


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = record.getMessage()
        record.msg = filter_datum(self.fields,
                                  self.REDACTION, message, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """This function returns the log message obfuscated"""
    for field in fields:
        pattern = f"{field}=.*?{separator}"
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)
    return message
