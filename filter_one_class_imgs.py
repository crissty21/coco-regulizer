import json
from collections import defaultdict

# Load the JSON file
annotations_file = r'train_annotations.json'
with open(annotations_file, 'r') as f:
    filtered_annotations = json.load(f)

# Count the number of unique classes for each image
image_class_counts = defaultdict(set)
for ann in filtered_annotations['annotations']:
    image_id = ann['image_id']
    category_id = ann['category_id']
    image_class_counts[image_id].add(category_id)

# Find images containing only one class
images_with_single_class = {image_id for image_id, classes in image_class_counts.items() if len(classes) == 1}

# Filter out images containing only one class
filtered_images = [img for img in filtered_annotations['images'] if img['id'] not in images_with_single_class]

# Update the annotations to include only annotations for images not containing only one class
remaining_annotations = {'info': filtered_annotations['info'],
                         'licenses': filtered_annotations['licenses'],
                         'categories': filtered_annotations['categories'],
                         'images': filtered_images,
                         'annotations': [ann for ann in filtered_annotations['annotations'] if ann['image_id'] not in images_with_single_class]}

# Save the filtered data to a new JSON file
filtered_file = 'filtered_annotations.json'
with open(filtered_file, 'w') as f:
    json.dump(remaining_annotations, f)

print("Filtered data excluding images containing only one class has been saved to:", filtered_file)
