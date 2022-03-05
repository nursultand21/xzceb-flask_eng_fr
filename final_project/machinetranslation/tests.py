import unittest
from translator import english_to_french
from translator import french_to_english

class TestEnglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french(0), 0) # test for null input.
        self.assertNotEqual(english_to_french('None'), '') # test for null input.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertEqual(english_to_french('How are you?'), 'Comment es-tu?')  # test when 'How are you?' is given as input the output is 'Comment es-tu?'.

class TestFrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english(0), 0) # test for null input.
        self.assertNotEqual(french_to_english(0), 0) # test for null input.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.
        self.assertEqual(french_to_english('Comment es-tu?'), 'How are you?') # test when 'Comment es-tu?' is given as input the output is 'How are you?'.

unittest.main()
