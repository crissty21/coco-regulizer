import matplotlib.pyplot as plt
from collections import defaultdict
import json

annotations_file =r'train_annotations_norm.json'
with open(annotations_file, 'r') as f:
    filtered_annotations = json.load(f)
    
category_counts = defaultdict(int)
category_image_counts = defaultdict(set)

# Count the number of instances for each category and the number of images for each category
for ann in filtered_annotations['annotations']:
    category_id = ann['category_id']
    category_counts[category_id] += 1
    category_image_counts[category_id].add(ann['image_id'])
category_names = {}

for cat in filtered_annotations['categories']:
    category_names[cat['id']] = cat['name']
    
categories = [category_names[cat_id] for cat_id in category_counts.keys()]
counts = list(category_counts.values())
image_counts_per_category = [len(image_ids) for image_ids in category_image_counts.values()]

plt.figure(figsize=(10, 6))
bars = plt.bar(categories, counts, color='skyblue')
plt.xlabel('Category')
plt.ylabel('Number of Instances')
plt.title('Total Number of Instances for Each Category')
plt.xticks(rotation=45, ha='right')
for bar, count, img_count in zip(bars, counts, image_counts_per_category) :
    plt.text(bar.get_x() +bar.get_width() /2, bar.get_height(), f'{count}\n{img_count} img', ha='center', va='bottom')
plt.tight_layout()
plt.show()