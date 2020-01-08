from flask import Flask, render_template
import data_manager
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/applicants')
def all_applicants_first_name():
    applicants = data_manager.get_all_applicants_first_name()
    return render_template('applicants.html', applicants=applicants)


if __name__ == '__main__':
    app.run(debug=True)
