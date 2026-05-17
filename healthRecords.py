class HealthNode:
    def __init__(self, ssn, age = 18, fullName = "Jane Doe"):
        self. ssn = ssn
        self.age = age
        self.fullName = fullName
        self.next = None
    
def mergeRecords(headA: HealthNode , headB: HealthNode):
    dummy = HealthNode(ssn=1)
    current = dummy

    while headA and headB:
        if headA.ssn <= headB.ssn:
            current.next = headA
            headA = headA.next
        else:
            current.next = headB
            headB = headB.next
        current = current.next
    
    if headA:
        current.next = headA
    elif headB:
        current.next = headB
    
    return dummy.next


