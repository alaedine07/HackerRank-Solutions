class Solution(object):

    def check_distinct(self, s):
        return len(set(s)) == len(s)

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = start = 0
        used_char = {}

        for i, char in enumerate(s):
            if char in used_char and start <= used_char[char]:
                start = used_char[char] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used_char[char] = i
        return max_length

def main():
    solution = Solution()
    input_string = "pwwkew"
    result = solution.lengthOfLongestSubstring(input_string)
    print(result)

if __name__ == "__main__":
    main()
