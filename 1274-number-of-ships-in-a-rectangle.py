# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
   def hasShips(self, topRight, bottomLeft):
       """
       :type topRight: Point
		 :type bottomLeft: Point
       :rtype bool
       """
       return True

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        q = [(bottomLeft, topRight)]
        count = 0

        while q:
            p1, p2 = q.pop()
            if sea.hasShips(p2, p1):
                if p1.x == p2.x and p1.y == p2.y:
                    count += 1

                elif p1.x < p2.x:
                    x_mid = (p1.x + p2.x) / 2
                    q.append((p1, Point(x_mid, p2.y)))
                    q.append((Point(x_mid+1, p1.y), p2))

                else:
                    # p1.x == p2.x and p1.y < p2.y
                    y_mid = (p1.y + p2.y) / 2
                    q.append((p1, Point(p1.x, y_mid)))
                    q.append((Point(p1.x, y_mid+1), p2))

        return count



