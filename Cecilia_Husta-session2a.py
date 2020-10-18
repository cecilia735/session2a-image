from PIL import Image
from PIL import ImageFilter
import os

# Assignment:
# Create a new folder called "processed" where all images from "raw" are stored in .png.
# They are all cropped to ratio 4:3 (or 3:4) and resized to be all the same size.

# Notice:
# 1. There are different extensions
# 2. They are all different sizes
# 3. We have portrait and landscape orientated images

# Steps
# 0. Create a new folder
processed_folder = "/Users/Cecilia/Desktop/python/session_2/session2a-image/processed/"
os.mkdir(processed_folder)

# Define old folder
img_folder = "/Users/Cecilia/Desktop/python/session_2/session2a-image/raw/"

# Create list of all images
img_list = os.listdir(img_folder)
img_list.remove('.DS_Store') # remove this unnecessary item
print(img_list)

# Loop over all images
for img_name in img_list:

    # 1. Define portrait and landscape images

    # load the image
    img_path = os.path.join(img_folder, img_name)
    img = Image.open(img_path)

    # define the width, height, and center
    width = img.width
    height = img.height
    center = (width/2, height/2)

    # define shortest and longest side
    shortest_side = min([width, height])
    longest_side = max([width, height])

    # 2. Figure out on which side you have to crop the image
    if shortest_side/3 >= longest_side/4:
        crop_side = longest_side
    else:
        crop_side = shortest_side

    if crop_side == longest_side:
        distance_from_center = crop_side/4
    elif crop_side == shortest_side:
        distance_from_center = crop_side/3
    else:
        print('ERROR: Distance_from_center is undefined')

    # 3. Crop the image

    tuple = []

    if width >= height:
        tuple.append(center[0] - (distance_from_center*2.0))
        tuple.append(center[1] - (distance_from_center*1.5))
        tuple.append(center[0] + (distance_from_center*2.0))
        tuple.append(center[1] + (distance_from_center*1.5))
    elif width < height:
        tuple.append(center[0] - (distance_from_center*1.5))
        tuple.append(center[1] - (distance_from_center*2.0))
        tuple.append(center[0] + (distance_from_center*1.5))
        tuple.append(center[1] + (distance_from_center*2.0))

    print(tuple)

    img_new_ratio = img.crop(tuple)
    # img_new_ratio.show()


    # 4. Resize the image

    if width >= height:
        img_rsz = img_new_ratio.resize((400, 300))
        # img_rsz.show()
    elif width < height:
        img_rsz = img_new_ratio.resize((300, 400))
        # img_rsz.show()

    # 5. Save it to your new folder with the new extension. That's it!

    outfile = img_name + ".png"
    img_rsz.save(os.path.join(processed_folder, outfile))