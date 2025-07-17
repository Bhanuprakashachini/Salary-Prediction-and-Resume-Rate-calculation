from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import os

app = Flask(__name__)

domain_skills_path = 'C:\\Users\\pc\OneDrive\\sp project (5)\\sp project\\domain_vs_skills_upd.xlsx'
salary_path = 'C:\\Users\pc\\OneDrive\\sp project (5)\\sp project\\salary.xlsx'

def process_resume(domain, input_skill):
    if not os.path.exists(domain_skills_path):
        return "Error: The domain_vs_skills.xlsx file was not found."

    try:
        short_ = pd.read_excel(domain_skills_path)
    except Exception as e:
        return f"Error reading domain_vs_skills.xlsx file: {str(e)}"

    def convert_skill(obj):
        """
        :type obj: object
        """
        l = []
        l.append(obj)
        return l

    for i in range(len(short_)):
        obj = short_.iloc[i].skills
        convert_skill(obj)
        short_['skills'] = short_.skills.apply(convert_skill)
        short_['skills'] = short_.skills.apply(lambda x: [i.replace(" ", "") for i in x])
        short_ = short_.explode('skills')

    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(short_['skills']).toarray()
    similarity = cosine_similarity(vectors)

    def job_role(domain, input_skills):
        for i in range(len(short_)):
            if domain == short_.job_role[i]:
                domain_skills = [short_.skills[i]]
                domain_vector = cv.transform(domain_skills).toarray()
                input_vector = cv.transform([input_skills]).toarray()
                result = cosine_similarity(domain_vector, input_vector)
                return result[0][0]
        return None  # Return None if the domain is not found

    input_skills = input_skill.replace(' ', '')
    result = job_role(domain, input_skills)

    if result is None:
        return "Error: Domain not found or no matching skills."

    return f"The similarity percentage is {result * 100:.2f}%"


# Function to process Google salary prediction
def process_google(jobrole, experience_, test_score_, inter_view_score_):
    if not os.path.exists(salary_path):
        return "Error: The google_salary.xlsx file was not found."

    try:
        df = pd.read_excel(salary_path)
    except Exception as e:
        return f"Error reading google_salary.xlsx file: {str(e)}"

    le = LabelEncoder()
    df['job_role'] = le.fit_transform(df['job_role'])
    input_ = df[['job_role', 'experience', 'test_score', 'interview_score']]
    target = df['salary']

    lr = LinearRegression()
    lr.fit(input_, target)

    jobrole_ = le.transform([jobrole])
    prediction = lr.predict(
        np.concatenate((jobrole_.reshape(1, -1), [[experience_, test_score_, inter_view_score_]]), axis=1))
    return f"The predicted salary is {prediction[0]:,.2f} LPA"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/resume', methods=['POST'])
def resume():
    domain = request.form['domain']
    input_skill = request.form['input_skill']
    result = process_resume(domain, input_skill)
    return render_template('index.html', result=result)


@app.route('/google', methods=['POST'])
def google():
    jobrole = request.form['jobrole']
    experience_ = int(request.form['experience'])
    test_score_ = int(request.form['test_score'])
    inter_view_score_ = int(request.form['interview_score'])
    result = process_google(jobrole, experience_, test_score_, inter_view_score_)
    return render_template('index.html', result=(result))


if __name__ == '__main__':
    app.run(debug=True)
