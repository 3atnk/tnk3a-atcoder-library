@tuple
class GaisekiKey:
    x: int
    y: int

    def __lt__(self, other):
        return self.x * other.y - self.y * other.x > 0

sorted1 = sorted(lst1, key=lambda p: GaisekiKey(p[0], p[1]))
sorted2 = sorted(lst2, key=lambda p: GaisekiKey(p[0], p[1]))
