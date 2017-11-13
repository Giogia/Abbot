from PIL import Image
import matplotlib.pyplot as plt

def average_image_colour(name):
    image = Image.open(name)
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

    return (r_total/count, g_total/count, b_total/count)

#see r,g,b values
def print_average_image_colour(name)
    average_colour = average_image_colour(image)
    print(average_colour)

#display colour
def display_average_colour(name)
    average_colour = average_image_colour(image)
    plt.imshow([[(average_colour)]])
    plt.show
