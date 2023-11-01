#!/usr/bin/python3
"""LockedClass classe"""


class LockedClass:
    """prevents the user from dynamically creating new instance attribute"""
    __slots__ = ["first_name"]
