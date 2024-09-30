from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name:str, is_alive:bool = True, family_name:str = "Baratheon", eyes:str = "brown", hairs:str = "dark"):
        super().__init__(first_name, is_alive=is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

class Lannister(Character):
    """Representing the Lannister family."""

    first_name = ""
    def __init__(self, first_name:str, is_alive:bool = True, family_name:str = "Lannister", eyes:str = "blue", hairs:str = "light"):
        super().__init__(first_name, is_alive=is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


    @staticmethod
    def create_lannister(first_name: str, is_alive: bool = True, family_name: str = "Lannister", eyes: str = "blue", hairs: str = "light"):
        """Create a Lannister character."""
        return Lannister(first_name, is_alive=is_alive, family_name=family_name, eyes=eyes, hairs=hairs)