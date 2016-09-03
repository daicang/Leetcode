class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        def _dir(name):
            return '.' not in name

        lpath = 0
        dirs = []

        for path in input.split('\n'):
            nr_dir = 0
            while nr_dir < len(dirs) and path[nr_dir] == '\t':
                nr_dir += 1
            real_path = path[nr_dir:]
            dirs = dirs[:nr_dir]

            if _dir(path):
                dirs.append(len(real_path))
            else:
                path_len = len(real_path) + nr_dir + sum(dirs)
                lpath = path_len if path_len > lpath else lpath

        return lpath

s = Solution()
print s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
print s.lengthLongestPath("dir\n    file.txt")
print s.lengthLongestPath("dir\n        file.txt")
print s.lengthLongestPath("a\n\tb1\n\t\tf1.txt\n\taaaaa\n\t\tf2.txt")
