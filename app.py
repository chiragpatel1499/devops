from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://photos.app.goo.gl/fJg2N4SV8ysUNgf8A",
    "https://photos.app.goo.gl/zPRDcNr2Et4sFkXh9",
    "https://photos.app.goo.gl/RuV5YYWzaymVqRfZ6",
    "https://photos.app.goo.gl/Mvjo6bd6mpqoSHV47"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
