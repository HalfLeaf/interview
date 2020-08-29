#-*-coding:utf-8-*-

from typing import List,Dict
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        lines = defaultdict(list)
        result = ["JFK", ]
        for x in tickets:
            lines[x[0]].append(x[1])
        self.get_next_line(lines, "JFK", result)
        return result


    def get_next_line(self, lines:Dict[str, List[str]], line:str, result:List[str]) -> List[str]:
        locations = lines.get(line, [])
        locations = sorted(locations)
        for l in locations:
            if l not in result:
                continue
            result.append(l)
            if lines.get(l, []):
                self.get_next_line(lines, l, result)




if __name__ == '__main__':
    s = Solution()
    print(s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]] ))