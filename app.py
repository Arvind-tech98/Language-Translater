from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        text = request.form.get('text', '')
        language = request.form.get('language', '')

        if not text or not language:
            return jsonify({'error': 'Invalid input'})

        translator = Translator()
        translated_text = translator.translate(text, dest=language).text

        return jsonify({'translated_text': translated_text})

    return jsonify({'error': 'Method not allowed'})

if __name__ == '__main__':
    app.run(debug=True)
