from ast import Str
import count_e_in_string
import length_of_string
import concat_elements_in_list
import reverse_string
import extract_from_list
import unittest

class CountEInString(unittest.TestCase):
    def test_count_e_in_string(self):
        self.assertEqual(count_e_in_string.count_e_in_string("E"), 1)


if __name__ == "__main__":
    unittest.main()

class LengthOfString(unittest.TestCase):
    def test_length_of_string(self):
        self.assertEqual(length_of_string.length_of_string("Hello, everyone out there!"), 26)


if __name__ == "__main__":
    unittest.main()


class ConcatElementsInList(unittest.TestCase):
    def test_concat_elements_in_list(self):
        self.assertEqual(concat_elements_in_list.concat_elements_in_list("Hello,", "everyone", "out", "there!"), "Hello, everyone out there!")
    
if __name__ == "__main__":
    unittest.main()


class ReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string.reverse_string("Hello Everyone!"), "!enoyrevE olleH")


if __name__ == "__main__":
    unittest.main()


class ExtractFromList(unittest.TestCase):
    def test_extract_from_list(self):
        self.assertEqual(extract_from_list.extract_from_list([]), [3, 3, 6])


if __name__ == "__main__":
    unittest.main()