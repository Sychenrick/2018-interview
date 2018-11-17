class Trie(object):
    class Node(object):
        def __init__(self):
            self.isleaf = False
            self.childs = [None for _ in range(26)]
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def charindex(self, char):
        return ord(char) - ord('a')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.insertWord(word, self.root)

    def insertWord(self, word, root):
        if not root:
            return False
        if len(word) == 0:
            root.isleaf = True
            return
        index = self.charindex(word[0])
        if root.childs[index] is None:
            root.childs[index] = self.Node()
        self.insertWord(word[1:], root.childs[index])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.searchWord(word, self.root)

    def searchWord(self, word, root):
        if not root:
            return False
        if len(word) == 0:
            return root.isleaf
        index = self.charindex(word[0])
        return self.searchWord(word[1:], root.childs[index])

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.startWord(prefix, self.root)

    def startWord(self, prefix, root):
        if not root:
            return False
        if len(prefix) == 0:
            return True
        index = self.charindex(prefix[0])
        return self.startWord(prefix[1:], root.childs[index])


class MapSum(object):
    class Node(object):
        def __init__(self):
            self.val = 0
            self.childs = [None for _ in range(26)]
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def charindex(self, char):
        return ord(char) - ord('a')

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.insertWord(key,self.root,val)
    def insertWord(self, word, root,val):
        if not root:
            return False
        if len(word) == 0:
            root.val = val
            return
        index = self.charindex(word[0])
        if root.childs[index] is None:
            root.childs[index] = self.Node()
        self.insertWord(word[1:], root.childs[index],val)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.countsum(prefix,self.root)
    def countsum(self,prefix,root):
        if not root:
            return False
        if len(prefix) != 0:
            index = self.charindex(prefix[0])
            return self.countsum(prefix[1:],root.childs[index])
        allsum = root.val
        for child in root.childs:
            allsum += self.countsum(prefix,child)
        return allsum


def binarySearch(nums,a):
    i = 0
    j = len(nums)
    while i <= j:
        print i,j
        mid = (i+j) /2
        temp = nums[mid]
        if temp == a:
            return mid
        elif temp > a:
            j = mid - 1
        else:
            i = mid + 1
    return i

print binarySearch([1,2,3,5,8],3.5)