class Vector:
    def __init__(self, components):
        if not isinstance(components, list) or not all(isinstance(x, (int, float)) for x in components):
            raise ValueError("Components must be a list of numbers.")
        self._components = components

    def __str__(self):
        return f"{len(self._components)}-dimensional vector: {self._components}"

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Can only scale by a real number.")
        return Vector([x * scalar for x in self._components])

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __add__(self, other):
        if not isinstance(other, Vector) or len(self._components) != len(other._components):
            raise ValueError("Vectors must be of the same dimension to add.")
        return Vector([self._components[i] + other._components[i] for i in range(len(self._components))])

    def __sub__(self, other):
        if not isinstance(other, Vector) or len(self._components) != len(other._components):
            raise ValueError("Vectors must be of the same dimension to subtract.")
        return Vector([self._components[i] - other._components[i] for i in range(len(self._components))])

    def __matmul__(self, other):
        if not isinstance(other, Vector) or len(self._components) != len(other._components):
            raise ValueError("Vectors must be of the same dimension to compute dot product.")
        return sum(self._components[i] * other._components[i] for i in range(len(self._components)))


v1 = Vector([1, 2, 3])
print(v1)
v2 = 2 * v1
print(v2)
v3 = v1 * 3
print(v3)
v4 = Vector([4, 5, 6])
print(v1 + v4)
print(v1 - v4)
print(v1 @ v4)
