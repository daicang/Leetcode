class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        # print(self.nums)
        low = 0
        high = len(self.nums)-1
        while low <= high:
            mid = (low+high) // 2
            if self.nums[mid] == number:
                low = high = mid
                break
            elif self.nums[mid] < number:
                low = mid + 1
            else:  # nums[mid] > number
                high = mid
                if low == high:
                    break
        self.nums.insert(low, number)


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        # print(self.nums)
        low = 0
        high = len(self.nums)-1
        while low < high:
            s = self.nums[low] + self.nums[high]
            if s == value:
                return True
            if s > value:
                high -= 1
            else:
                low += 1
        return False

ts = TwoSum()

for i in [1, 3, 5]:
    ts.add(i)
for i in [4, 7]:
    print(ts.find(i))

ts = TwoSum()

for i in [0, 0]:
    ts.add(i)
for i in [0,]:
    print(ts.find(i))


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)