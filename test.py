import unittest
from healthRecords import HealthNode, mergeRecords

class MergeTest (unittest.TestCase):

    def linkify(self, list):
        if not list:
            return None
        link = HealthNode(list[0])
        current = link
        for value in list[1:]:
            current.next = HealthNode(value)
            current = current.next
        return link
    
    def listify(self, link):
        array = []
        current = link
        while current:
            array.append(current.ssn)
            current = current.next
        return array
    
    def testBasic1(self):
        list1 = self.linkify([1,3,5])
        list2 = self.linkify([2,4,6])
        merged = mergeRecords(list1, list2)
        self.assertEqual(self.listify(merged), [1,2,3,4,5,6])
    
    def testBasic2(self):
        list1 = self.linkify([1,3,5])
        list2 = self.linkify([1,4,6])
        merged = mergeRecords(list1, list2)
        self.assertEqual(self.listify(merged), [1,1,3,4,5,6])
    
    def testBasic3(self):
        list1 = self.linkify([1,3,5,7,8,10])
        list2 = self.linkify([1,4,6])
        merged = mergeRecords(list1, list2)
        self.assertEqual(self.listify(merged), [1,1,3,4,5,6,7,8,10])
    
    def testOneEmpty(self):
        list1 = self.linkify([1,2,5,8])
        list2 = self.linkify([])
        merged = mergeRecords(list1, list2)
        self.assertEqual(self.listify(merged), [1,2,5,8])
    
    def testAllDupes(self):
        list1 = self.linkify([1,2,3])
        list2 = self.linkify([1,2,3])
        merged = mergeRecords(list1, list2)
        self.assertEqual(self.listify(merged), [1,1,2,2,3,3])
    
    def testEmpty(self):
        list1 = self.linkify([])
        list2 = self.linkify([])
        merged = mergeRecords(list1, list2)
        self.assertEqual(self.listify(merged), [])
if __name__ == "__main__":
    unittest.main()