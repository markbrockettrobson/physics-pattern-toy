from model.shape import Shape
from model.physics_object import PhysicsObject
from PIL import ImageDraw

class VisibleObject:
    def __init__(self, physics_object: PhysicsObject, shape: Shape, color: str, size):
        self._physics_object = physics_object
        self._shape = shape
        self._color = color
        self._size = size

    def render(self, image_draw: ImageDraw.ImageDraw):
        if self._shape == Shape.CIRCLE:
            image_draw.ellipse(
                (
                    self._physics_object.get_position()[0] - (self._size/2),
                    self._physics_object.get_position()[1] - (self._size/2),
                    self._physics_object.get_position()[0] + (self._size/2),
                    self._physics_object.get_position()[1] + (self._size/2)
                ),
                fill=self._color
            )

        else:
            image_draw.regular_polygon(
                (
                    self._physics_object.get_position()[0],
                    self._physics_object.get_position()[1],
                    self._size
                ),
                self._shape.value,
                self._color)

    def update(self, dt: float):
        self._physics_object.update(dt)