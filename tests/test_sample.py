import os.path
import sys

sys.path.append(os.path.dirname(__file__) + '/..')

import pytest
from utilities.testbase import TestBase

class TestSample(TestBase):

    def test_sample(self):
        print("Test Executed")