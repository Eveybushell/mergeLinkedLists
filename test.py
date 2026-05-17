import unittest
from healthRecords import HealthNode, mergeRecords

class TestMerge(unittest.TestCase):

    def linkify(self, list):
        if not list:
            return None
        head = HealthNode(list[0])
        current = head
        for value in list[1:]:
            current.next = HealthNode(value)
            current = current.next
        return head
    
    def listify(self, head=HealthNode):
        array = []
        current = head
        while current:
            array.append(current.ssn)
            current = current.next
        return array
    
    def testNoDuplicatesNoNull(self):
        link1 = self.linkify([1,3,5])
        link2 = self.linkify([2,4,6])
        merged = mergeRecords(link1, link2)
        self.assertEqual(self.listify(merged), [1,2,3,4,5,6])
    
    def testBasic2(self):
        link1 = self.linkify([1,2,5])
        link2 = self.linkify([3,4])
        merged = mergeRecords(link1, link2)
        self.assertEqual(self.listify(merged), [1,2,3,4,5])
    
    def testBasic3(self):
        link1 = self.linkify([1,3,6])
        link2 = self.linkify([1,2,3])
        merged = mergeRecords(link1, link2)
        self.assertEqual(self.listify(merged), [1,1,2,3,3,6])
    
    def testoneEmpty(self):
        link1 = self.linkify([1,2,3])
        link2 = self.linkify([])
        merged = mergeRecords(link1, link2)
        self.assertEqual(self.listify(merged), [1,2,3])
    
    def testBothEmpty(self):
        link1 = self.linkify([])
        link2 = self.linkify([])
        merged = mergeRecords(link1, link2)
        self.assertEqual(self.listify(merged), [])
    
    def testAllDuplicates(self):
        link1 = self.linkify([1,2,3])
        link2 = self.linkify([1,2,3])
        merged = mergeRecords(link1, link2)
        self.assertEqual(self.listify(merged), [1,1,2,2,3,3])
        
if __name__ == "__main__":
    unittest.main()
