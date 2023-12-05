class Solution(object):

    def check_distinct(self, s):
        return len(set(s)) == len(s)

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        subStrDict = {}
        spliter = 2
        i = 0
        while (len(s[i::]) > spliter):
            subString = s[i:spliter]
            if (self.check_distinct(subString)):
                spliter += 1
            else:
                subString = subString[:-1]
                subStrDict[subString] = len(subString)
                i += 1
        return subStrDict
