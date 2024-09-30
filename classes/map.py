class Map:
    map_data = []

    def __init__(self, w, h, map_data):
        self.w = w
        self.h = h
        Map.map_data = map_data

    def get_dimensions(self):
        return (self.w, self.h)
        