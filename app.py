from flask import Flask, render_template, url_for



app = Flask(__name__)

@app.route('/')
def home():
    bg_image_url = url_for('static', filename='images/DALL·E 2024-05-04 13.09.36 - A beautiful and vibrant photo of an assortment of decorative cakes on display at a bakery. The image features a variety of cakes with different design.webp')
    return render_template('home.html', bg_image_url=bg_image_url)

@app.route('/about')
def about():
    return render_template('about.html')

# Add zip to jinja global functions
app.jinja_env.globals.update(zip=zip)

@app.route('/cakes')
def cakes():
    cake_images = [
        url_for('static', filename='images/cake1.webp'),
        url_for('static', filename='images/cake2.webp'),
        url_for('static', filename='images/cake3.webp'),
        url_for('static', filename='images/cake4.webp'),
        url_for('static', filename='images/cake5.webp'),
        url_for('static', filename='images/cake6.webp'),
        url_for('static', filename='images/cake7.webp'),
        url_for('static', filename='images/cake8.webp'),
        url_for('static', filename='images/cake9.webp')
    ]
    cake_names = [
        "Chocolate Cake", "Vanilla Cake", "Red Velvet Cake",
        "Lemon Drizzle", "Carrot Cake", "Black Forest",
        "Cheesecake", "Banana Bread", "Pound Cake"
    ]
    return render_template('cakes.html', cake_images=cake_images, cake_names=cake_names)

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
