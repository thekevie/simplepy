"""
simplepy package
"""

__author__ = 'thekevie'
__license__ = 'MIT'
__version__ = '1.0.7'
__description__ = 'A python package that can do math and have games'

from .games import *
from .percent import *
from .convert import * 
from .get import *

in_percent = percent.in_percent
get_type = get.get_type