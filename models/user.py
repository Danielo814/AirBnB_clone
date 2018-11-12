#!/usr/bin/python
"""A class User that inherits from BaseModel"""

from model.BaseModel import base_model

class User(BaseModel):
    """Represents a class User
    """

    def __init__(self):
        """User Instantiation
        """

        email = ''
        password = ''
        first_name = ''
        last_name = ''
