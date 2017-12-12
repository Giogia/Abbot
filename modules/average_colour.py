from PIL import Image
import colorsys

#name is the image name string as follows "example.jpg"

def average_image_colour(name):
    image = Image.open("resources/"+name)
    image = image.resize((50,50))  # Small optimization
    width, height = image.size
    
    r_total = 0
    g_total = 0
    b_total = 0
    
    count = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = image.getpixel((x,y))
            r_total += r
            g_total += g
            b_total += b
            count += 1

    hsv = list(colorsys.rgb_to_hsv(r_total,g_total,b_total))
    hsv[1] = 1 #(hope)fully saturated
    rgb = list(colorsys.hsv_to_rgb(hsv[0],hsv[1],hsv[2]))
    return (rgb[1], rgb[0], rgb[2]) #see r,g,b values


def print_average_colour(name):
    average_colour = average_image_colour(name)
    print(average_colour)



