# mergeLinkedLists

## Questions
1. If we are keeping duplicate information, does it matter what order they are kept?
2. If we receive an empty list, should we still merge with just one list
3. If both lists are empty, should we return an empty list as well

## Complexity
Time complexity is O(n). We are navigating each node of both lists once.
Space complexity is O(1). We are adding a single node and building a list, but doing so by manipulation of next pointers rather than constructing a new list of whole cloth

