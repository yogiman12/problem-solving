class Solution:
    def __init__(self) -> None:
        """
        Initialize the Solution class and define the vowels to be removed.
        """
        self.vowels = ("a", "e", "i", "o", "u", "y")
    
    def string_task(self, word: str) -> str:
        """
        Process the input string by:
        1. Converting all characters to lowercase.
        2. Removing all vowels (a, e, i, o, u, y).
        3. Adding a '.' before each consonant.

        Parameters:
        word (str): The input string consisting of uppercase and lowercase Latin letters.

        Returns:
        str: The processed string after removing vowels, adding a '.', and converting to lowercase.
        """
        result = ""
        for letter in word.lower():
            if letter in self.vowels:
                pass
            else:
                result += f".{letter}"
        return result    

def main():
    word: str = input()
    result: str = Solution().string_task(word)
    print(result)
    
if __name__ == '__main__':
    main()
