from simple import *
import unittest

class TestAdd(unittest.TestCase):
  def test_twothree(self):
    self.assertEqual(add(2,3), 5)
