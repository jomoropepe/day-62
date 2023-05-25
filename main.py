from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    op_time = StringField('Opening Time eg. 8AM', validators=[DataRequired()])
    cl_time = StringField('Closing Time eg. 8AM', validators=[DataRequired()])
    rating_choices = ["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
    rating = SelectField('Coffe Rating', choices=[(rating_choices, rating_choices) for rating_choices in rating_choices],default=1)
    # rating = StringField('Coffe Rating', validators=[DataRequired()])
    wifi_choices = ["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
    wifi = SelectField('Wifi Strength Rating', choices=[(wifi_choices, wifi_choices) for wifi_choices in wifi_choices], default=1)
    # wifi = StringField('Wifi Strength Rating', validators=[DataRequired()])
    power_choices = ["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]
    power = SelectField('Power Socket Aviability', choices=[(power_choices, power_choices) for power_choices in power_choices], default=1)
    # power = StringField("Power Socket Aviability", validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        new_cafe = [form.cafe.data, form.location.data, form.op_time.data, form.cl_time.data, form.rating.data, form.wifi.data, form.power.data]
        print(new_cafe)
        with open('C:\\Users\\Pepe\\PycharmProjects\\day-62\\cafe-data.csv', mode='a', encoding="utf8", newline='') as cafe_file:
            cafe_data = csv.writer(cafe_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            cafe_data.writerow(new_cafe)
        return cafes()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('C:\\Users\\Pepe\\PycharmProjects\\day-62\\cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
