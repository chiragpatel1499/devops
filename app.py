from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
]

@app.route('/')
def index():
    url = random.choice(images)
    printf("Hello url : ")
    printf(url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
