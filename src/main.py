import openpyxl

from flask import Flask, render_template
from CSpace import CSpace

# load workbook into cspace object
wb = openpyxl.load_workbook('cSpace_booking.xlsx')
cspace = CSpace(wb)

# setup flask project
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:date>')
def show_people_by_date(date):
    clients_credits = cspace.run(date)
    return render_template('tables.html', clients=clients_credits, date=date)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
