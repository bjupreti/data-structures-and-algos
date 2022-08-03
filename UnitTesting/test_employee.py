import unittest
from unittest.mock import patch

from employee import Employee

class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Runs before_all tests"""
        print('setupClass')
        
    @classmethod
    def tearDownClass(cls):
        """Runs after_all tests"""
        print('tearDownClass')
        
    def setUp(self):
        """Runs before each test"""
        print('setUp')
        self.emp_1 = Employee('Bijay', 'Upreti', 50000)
        self.emp_2 = Employee('Bibek', 'Upreti', 100000)
        
    def tearDown(self):
        """Runs after each test"""
        print('tearDown')
    
    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Bijay.Upreti@email.com')
        self.assertEqual(self.emp_2.email, 'Bibek.Upreti@email.com')
        
        self.emp_1.fname = 'Pratima'
        
        self.assertEqual(self.emp_1.email, 'Pratima.Upreti@email.com')
    
    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, 'Bijay Upreti')
        self.assertEqual(self.emp_2.fullname, 'Bibek Upreti')
        
        self.emp_1.fname = 'Pratima'
        self.assertEqual(self.emp_1.fullname, 'Pratima Upreti')
        
    
    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
    
    def test_monthly_schedule(self):
        print('test_monthly_schedule')
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Upreti/May')
            self.assertEqual(schedule, 'Success')
            
            mocked_get.return_value.ok = False
            
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Upreti/June')
            self.assertEqual(schedule, 'Bad Response!')
        
        
if __name__ == '__main__':
    unittest.main()
    
    