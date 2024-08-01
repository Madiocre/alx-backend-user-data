#!/usr/bin/env python3
"""
Logger Filtering Function
"""
import re
import logging


def filter_datum(fields, redaction, message, separator):
    """ 
    Filtering the Logger 
    
    Args:
    fields: fields to be redacted
    redaction: what to put in place of redacted fields
    message: a string representing the log line
    separator: a string representing by which character is separating
    """
    for field in fields:
        regex = rf"{field}=(.*?)(?={separator}|$)"
        message = re.sub(regex, f"{field}={redaction}", message)
    return message