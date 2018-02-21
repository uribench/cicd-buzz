# test_generator.py
#
# This is not the original example code from https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b
# It was modified by Uri to better match the recommended way of using 'unittest' framework as follows:
#   1. Added a class wrapping all the method
#   2. The class is derived from 'unittest.TestCase' class
#   3. Asserts were changed (originally, only plain assert statements of 'pytest' framework were used)

import unittest
from buzz import generator

class PrimesTestCase(unittest.TestCase):
    """Tests for `generator.py`"""

    def test_sample_single_word(self):
        l = ('foo', 'bar', 'foobar')
        word = generator.sample(l)
        self.assertTrue(word in l)

    def test_sample_multiple_words(self):
        l = ('foo', 'bar', 'foobar')
        words = generator.sample(l, 2)
        self.assertTrue(len(words) == 2)
        self.assertTrue(words[0] in l)
        self.assertTrue(words[1] in l)
        self.assertFalse(words[0] is words[1])

    def test_generate_buzz_of_at_least_five_words(self):
        phrase = generator.generate_buzz()
        self.assertTrue(len(phrase.split()) >= 5)

if __name__ == '__main__':
    unittest.main()
