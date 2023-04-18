from flask import Flask, abort, send_file

app = Flask(__name__)
image_dir = "./"



# Define routes for different images
@app.route('/apple')
def appHome_image():
    image_name = "appleHome.jpg"
    return display_image(image_name)


# Define routes for different images


# Helper function to retrieve and display an image from the local directory
def display_image(image_name):
    try:
        image_path = f"{image_dir}/{image_name}"
        return send_file(image_path, mimetype="image/jpeg")
    except Exception as e:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))