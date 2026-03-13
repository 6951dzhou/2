import re
import os

# Function to scan a markdown file and extract image paths

def extract_image_references(markdown_file):
    # Initialize a list to hold image paths
    image_paths = []

    # Regular expression pattern for image references
    image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')

    # Read the markdown file
    with open(markdown_file, 'r') as file:
        content = file.read()
        image_paths = image_pattern.findall(content)

    return image_paths

# Function to check and fix image paths

def fix_image_paths(image_paths):
    fixed_paths = []
    for path in image_paths:
        # Here you can add logic to fix or reorganize image paths as needed
        # For simplicity, let's assume we append a prefix to images
        fixed_paths.append(os.path.join('assets', path))

    return fixed_paths

if __name__ == '__main__':
    markdown_file = 'your_markdown_file.md'  # Specify your markdown file here
    images = extract_image_references(markdown_file)
    fixed_images = fix_image_paths(images)
    print('Extracted Image References:', images)
    print('Fixed Image Paths:', fixed_images)
