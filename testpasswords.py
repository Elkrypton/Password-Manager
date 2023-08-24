from password_manager import *
import unittest

class TestPasswordManager(unittest.TestCase):
    
    def __init__(self, website, email, password):
        self.instance = TestPasswordManager(website, email, password)
        self.instance.generate_key()
    

    def TestKeyGeneration(self):
        return self.assertTrue(self.instance.generate_key())
    
    def TestEncode(self):
        return self.instance.Encode()
    
    def testDecode(self):
        return self.instance.Decode()
    
    def testSaveFile(self):
        self.instance.save_to_file()
if __name__ == "__main__":
    unittest.main()       