import openpyxl
import datetime
import json

from flask import Flask, render_template, send_from_directory
from CSpace import CSpace
from Client import Client


# load workbook into cspace object
wb = openpyxl.load_workbook('./data/cSpace_booking.xlsx')
cspace = CSpace(wb)

# setup flask project
app = Flask(__name__)
app.static_folder = 'templates/resources'


@app.route('/')
def index():
    with open('data/testimonials.json') as json_data:
        testimonials = json.load(json_data)

    print(testimonials)

    return render_template('index.html', testimonials=testimonials)


# @app.route('/js/<path:path>')
# def send_js(path):
#     return send_from_directory('templates/resources/js/', path)


@app.route('/admin')
def admin():
    return render_template('admin_nav.html')

@app.route('/credits')
def credits():
    return render_template('credits.html')


@app.route('/rates')
def rates():
    return render_template('rates.html')


@app.route('/clients')
def show_clientlist():
    cspace.add_clients_from_array(cspace.clients_array)
    return render_template('clients.html', clients=cspace.clients)


cspace.add_clients_from_array(cspace.clients_array)
@app.route('/clients/<name>')
def client_page(name=None):
    return render_template('client_info.html', clients=cspace.clients, name=name)


@app.route('/calendar')
def get_bookings():
    # Get Rates
    cspace.add_rooms_from_array(cspace.room_array, cspace.workbook['Rates'])

    # Color code for Rates
    colors = ['#C39BD3', '#7FB3D5', '#7DCEA0', '#F0B27A', '#808B96']
    i = 0
    dataRates = {}
    for type, credit in cspace.rates.items():
        dataRates[type] = {'Credits': credit, 'Color': colors[i]}
        i = i + 1

    # Get Month tabs from excel worksheet
    sheets = cspace.workbook.sheetnames
    sheets.remove('Clients')
    sheets.remove('Facilities')
    sheets.remove('Rates')

    # Form the data structure to be sent to template
    #   it will include all the month tabs from the excel spreadsheet
    tempData = {}
    for month_sheet in sheets:
        monthly_booking = cspace.extract_bookings(cspace.workbook[month_sheet])
        mydate = month_sheet.split('-')

        mdate = datetime.date(int(mydate[0]), int(mydate[1]), 1)
        maxDays = cspace.last_day_of_month(mdate)
        dayheader = [];
        for myday in range(maxDays):
            mdate = datetime.date(int(mydate[0]), int(mydate[1]), myday+1)
            dayheader.append(mdate.strftime('%a'))

        tempData[month_sheet] = {
                    'dayheader': dayheader,
                    'bookings': monthly_booking,
                    'maxrows': len(monthly_booking),
                    'maxcols': maxDays }

    # print(tempData)
    return render_template('base-calendar.html',
                           tempData=tempData,
                           rates=dataRates,
                           facilities=cspace.rooms,
                           clients=cspace.clients)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
