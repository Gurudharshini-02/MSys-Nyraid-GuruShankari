import unittest
import File_Transfer1

class TestFileTrasfer(unittest.TestCase):
    def testfile(self):
        hostname='127.0.1.1'
        username='guru'
        password='kiruthiga'
        res=File_Transfer1.file_transfer(hostname,username,password)
        self.assertEqual(res,"File Copied")
        
        
if __name__ == "__main__":
    unittest.main()
