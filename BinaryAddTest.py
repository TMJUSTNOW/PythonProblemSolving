import BinaryAdd
import unittest

class BinaryAddTest(unittest.TestCase):

  def testBinary(self):
    self.assertEquals("0", BinaryAdd.add_binary("0", "0"))
    self.assertEquals("1", BinaryAdd.add_binary("0", "1"))
    self.assertEquals("1", BinaryAdd.add_binary("1", "0"))
    self.assertEquals("11", BinaryAdd.add_binary("10", "1"))

  def testCarry(self):
    self.assertEquals("101", BinaryAdd.add_binary("11", "10"))
    self.assertEquals("110", BinaryAdd.add_binary("11", "11"))

  def testLong(self):
    self.assertEquals(
        "11111111111111",
        BinaryAdd.add_binary("1111111111111", "10000000000000"))

if __name__ == "__main__":
  unittest.main()