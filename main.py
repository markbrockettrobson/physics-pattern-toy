
from tqdm import tqdm
from model.object_factory import make_n_random_objects
from PIL import ImageDraw, Image

if __name__ == "__main__":
    # Your code here
    x_size = 400
    y_size = 400

    visible_objects = make_n_random_objects(20, x_size, y_size, 1, 3)

    frames = []

    for i in tqdm(range(500)):
        for visible_object in visible_objects:
            visible_object.update(1)


        image = Image.new("RGB", (x_size, y_size), (100, 100, 100))
        image_draw = ImageDraw.ImageDraw(image)

        for visible_object in visible_objects:
            visible_object.render(image_draw)

        frames.append(image)

    frames[0].save('random_dots.gif',
               save_all=True,
               append_images=frames[1:],
               optimize=False,
               duration=40,
               loop=0)