from math import ceil
class Solution:
    def cover ( a_length : int,a_width : int, b_length : int)-> int:
        """
        Calculate the minimum number of flagstones required to cover a rectangular area.

        Parameters:
        a_length (int): The length of the rectangular area (n).
        a_width (int): The width of the rectangular area (m).

        Returns:
            int: number of flagstones needs.
        """
        result = ceil(a_length/b_length) * ceil(a_width/b_length)
        return result

def main():
    
    inputs :list[int] = list(map(int,input().split(" ")))
    result :int = Solution.cover(*inputs)
    print(result)
    
if __name__ == '__main__':
    main()
