from app.fancyText import FancyText

import unittest

class TestFancyText(unittest.TestCase):

    #Positive Cases

    def test_upper_and_lower_case_a_uppercase_word(self):
        # Arrange
        fancy = FancyText()
        test_data = "DAVID"
        expected_result = "DaViD"
        
        # Act
        observed = fancy.mixed_case(test_data)
        
        # Assert
        self.assertEqual(observed, expected_result)


    def test_upper_and_lower_case_a_sentence(self):
        #Arrange
        fancy = FancyText()
        test_data = "alan sure is great"
        expected_result = "AlAn sUrE Is gReAt"

        #Act
        observed = fancy.mixed_case(test_data)

        #Assert
        self.assertEqual(observed,expected_result)

    def test_special_characters(self):
        #Arrange
        fancy = FancyText()
        test_data = "!@£$%^&*()"
        expected_result = "!@£$%^&*()"

        #Act
        observed = fancy.mixed_case(test_data)

        #Assert
        self.assertEqual(observed,expected_result)

    
#Negative Cases
    def test_needs_to_raise_exception_when_not_string(self):
        #Arrange
        fancy = FancyText()
        test_data = 12345
        expected_result = TypeError

        #Act/asset
        self.assertRaises(expected_result, fancy.mixed_case(test_data))