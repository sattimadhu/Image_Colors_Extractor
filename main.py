import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt # type: ignore
import matplotlib.colors as mcolors # type: ignore
from sklearn.cluster import KMeans

# Function to convert RGB to Hex
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

# Function to process the image and extract colors
def process_image(filepath):
    img = Image.open(filepath)

    # Convert the image to RGB if it's not already in RGB format
    if img.mode != 'RGB':
        img = img.convert('RGB')

    img = img.resize((img.width // 2, img.height // 2))
    img_data = np.array(img)

    # Reshape the image data to a 2D array of RGB values
    pixels = img_data.reshape(-1, 3)

    # Use KMeans to find the most frequent colors
    kmeans = KMeans(n_clusters=10, random_state=0).fit(pixels)
    centers = kmeans.cluster_centers_

    # Convert cluster centers to hex colors
    hex_colors = sorted(set(rgb_to_hex(tuple(map(int, color))) for color in centers))

    # Generate a color palette image using matplotlib
    plt.figure(figsize=(10, 2))
    plt.imshow([list(mcolors.hex2color(c) for c in hex_colors)], aspect="auto")
    color_image_path = os.path.join('palettes', 'colors.png')
    plt.axis('off')
    plt.savefig(color_image_path, bbox_inches='tight', pad_inches=0)
    plt.close()
    print(hex_colors)
    return hex_colors, color_image_path
