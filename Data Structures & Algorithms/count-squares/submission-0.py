class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x,y = point[0], point[1]
        self.points[(x,y)] = self.points.get((x,y),0) + 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point[0], point[1]
        result = 0

        for (x2, y2), count2 in self.points.items():
            # Skip if same point
            if x1 == x2 and y1 == y2:
                continue
            
            if abs(x2 - x1) != abs(y2-y1) or x1 == x2 or y1 == y2:
                continue
            
            count_corner1 = self.points.get((x1,y2),0)
            count_corner2 = self.points.get((x2,y1),0)


            result += count2 * count_corner1 * count_corner2
        return result