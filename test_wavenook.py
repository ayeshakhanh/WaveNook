# test_wavenook.py
"""
Tests for WaveNook module.
"""

import unittest
from wavenook import WaveNook

class TestWaveNook(unittest.TestCase):
    """Test cases for WaveNook class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WaveNook()
        self.assertIsInstance(instance, WaveNook)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WaveNook()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
