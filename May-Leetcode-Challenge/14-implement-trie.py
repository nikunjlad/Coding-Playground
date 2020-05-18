"""
Implement a trie with insert, search, and startsWith methods.
Example:
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

"""


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        w = self.trie

        for char in word:
            if char not in w:
                w[char] = {}

            w = w[char]

        w['@'] = "done"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        w = self.trie

        for char in word:
            if char not in w:
                return False
            else:
                w = w[char]

        if '@' not in w:
            return False
        else:
            return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        w = self.trie

        for char in prefix:
            if char not in w:
                return False
            else:
                w = w[char]

        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
