from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://media1.giphy.com/media/EVGlX9PvSyusGB4aZz/giphy.gif",
    "https://media4.giphy.com/media/eiSJYf5FLYGMFXoIod/giphy.gif",
    "https://media0.giphy.com/media/SsqksUwZx3BdNIYlSE/giphy.gif",
    "https://media0.giphy.com/media/J62Fq3m1UJl75QbLmN/giphy.gif",
    "https://media0.giphy.com/media/iFrVcSxGNbiXnJWDvO/giphy.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
