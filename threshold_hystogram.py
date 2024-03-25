import json
from collections import defaultdict

# Load the JSON file
annotations_file = r'filtered_annotations.json'
with open(annotations_file, 'r') as f:
    filtered_annotations = json.load(f)

# Count the number of annotations for each class and collect image IDs
category_counts = defaultdict(list)
for ann in filtered_annotations['annotations']:
    category_id = ann['category_id']
    category_counts[category_id].append(ann)

# Find the third maximum number of annotations across all classes
all_annotations_counts = [len(annotations) for annotations in category_counts.values()]
sorted_counts = sorted(all_annotations_counts, reverse=True)
third_max_annotations = sorted_counts[2] if len(sorted_counts) >= 3 else max(sorted_counts)

# Collect image IDs used in annotations after thresholding
used_image_ids = set()
for category_id, annotations in category_counts.items():
    used_image_ids.update(ann['image_id'] for ann in annotations[:third_max_annotations])

# Filter images based on used image IDs
filtered_images = [img for img in filtered_annotations['images'] if img['id'] in used_image_ids]

# Create balanced annotations with filtered images
balanced_annotations = {'info': filtered_annotations['info'],
                        'licenses': filtered_annotations['licenses'],
                        'categories': filtered_annotations['categories'],
                        'images': filtered_images,
                        'annotations': []}

# Populate balanced annotations with annotations after thresholding
for category_id, annotations in category_counts.items():
    balanced_annotations['annotations'].extend(annotations[:third_max_annotations])

# Save the balanced data to a new JSON file
balanced_file = 'train_annotations_norm.json'
with open(balanced_file, 'w') as f:
    json.dump(balanced_annotations, f)

print("Balanced data including annotations, info, licenses, images, and categories based on the third maximum number of annotations have been saved to:", balanced_file)
