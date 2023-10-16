from PIL import Image


# Converting white of an image to transparent
def color_is_white(color):
    return color[0] > 250 and color[1] > 250 and color[2] > 250


with Image.open("graphics/student/Student.png") as im:
    im.convert("RGBA")
    image_data = list(im.getdata())
    new_data = [(r, g, b, 0) if color_is_white((r, g, b)) else (r, g, b, a) for (r, g, b, a) in image_data]
    im.putdata(new_data)
    im.save("graphics/student/Student2.png", "PNG")