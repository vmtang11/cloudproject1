from flask import Flask, jsonify, redirect
import pandas as pd
import wikipedia

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

@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

@app.route('/wikipedia/<company>')
def wikipedia_route(company):

    # Imports the Google Cloud client library
    from google.cloud import language
    result = wikipedia.summary(company, sentences=10)

    client = language.LanguageServiceClient()
    document = language.Document(
        content=result,
        type_=language.Document.Type.PLAIN_TEXT)
    encoding_type = language.EncodingType.UTF8
    entities = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type}).entities
    return str(entities)

@app.route('/weather')
def weather():
    """Redirects to Durham weather page"""
    return redirect('https://weather.com/weather/tenday/l/Durham+NC?canonicalCityId=63d89211f7bcfd0da57abeac727a32c0f62cb675513c8c4da3432fa06c0a8581')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
