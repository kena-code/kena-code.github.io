from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

# Define a default profile
default_profile = {
    'names': 'Emmanuel Noe A. KPADEDJI',
    'age': 27,
    'location': 'Saint Petersburg'
}

# Route for the default page, redirects to the profile page
@app.route('/')
def index():
    return redirect(url_for('profile'))

# Route for the profile page
@app.route('/profile')
def profile():
    return render_template('index.html', **default_profile)

if __name__ == '__main__':
    app.run(debug=True)