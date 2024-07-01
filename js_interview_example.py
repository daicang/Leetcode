
'''
input:

m = 3.28 ft
ft = 12 in
hr = 60 min
min = 60 sec

query:
2 m = ? in => 78.72
13 in = ? m => 0.33
13 in = ? hr => 'not convertible!'
'''

from typing import List
from collections import defaultdict, deque

class Converter:
    def __init__(self):
        # unit -> {unit: ratio}
        self.graph = defaultdict(dict)
        self.errs = 'not convertible'

    def parse_input_line(self, line):
        parts = line.split(' ')
        assert(len(parts) == 4)
        u1 = parts[0]
        assert parts[1] == '='
        ratio = float(parts[2])
        u2 = parts[3]
        return u1, u2, ratio

    def parse_query_line(self, line):
        parts = line.split(' ')
        assert(len(parts) == 5)
        u1 = parts[1]
        assert parts[2] == '='
        assert parts[3] == '?'
        u2 = parts[4]
        quant = float(parts[0])
        return u1, u2, quant

    def read_input(self, line):
        u1, u2, ratio = self.parse_input_line(line)
        self.graph[u1][u2] = ratio
        self.graph[u2][u1] = 1 / ratio

    def query(self, query):
        u1, target, quant = self.parse_query_line(query)
        # convert u1 to u2, mul quant
        visisted = set()
        queue = deque()
        queue.append((u1, 1))
        # bfs
        while queue:
            unit, ratio = queue.popleft()
            if unit == target:
                return ratio * quant
            if unit in visisted:
                continue
            visisted.add(unit)
            convert_table = self.graph[unit]
            for next_unit, r in convert_table.items():
                if next_unit not in visisted:
                    queue.append((next_unit, ratio * r))

        # not found
        return self.errs


c = Converter()

inputs = [
    'm = 3.28 ft',
    'ft = 12 in',
    'hr = 60 min',
    'min = 60 sec',
]

queries = [
    '2 m = ? in', # 78.72
    '13 in = ? m', # 0.33
    '13 in = ? hr', # 'not convertible!'
]

for i in inputs:
    c.read_input(i)

for q in queries:
    print(c.query(q))
