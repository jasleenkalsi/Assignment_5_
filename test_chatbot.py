"""
Description:
Author:
Date:
Usage:
"""
import unittest
from unittest.mock import patch

class ChatbotTests(unittest.TestCase): 
  pass

from chatbot import get_account 
class TestGetAccount(unittest.TestCase):
    def test_valid_account_number(self):
        # Arrange
         with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["123456"]
            # Act
            account_number = get_account()
            
            # Assert
            self.assertEqual(account_number, 123456)

    def test_non_numeric_account_number(self):
        # Arrange
         with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["non_numeric_data"]

            # Act & Assert
            with self.assertRaises(ValueError) as context:
                get_account()

            self.assertEqual(str(context.exception), "Account number must be a whole number.")

def test_non_existing_account(self):
    with patch("builtins.input") as mock_input:
        mock_input.side_effect = ["112233"]

        # Act & Assert
        with self.assertRaises(ValueError):
            get_account()

if __name__ == "__main__":
    unittest.main()
