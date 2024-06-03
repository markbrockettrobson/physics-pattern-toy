from numpy import array


class PhysicsObject :
    def __init__(self, position_vector: array=array([0,0]), velocity_vector: array=array([0,0]), mass: float=1) -> None:
        self._position_vector = position_vector
        self._velocity_vector = velocity_vector
        self._mass = mass

    def update(self, dt: float):
        new_position_vector = self._position_vector;
        for i in range(len(self._position_vector)):
            new_position_vector[i] += self._velocity_vector[i]*dt

    def get_position(self):
        return self._position_vector

    def get_velocity(self):
        return self._velocity_vector

    def set_position(self, position: array):
        self._position_vector = position

    def set_velocity(self, velocity: array):
        self._velocity_vector = velocity

    def set_mass(self, mass: float):
        self._mass = mass

    def get_mass(self):
        return self._mass

    def __str__(self) -> str:
        return f"{PhysicsObject.__name__},  Position: {self._position_vector}, Velocity: {self._velocity_vector}, Mass: {self._mass}"

