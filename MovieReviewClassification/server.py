from flask import Flask,render_template, request, jsonify
import pickle
from test import predictReview

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_word():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    input_data = next(request.form.values())
    result = predictReview(input_data)
    return render_template('index.html', prediction=result)


if __name__ == '__main__':
    app.run(port=3000, debug=True)