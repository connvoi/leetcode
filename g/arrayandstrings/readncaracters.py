#https://leetcode.com/explore/interview/card/google/59/array-and-strings/436/

class Solution:
    def __init__(self):
        self.chars = itertools.chain.from_iterable(iter(lambda buf=[0]*4: buf[:read4(buf)], []))
        for i in self.chars:
            print(i)
    
    def test(self, buf):
        self.chars = itertools.chain.from_iterable(iter(lambda buf=[0]*4: buf[:read4(buf)], []))
        for i in self.chars:
            print(i)
    
    def read(self, buf, n):
        return len([buf.__setitem__(*x) for x in zip(range(n), self.chars)])


class Solution(object):
    def __init__(self):
        self.buf4 = ['']*4
        self.start = 0
        self.end = 0
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while self.start < self.end and idx < n:
            buf[idx] = self.buf4[self.start]
            self.start += 1
            idx += 1
        
        if self.start == self.end:
            self.start, self.end = 0, 0

        while idx < n :
            self.end = read4(self.buf4)
            
            if self.end == 0:
                break
        
            i = 0
            while i < min(self.end, n-idx):
                buf[idx+i] = self.buf4[i]
                i += 1
            
            self.start = i
            idx += i
    
        return idx

sol= Solution()
sol.test("abc")