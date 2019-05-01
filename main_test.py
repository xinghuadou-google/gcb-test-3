import unittest

from main import hello


class TestMain(unittest.TestCase):

  def test_hello(self):
    self.assertEqual(hello(None), 'Hello world!!!')


if __name__ == '__main__':
  unittest.main()
