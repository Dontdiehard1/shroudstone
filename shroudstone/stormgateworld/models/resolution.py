# coding: utf-8

"""
    api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Resolution(str, Enum):
    """
    Resolution
    """

    """
    allowed enum values
    """
    MINUTE = 'minute'
    HOUR = 'hour'
    DAY = 'day'
    WEEK = 'week'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Resolution from a JSON string"""
        return cls(json.loads(json_str))

