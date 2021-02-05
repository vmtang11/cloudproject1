from flask import Flask, redirect
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World! Welcome to my project 1. Testing continuous delivery...'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """

@app.route('/weather')
def weather():
    """Redirects to Durham weather page"""
    return redirect('https://weather.com/weather/tenday/l/Durham+NC?canonicalCityId=63d89211f7bcfd0da57abeac727a32c0f62cb675513c8c4da3432fa06c0a8581')

@app.route('/cloud')
def cloud():
    """Redirect to Cloud Computing home page"""
    return redirect('https://noahgift.github.io/cloud-data-analysis-at-scale/')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
