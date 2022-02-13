import pickle as pickle
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/viewappointment',methods=['GET'])
def viewappointment():
    return render_template('previousbooking.html')

@app.route('/community',methods=['GET'])
def community():
    return render_template('community.html')

@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/appointmentform',methods=['GET'])
def appointmentform():
    return render_template('appointmentform.html')

@app.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/firstaid',methods=['GET'])
def firstaid():
    return render_template('firstaid.html')

@app.route('/service',methods=['GET'])
def service():
    return render_template('service.html')

@app.route('/passwordless',methods=['GET'])
def sawo():
    return render_template('sawo.html')

@app.route('/corona', methods=["GET", "POST"])
def corona():
    file = open('corona.pkl', 'rb')
    clf = pickle.load(file)
    file.close()
    if request.method == "POST":
        myDict = request.form
        fever = int(myDict['fever'])
        age = int(myDict['age'])
        pain = int(myDict['pain'])
        runnyNose = int(myDict['runnyNose'])
        diffBreath = int(myDict['diffBreath'])
        # Code for Inference
        inputFeatures = [fever, pain, age, runnyNose, diffBreath]
        infProb = clf.predict_proba([inputFeatures])[0][1]
        if round(infProb * 100) >= 50:
            prediction = "May have COVID"
            greet = "Oops!"
        else:
            prediction = "You are Normal"
            greet = "Great!"
        return render_template('prediction.html', greet=greet, prediction=prediction)
    return render_template('corona.html')

if __name__=='__main__':
    app.run()

