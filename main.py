import random
import sys
from PIL import Image
#Scans the pixels in Image 2 to check for pixels with an RGB value close to the RGB value of white (255,255,255) so that the white background in Image 2 disappears relatively well when pasted onto image 2
def inRange(pixel):
    (r,g,b) = pixel
    if (r > 233 and g > 233 and b > 233):
        return False
    else:
        return True

input_path = sys.argv[1]
input_path2 = "lightning-emoji.jpg"
output_path = sys.argv[2]
#img 1 is the lion
#img 2 is the lightning emoji
img = Image.open(input_path)
img2 = Image.open(input_path2)
width, height = img.size
width2, height2 = img2.size
new_img = Image.new("RGB", (width, height), "white")

columnlist = list()
columnlist2 = list()
#Gets all pixels from first image
for i in range(0,width):
    column = list()
    for j in range(0,height):
        column.append(img.getpixel((i,j)))
    columnlist.append(column)
#Gets all pixels from second image
for i in range(0,width2):
    column = list()
    for j in range(0,height2):
        column.append(img2.getpixel((i,j)))
    columnlist2.append(column)
#Modifies image 1 pixel color
for i in range(0,width):
    for j in range(0,height):
        (r,g,b) = columnlist[i][j]
        colors = [(r,g,b),(100,g,b),(r,40,b),(r,g,20)]
        columnlist[i][j] = random.choice(colors)
#Paste image 2 in image 1
for i in range(0,width2):
    for j in range(0,height2):
        if (inRange(columnlist2[i][j])):
            columnlist[i + width * 95 // 162][j + height // 3] = columnlist2[i][j]

#Saves new image to file
for i in range(0,width):
    for j in range(0,height):
        new_img.putpixel((i, j), columnlist[i][j])


new_img.save(output_path)
