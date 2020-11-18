import unittest
from MyStringBuilder import MyStringBuilder

class MyStringBuilderTests(unittest.TestCase):

    def test_when_append_one_time_then_ToString_returns_the_text(self):
        sut = MyStringBuilder()
        sut.Append("Initial sentence..")
        self.assertEqual("Initial sentence..", sut.ToString())

    def test_when_append_two_times_then_ToString_returns_the_text(self):
        sut = MyStringBuilder()
        sut.Append("Initial sentence..")
        sut.Append("..and here a 2nd sentence!")
        self.assertEqual("Initial sentence....and here a 2nd sentence!", sut.ToString())

if __name__ == '__main__':
    unittest.main()


