# test_simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
  
    
    def setUp(self):
       
        self.calc = SimpleCalculator()
    
    # Test Addition
    def test_addition_positive_numbers(self):
       
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
    
    def test_addition_negative_numbers(self):
      
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-5, 10), 5)
    
    def test_addition_zero(self):
       
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_addition_decimal_numbers(self):
      
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(1.1, 2.2), 3.3)
    
    # Test Subtraction
    def test_subtraction_positive_numbers(self):
       
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 5), 5)
    
    def test_subtraction_negative_numbers(self):
        
        self.assertEqual(self.calc.subtract(-2, -3), 1)
        self.assertEqual(self.calc.subtract(-5, 10), -15)
    
    def test_subtraction_zero(self):
     
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    
    def test_subtraction_decimal_numbers(self):
     
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertEqual(self.calc.subtract(3.3, 1.1), 2.2)
    
    # Test Multiplication
    def test_multiplication_positive_numbers(self):
        
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 4), 20)
    
    def test_multiplication_negative_numbers(self):
       
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
    
    def test_multiplication_zero(self):
       
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
    
    def test_multiplication_decimal_numbers(self):
       
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(1.5, 2.5), 3.75)
    
    # Test Division
    def test_division_positive_numbers(self):
      
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        self.assertEqual(self.calc.divide(10, 2), 5.0)
    
    def test_division_negative_numbers(self):
        
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        self.assertEqual(self.calc.divide(6, -3), -2.0)
        self.assertEqual(self.calc.divide(-6, -3), 2.0)
    
    def test_division_decimal_numbers(self):
      
        self.assertEqual(self.calc.divide(5.5, 2), 2.75)
        self.assertEqual(self.calc.divide(10.0, 4.0), 2.5)
    
    def test_division_by_zero(self):
        
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
    
    def test_division_zero_by_number(self):
       
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), 0.0)
    
    def test_division_result_decimal(self):
        
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(1, 3), 1/3)

if __name__ == '__main__':
    # Run the tests
    unittest.main()