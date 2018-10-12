import openpyxl
import unittest
from Room import Room
from CSpace import CSpace


class TestRoom(unittest.TestCase):
    def setUp(self):
        room_data = ('First Floor Hall', 'Gallery', 'King Edward', '', '')
        self.room = Room(room_data)

        workbook = openpyxl.Workbook()

        self.rate_sheet = workbook.active
        self.rate_sheet.title = 'Rates'

        rates = (
            ('Location', 'Type', 'Credits'),
            ('King Edward', 'Desk', 1),
            ('King Edward', 'Gallery', 5),
            ('King Edward', 'Meeting', 3)
        )

        for row in rates:
            self.rate_sheet.append(row)

    def test_add_rate(self):
        self.assertEqual(0, self.room.rate)
        self.room.add_rate(5)
        self.assertEqual(5, self.room.rate)

    def test_assign_rate_from_dict(self):
        rate_dict = CSpace.extract_rates(self.rate_sheet)
        self.assertEqual(0, self.room.rate)
        self.room.assign_rate(rate_dict)
        self.assertEqual(5, self.room.rate)

        unknown_dict = {
            'Nowhere Room': 10000
        }

        self.room.assign_rate(unknown_dict)
        self.assertEqual(0, self.room.rate)
