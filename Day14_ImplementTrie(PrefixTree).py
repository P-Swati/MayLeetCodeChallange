class TrieNode:
    def __init__(self,data=None):
        self.children=[None]*26 # 26 child pointers
        self.endOfWord=False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root= TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp=self.root
        
        for char in word:
            # if the index corresponding to value of char is None, then this char is not present
            if(not temp.children[ord(char)-ord('a')]):
                temp.children[ord(char)-ord('a')]=TrieNode()
            
            # move to new location in trie
            temp=temp.children[ord(char)-ord('a')]
            
        #after the word has been traversed , mark the last trie node as endofword
        temp.endOfWord=True
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp=self.root
        
        for char in word:
            if(not temp.children[ord(char)-ord('a')]):
                return False
            temp=temp.children[ord(char)-ord('a')]
            
        if(temp and temp.endOfWord==True):
            return True
        
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp=self.root
        for char in prefix:
            index=ord(char)-ord('a')
            
            if(not temp.children[index]):
                return False
            temp=temp.children[index]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
