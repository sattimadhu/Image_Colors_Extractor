from flask import Flask, render_template, request, redirect, url_for
import os
from main import process_image  # Import the main logic from main.py
from fileFun import fileD,rename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploaded_images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
            fileD()
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            try:
                file.save(filepath)
                # Call the function from main.py to process the image
                hex_colors,_ = process_image(filepath)
                rename()
                return render_template('index.html', colors=hex_colors)
            except Exception as e:
                print(f"Error: {e}")
                return "Error processing image."

    return render_template('index.html', colors=None)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
