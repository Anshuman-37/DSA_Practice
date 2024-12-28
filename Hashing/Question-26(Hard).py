# Question 26: Implement a Trie using hash maps for children.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

trie = Trie()
trie.insert("apple")
print(f"Search 'apple': {trie.search('apple')}")
print(f"Search 'app': {trie.search('app')}")
print(f"StartsWith 'app': {trie.startsWith('app')}") 

trie.insert("app")
print(f"Search 'app': {trie.search('app')}")

print(f"Search 'banana': {trie.search('banana')}")
print(f"StartsWith 'appl': {trie.startsWith('appl')}")
print(f"StartsWith 'b': {trie.startsWith('b')}")

# Edge cases
print(f"StartsWith '': {trie.startsWith('')}")

trie2 = Trie()
trie2.insert("")
print(f"Search '': {trie2.search('')}")
print(f"StartsWith '': {trie2.startsWith('')}")