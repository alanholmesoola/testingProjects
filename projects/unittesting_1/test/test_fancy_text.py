from app.fancyText import FancyText

import unittest

class TestFancyText(unittest.TestCase):

    def test_upper_and_lower_case_a_uppercase_word(self):
        # Arrange
        fancy = FancyText()
        test_data = "david"
        expected_result = "DaViD"
        
        # Act
        observed = fancy.mixed_case(test_data)
        
        # Assert
        self.assertEqual(observed, expected_result)
