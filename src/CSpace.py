from Client import Client
from Room import Room


class CSpace:
    def __init__(self, workbook):
        self.clients = {}
        self.rooms = {}
        self.workbook = workbook
        self.clients_array = self.extract_data(workbook['Clients'])
        self.room_array = self.extract_data(workbook['Facilities'])
        self.rates = self.extract_rates(workbook['Rates'])

    def __str__(self):
        temp_string = ''
        for client in self.clients.values():
            temp_string += str(client) + '\n'

        return temp_string

    def add_client(self, client):
        self.clients[client.first_name] = client

    def add_clients_from_array(self, clients_array):
        for client_info in clients_array:
            self.add_client(Client(client_info))

    def add_rooms_from_array(self, room_array, rate_sheet):
        rate_dict = self.extract_rates(rate_sheet)
        for room_info in room_array:
            current_room = Room(room_info)
            current_room.assign_rate(rate_dict)
            self.rooms[current_room.name] = current_room

    def update_credits(self, bookings):
        for booking_name in bookings:
            current_room_rate = self.rooms[booking_name].rate
            for client_first_name in bookings[booking_name]:
                if client_first_name is not None and client_first_name is not '':
                    self.clients[client_first_name].add_credits(current_room_rate)

    def run(self, date_input):
        booking_dict = self.extract_bookings(self.workbook[date_input])
        self.add_rooms_from_array(self.room_array, self.workbook['Rates'])
        self.add_clients_from_array(self.clients_array)

        self.update_credits(booking_dict)

        output_array = []
        for client in self.clients:
            output_array.append((self.clients[client].first_name, self.clients[client].last_name, self.clients[client].credits))

        return output_array

    @staticmethod
    def extract_data(data_sheet):
        data = []
        for row in data_sheet.iter_rows(min_row=2, max_row=data_sheet.max_row, max_col=data_sheet.max_column):
            individual_data = []
            for cell in row:
                individual_data.append(cell.value)

            data.append(individual_data)

        return data

    @staticmethod
    def extract_rates(rate_sheet):
        rates = {}
        rows = rate_sheet['B2':'C' + str(rate_sheet.max_row)]

        for row in rows:
            rates[row[0].value] = row[1].value

        return rates

    @staticmethod
    def extract_bookings(month_sheet):
        bookings = {}
        heading = ''

        for cols in month_sheet.iter_cols(min_row=1, max_row=month_sheet.max_row, min_col=3):
            for x, cell in enumerate(cols):
                if x is 0:
                    heading = cell.value
                    bookings[heading] = []
                else:
                    bookings[heading].append(cell.value)

        return bookings
