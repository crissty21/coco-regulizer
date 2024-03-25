import os
import shutil
import json

# Load the balanced annotations JSON file
balanced_annotations_file = 'train_annotations_norm.json'
with open(balanced_annotations_file, 'r') as f:
    balanced_annotations = json.load(f)

# Directory containing all images
images_folder = r"E:\Downloads - Chrome\train2017\train2017"

# Directory to store only the required images
output_folder = r"E:\train_img_ram"
os.makedirs(output_folder, exist_ok=True)

# Get a set of all image file names from the balanced annotations
required_images = {image['file_name'] for image in balanced_annotations['images']}
print(len(required_images))
# Iterate over the files in the images folder and move required images to the output folder
for filename in os.listdir(images_folder):
    if filename in required_images:
        source = os.path.join(images_folder, filename)
        destination = os.path.join(output_folder, filename)
        shutil.copyfile(source, destination)

print("Required images have been copied to:", output_folder)
