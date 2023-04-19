from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('IPL_Prediction_Model.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    team1 = request.form['team1']
    team2 = request.form['team2']
    toss_winner = request.form['toss_winner']
    toss_decision = request.form['toss_decision']

    # Make the prediction using the model
    prediction = model.predict([[team1, team2, toss_winner, toss_decision]])

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
