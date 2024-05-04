from flask import Flask, render_template, url_for



app = Flask(__name__)

@app.route('/')
def home():
    bg_image_url = url_for('static', filename='images/DALL·E 2024-05-04 13.09.36 - A beautiful and vibrant photo of an assortment of decorative cakes on display at a bakery. The image features a variety of cakes with different design.webp')
    return render_template('home.html', bg_image_url=bg_image_url)


if __name__ == '__main__':
    app.run(debug=True)
