# test_dialogblaze.py
"""
Tests for DialogBlaze module.
"""

import unittest
from dialogblaze import DialogBlaze

class TestDialogBlaze(unittest.TestCase):
    """Test cases for DialogBlaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DialogBlaze()
        self.assertIsInstance(instance, DialogBlaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DialogBlaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
