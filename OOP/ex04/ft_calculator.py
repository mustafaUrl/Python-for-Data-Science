class calculator:
    """A class that represents a calculator for vector operations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> float:
        """Calculate the dot product of two vectors."""

        vectors = (sum(x * y for x, y in zip(V1, V2)))
        print("Dot product is: ", vectors)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> list[float]:
        """Add two vectors."""

        vectors = [float(x + y) for x, y in zip(V1, V2)]
        print("Add Vector is : ", vectors)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> list[float]:
        """Subtract two vectors."""
        vectors = [float(x - y) for x, y in zip(V1, V2)]
        print("Sous Vector is: ", vectors)
