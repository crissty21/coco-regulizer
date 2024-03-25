import matplotlib.pyplot as plt
from pycocotools.coco import COCO
import json
from collections import defaultdict

annotations_file =r"C:\Users\crist\Desktop\annotations\instances_train2017.json"
#categories_to_keep =[1,2,3,4,5, 6, 7, 8, 10, 17] # List of category names to keep
categories_to_keep = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'traffic light', 'dog']

coco = COCO(annotations_file)
cats = coco.loadCats(coco.getCatIds())
nms = [cat['name'] for cat in cats]
print('coco categories: \n{}\n'.format(''.join(nms)))

category_ids_to_keep = coco.getCatIds(catNms=categories_to_keep)

annotations_to_keep = []
for ann in coco.dataset['annotations']:
    if ann['category_id'] in category_ids_to_keep:
        annotations_to_keep.append(ann)

#print(annotations_to_keep)

coco.dataset['annotations'] = annotations_to_keep

# Remove annotations for categories not in categories_to_keep
categories_to_remove = [cat for cat in coco.getCatIds() if cat not in category_ids_to_keep]
coco.dataset['categories'] = [cat for cat in coco.dataset['categories'] if cat['id'] in category_ids_to_keep]

output_file = 'train_annotations.json'
with open(output_file, 'w') as f:
    json.dump(coco.dataset, f)