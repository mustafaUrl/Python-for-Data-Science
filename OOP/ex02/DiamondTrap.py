from S1E7 import Baratheon, Lannister
class King(Baratheon, Lannister):
    """King class"""

    def __init__(self, first_name):
        return super().__init__(first_name)
    def set_eyes(self, eyes):
        self.eyes = eyes

    def set_hairs(self, hairs):
        self.hairs = hairs

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs