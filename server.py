from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.applicants('/applicants')
def all_applicants_first_name():
    return render_template('applicants.html')


if __name__ == '__main__':
    app.run(debug=True)
