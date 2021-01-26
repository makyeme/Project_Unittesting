import unittest
import add_func

class TestAdd(unittest.TestCase):
    
    """looping through the given integer range & asserting that given arguments,
    will generate a corresponding outcome
    """
    
    
    def test_add(self):
        for i in range(1, 201):
            with self.subTest(i = i):
                
                self.assertEqual(add_func.add(i, i, i), add_func.output[i+i+i])
        