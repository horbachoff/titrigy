import random
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'mysecret'

employees = []
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

class EmployeeForm(FlaskForm):
    employee = StringField("Employee Name:")
    submit = SubmitField("add")

@app.route('/', methods=["GET", "POST"])
def index():
    if 'employee' in request.form:
        employees.append(request.form['employee'])
    schedule = {}
    if request.method == "POST" and 'generate' in request.form:
        if len(employees) > 0:
            for i, weekday in enumerate(weekdays):
                if i>=len(employees):
                    schedule[weekday] = employees[i % len(employees)]
                else:
                    schedule[weekday] = employees[i]
    return render_template("index.html", employees=employees, template_form=EmployeeForm(), weekdays=weekdays, schedule=schedule)

if __name__ == "__main__":
    app.run(debug=True)