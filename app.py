from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text-input']
    
    result = model(text)
    
    sentiment = result[0]['label']
    score = result[0]['score']
    
    return jsonify(sentiment=sentiment, score=score)

if __name__ == '__main__':
    app.run(debug=True)
