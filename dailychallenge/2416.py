from typing import List

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()

        for word in words:
            #print(word[:i])
            trie.insert(word)
        
        scores = []
        for word in words:
            scores.append(trie.get_score(word))
        
        return scores
        

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.hit = 0
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
            node.hit += 1
    
    def search(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return -1
            node = node.children[char]
        return node.hit

    def get_score(self, word: str) -> int:
        node = self.root
        score = 0
        for char in word:
            node = node.children[char]
            score += node.hit
        
        return score
    
    def starts_with(self, prefix: str) -> None:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True