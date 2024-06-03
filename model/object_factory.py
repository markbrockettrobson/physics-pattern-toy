import random
import math
from typing import List
from model.shape import Shape
from model.visible_object import VisibleObject
from model.physics_object import PhysicsObject

colors = {
    "red": "#f00",
    "green": "#0f0",
    "blue": "#00f",
    "yellow": "#ff0",
    "purple": "#f0f",
    "cyan": "#0ff",
    "white": "#fff",
    "orange": "#ffa500",
    "pink": "#ffc0cb",
    "brown": "#a52a2a",
    "gray": "#808080",
    "silver": "#c0c0c0",
    "gold": "#ffd700",
    "maroon": "#800000",
    "navy": "#000080",
    "olive": "#808000",
    "teal": "#008080",
    "lime": "#00ff00",
    "aqua": "#00ffff",
    "indigo": "#4b0082",
    "violet": "#ee82ee",
    "magenta": "#ff00ff",
    "salmon": "#fa8072",
    "turquoise": "#40e0d0",
    "coral": "#ff7f50",
    "lavender": "#e6e6fa",
    "beige": "#f5f5dc",
    "khaki": "#f0e68c",
    "orchid": "#da70d6",
    "plum": "#dda0dd",
    "skyblue": "#87ceeb",
    "tan": "#d2b48c",
    "wheat": "#f5deb3",
    "thistle": "#d8bfd8",
    "peru": "#cd853f",
    "chartreuse": "#7fff00",
    "crimson": "#dc143c",
    "darkgreen": "#006400",
    "darkorange": "#ff8c00",
    "darkviolet": "#9400d3"
}

def make_random_object(max_x: float, max_y: float, max_speed: float, mass: float =1) -> VisibleObject:
    random_angle = 2 * math.pi * random.random()
    speed = random.random() * max_speed

    new_physics_object = PhysicsObject(
        position_vector=[max_x*random.random(), max_y*random.random()],
        velocity_vector=[speed*math.sin(random_angle), speed*math.cos(random_angle)],
        mass=mass
    )

    return VisibleObject(
        physics_object=new_physics_object,
        shape=Shape.CIRCLE,
        color=random.choice(list(colors.values())),
        size=5
    )


def make_n_random_objects(n: int, max_x: float, max_y: float, max_speed: float, mass: float =1) -> List[VisibleObject]:
    return [make_random_object(max_x, max_y, max_speed, mass) for _ in range(n)]
