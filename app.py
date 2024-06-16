from flask import Flask, render_template, request, url_for, flash, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for session management and flash messages

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''  # Use your email
app.config['MAIL_PASSWORD'] = ''  # Use your app-specific password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def home():
    bg_image_url = url_for('static', filename='images/BeautifulCake.webp')
    return render_template('home.html', bg_image_url=bg_image_url)

@app.route('/about')
def about():
    bg_image_url = url_for('static', filename='images/BeautifulCake.webp')  # Ensure this matches your actual file path
    return render_template('about.html', bg_image_url=bg_image_url)

# Adding zip to Jinja global functions for template iteration
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

@app.route('/send_mail', methods=['POST'])
def send_mail():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        msg = Message('Contact Form Submission from ' + name,
                      sender=app.config['MAIL_USERNAME'],  # Sender email
                      recipients=['njabuldinho@gmail.com'])  # Change to your email
        msg.body = f"Received a message from {name} ({email}):\n\n{message}"
        mail.send(msg)
        
        flash('Message sent successfully! Thank you for your feedback.', 'success')
        return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)
