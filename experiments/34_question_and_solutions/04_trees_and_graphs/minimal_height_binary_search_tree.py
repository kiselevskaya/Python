# minimal_height_binary_search_tree.py

"""
Given a sorted (increasing order) array, write an algorithm to create a binary search tree with minimal height
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def min_height_bst(arr, start, end):
    if end < start:
        return
    mid = round((start+end) / 2)
    root = Node(arr[mid])
    root.left = min_height_bst(arr, start, mid-1)
    root.right = min_height_bst(arr, mid+1, end)
    return root


if __name__ == '__main__':
    array = [i for i in range(5)]
    print(array)
    print(min_height_bst(array, 0, len(array)-1).data)

