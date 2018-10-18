import openpyxl

from flask import Flask, render_template, send_from_directory
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

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/resources/js/', path)

@app.route('/admin')
def admin():
    return render_template('admin_nav.html')

@app.route('/credits')
def credits():
    return render_template('credits.html')

@app.route('/rates')
def rates():
    return render_template('rates.html')

@app.route('/<string:date>')
def show_people_by_date(date):
    clients_credits = cspace.run(date)
    return render_template('tables.html', clients=clients_credits, date=date)

@app.route('/clients')
def show_clientlist():
    cspace.add_clients_from_array(cspace.clients_array)
    return render_template('clients.html', clients=cspace.clients)

cspace.add_clients_from_array(cspace.clients_array)
@app.route('/clients/<name>')
def client_page(name=None):
    return render_template('client_info.html', clients=cspace.clients, name=name)

@app.route('/ws/<string:date>')
def get_bookings_by_month(date):
    monthly_booking = cspace.extract_bookings(cspace.workbook[date])
    cspace.add_rooms_from_array(cspace.room_array, cspace.workbook['Rates'])
    # monthly_booking = cspace.extract_bookings(date)
    # print(monthly_booking)

    colors = ['#C39BD3', '#7FB3D5', '#7DCEA0', '#F0B27A', '#808B96']
    i = 0
    dataRates = {}
    for type, credit in cspace.rates.items():
        dataRates[type] = {'Credits': credit, 'Color': colors[i]}
        i = i + 1

    cols = len(next(iter(monthly_booking.values() )))
    rows = len(monthly_booking)
    return render_template('base-calendar.html',
                           monthly_booking=monthly_booking,
                           rows=rows,
                           cols=cols,
                           rates=dataRates,
                           facilities=cspace.rooms,
                           clients=cspace.clients,
                           date=date)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
