import openpyxl
import datetime

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

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

@app.route('/calendar')
def get_bookings():
    monthly_booking = cspace.extract_bookings(cspace.workbook['2018-09'])

    mydate = '2018-09'.split('-')

    mdate = datetime.date(int(mydate[0]), int(mydate[1]), 1)
    maxDays = last_day_of_month(mdate).day
    dayheader = [];
    for myday in range(maxDays):
        mdate = datetime.date(int(mydate[0]), int(mydate[1]), myday+1)
        dayheader.append(mdate.strftime('%a'))
    # print(maxDays, dayheader)
    cspace.add_rooms_from_array(cspace.room_array, cspace.workbook['Rates'])
    # monthly_booking = cspace.extract_bookings(date)
    # print(monthly_booking)

    tempData = {'date': '2018-09',
                'dayheader': dayheader,
                'bookings': monthly_booking,
                'maxrows': len(monthly_booking),
                'maxcols': maxDays }
    colors = ['#C39BD3', '#7FB3D5', '#7DCEA0', '#F0B27A', '#808B96']
    i = 0
    dataRates = {}
    for type, credit in cspace.rates.items():
        dataRates[type] = {'Credits': credit, 'Color': colors[i]}
        i = i + 1


    # cols = len(next(iter(monthly_booking.values() )))
    # rows = len(monthly_booking)
    return render_template('base-calendar.html',
                           tempData=tempData,
                           rates=dataRates,
                           facilities=cspace.rooms,
                           clients=cspace.clients)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
