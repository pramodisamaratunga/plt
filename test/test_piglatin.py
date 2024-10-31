import unittest
from tensorflow.python.ops.check_ops import assert_equal
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def getStringPhrase(self):
        translator = PigLatin("hello world")
        assert translator.get_phrase() == "hello world"

    def testGetPhrase(self):
        pass
