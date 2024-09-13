from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from sklearn.cluster import KMeans

app = Flask(__name__)
UPLOAD_FOLDER = 'uploaded_images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to convert RGB to Hex
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

# Route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)

        file = request.files['image']
        if file.filename == '':
            return redirect(request.url)

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            try:
                file.save(filepath)
                img = Image.open(filepath)
                img = img.resize((img.width // 2, img.height // 2))
                img_data = np.array(img)

                # Check if the image has RGB channels
                if img_data.ndim != 3 or img_data.shape[2] != 3:
                    return "Uploaded image is not an RGB image."

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
                color_image_path = os.path.join('static', 'colors.png')
                plt.axis('off')
                plt.savefig(color_image_path, bbox_inches='tight', pad_inches=0)
                plt.close()

                return render_template('index.html', colors=hex_colors)
            except Exception as e:
                print(f"Error: {e}")
                return "Error processing image."
                
    return render_template('index.html', colors=None)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
