from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/consulting')
def about():
    return render_template('consulting.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/rootfs')
def rootfs():
    return render_template('rootfs.html')

if __name__ == '__main__':
    app.run()
