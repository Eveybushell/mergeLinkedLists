class HealthNode:
    def __init__(self, ssn, age=18, fullName="Jane Doe"):
        self.ssn = ssn
        self.age = age
        self.fullName = fullName
        self.next = None

def mergeRecords(head1, head2):
    dummy = HealthNode(ssn=-1)
    current = dummy

    while head1 and head2:
        if head1.ssn <= head2.ssn:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    
    if head1:
        current.next = head1
    elif head2:
        current.next = head2
    
    return dummy.next