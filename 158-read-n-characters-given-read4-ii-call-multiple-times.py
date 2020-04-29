"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.last_read_buf = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if n <= len(self.last_read_buf):
            for i in range(n):
                buf[i] = self.last_read_buf[i]
            self.last_read_buf = self.last_read_buf[n:]
            return n

        # n > len(last-read-buf)
        read_count = 0
        i = 0
        if self.last_read_buf:
            for i in range(len(self.last_read_buf)):
                buf[i] = self.last_read_buf[i]
                read_count += 1
                n -= 1
            self.last_read_buf = []
            i += 1

        read4_buf = [None] * 4
        while n > 0:
            read = read4(read4_buf)
            if read == 0:
                break

            for j in range(min(read, n)):
                buf[i] = read4_buf[j]
                i += 1

            if n < read:
                self.last_read_buf = read4_buf[n:read]

            read_count += min(read, n)
            n -= read

        return read_count

