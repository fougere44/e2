import numpy as np
from flask import Flask, request, render_template, url_for
import pickle
import os
import ast
import sklearn

app = Flask(__name__)

def load_model(model_file):
    loaded_model = pickle.load(open(os.path.join(model_file), "rb"))
    return loaded_model


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if value == val:
            return key


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = request.form['age']
        balance = request.form['balance']
        day = request.form['day']
        duration = request.form['duration']
        campaign = request.form['campaign']
        pdays = request.form['pdays']
        previous = request.form['previous']
        default = request.form['default']
        housing_loan = request.form['housing_loan']
        personal_loan = request.form['personal_loan']
        job = request.form['job']
        marital = request.form['marital']
        education = request.form['education']
        contact_type = request.form['contact_type']
        month = request.form['month']
        poutcome = request.form['poutcome']

        sample_result = {"age": age, "balance": balance, "day": day, "duration": duration, "campaign": campaign, "pdays": pdays, "previous": previous, "default": default, "housing_loan": housing_loan, "personal_loan": personal_loan, "job": job, "marital": marital, "education": education, "contact_type": contact_type, "month": month, "poutcome": poutcome}



        # Traitement de la variable catégorielle job
        job_ast = ast.literal_eval(job)
        liste_job = []

        for i in job_ast:
            liste_job.append(i)


        # Traitement de la variable catégorielle marital
        marital_ast = ast.literal_eval(marital)
        liste_marital = []

        for i in marital_ast:
            liste_marital.append(i)


        # Traitement de la variable catégorielle education 
        education_ast = ast.literal_eval(education)
        liste_education = []

        for i in education_ast:
            liste_education.append(i)


        # Traitement de la variable catégorielle contact 
        contact_ast = ast.literal_eval(contact_type)
        liste_contact = []

        for i in contact_ast:
            liste_contact.append(i)


        # Traitement de la variable catégorielle month 
        month_ast = ast.literal_eval(month)
        liste_month = []

        for i in month_ast:
            liste_month.append(i)

        # Traitement de la variable catégorielle poutcome 
        poutcome_ast = ast.literal_eval(poutcome)
        liste_poutcome = []

        for i in poutcome_ast:
            liste_poutcome.append(i)



        l_total = liste_job + liste_marital + liste_education + liste_contact + liste_month + liste_poutcome
        assert type(l_total) is list

        num_data = [age, balance, day, duration, campaign, pdays, previous, default, housing_loan, personal_loan]
        assert type(num_data) is list

        num_total = num_data + l_total
        assert type(num_total) is list

        numerical_encoded_data = [int(x) for x in num_total]
        assert 42 == len(numerical_encoded_data)
        
        model = load_model('models/bank_model.pkl')
        assert type(model) is sklearn.model_selection._search.GridSearchCV
        
        prediction = model.predict(np.array(numerical_encoded_data).reshape(1, -1))
        assert type(prediction) is np.ndarray

        
        prediction_label = {"Positive Predict": 1, "Negative Predict": 0}
        final_result = get_key(prediction[0], prediction_label)
        assert type(final_result) is str


        pred_prob = model.predict_proba(np.array(numerical_encoded_data).reshape(1, -1))
        pred_probalility_score = {"DAT Positive": pred_prob.round(2)[0][1] * 100, "DAT Negative": pred_prob.round(2)[0][0] * 100}
            

    return render_template("index.html", sample_result=sample_result, prediction=final_result, pred_probalility_score=pred_probalility_score)


if __name__ == "__main__":
    app.run(debug=True)
