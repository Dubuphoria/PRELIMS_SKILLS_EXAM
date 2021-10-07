from part2_temp import Temperature
import unittest

print(Temperature) # checked if the part2_temp.py is imported inside unittest_kelvin.py

# Creating a class for unittesting

class Kelvin_Test(unittest.TestCase):
    def test_celsius(self): # unittesting for celsius
        self.assertEqual(Temperature(celsius=17).kelvin,290.15)

    def test_fahrenheit(self): # unittesting for fahrenheit
        self.assertEqual(Temperature(fahrenheit=17).kelvin,264.816666667)

    def test_kelvin(self): # unittesting for kelvin
        self.assertEqual(Temperature(kelvin=17).kelvin,17)

    def test_noArg(self): #unittesting for negative valued kelvin
        self.assertEqual(Temperature(kelvin=-1).kelvin,-1)

if __name__ == '__main__':
    unittest.main()