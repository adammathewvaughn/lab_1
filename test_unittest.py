import count_e_in_string
import length_of_string
import concat_elements_in_list
import reverse_string
import extract_from_list
import lab_1
import unittest

class CountEInString(unittest.TestCase):
    def test_count_e_in_string(self):
        self.assertEqual(lab_1.count_e_in_string(int), 1)


if __name__ == "__main__":
    unittest.main()

class LengthOfString(unittest.TestCase):
    def test_length_of_string(self):
        self.assertEqual(length_of_string.length_of_string(int), 26)


if __name__ == "__main__":
    unittest.main()


class ConcatElementsInList(unittest.TestCase):
    def test_concat_elements_in_list(self):
        self.assertEqual(lab_1.concat_elements_in_list(str), "Hello, everyone out there!")
        
        
if __name__ == "__main__":
    unittest.main()


class ReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string.reverse_string("Hello Everyone"), ("!enoyrevE olleH"))


if __name__ == "__main__":
    unittest.main()


class ExtractFromList(unittest.TestCase):
    def test_extract_from_list(self):
        self.assertEqual(extract_from_list([]), [3, 3, 6])


if __name__ == "__main__":
    unittest.main()