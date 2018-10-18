import openpyxl

from flask import Flask, render_template
from CSpace import CSpace
from Client import Client

# load workbook into cspace object
wb = openpyxl.load_workbook('./data/cSpace_booking.xlsx')
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

@app.route('/clients')
def show_clientlist():
    cspace.add_clients_from_array(cspace.clients_array)
    return render_template('clients.html', clients=cspace.clients)

@app.route('/clients')
def show_clientlist():
    cspace.add_clients_from_array(cspace.clients_array)
    return render_template('clients.html', clients=cspace.clients)

cspace.add_clients_from_array(cspace.clients_array)
@app.route('/clients/<name>')
def client_page(name=None):
    return render_template('client_info.html', clients=cspace.clients, name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
