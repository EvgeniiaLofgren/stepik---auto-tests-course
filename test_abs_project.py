#Here is a test, can run from terminal

# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     print("All tests passed!")

#Here are a few tests, can run from terminal

# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     test_abs2()
#     print("Everything passed")

#Here are the tests using unittest framework
#Need to import unittest in the file
#Need to create class inherited from TestCase: class TestAbs(unittest.TestCase)
#Need to make all test functions into methods adding self:  def test_abs1(self):
#Need to change assert to self.assertEqual()
#need to change test launch string to unittest.main()

import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()