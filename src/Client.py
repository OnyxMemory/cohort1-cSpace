class Client:
    def __init__(self, client_info):
        self.name, self.email, self.phone, self.payment_method, self.payment_status, self.issues, self.notes = client_info
        self.first_name, self.last_name = self.name.split()
        self.credits = 0
        self.bookings = {}

    def __str__(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'credits': self.credits
        }

    def add_credits(self, number_of_credits):
        self.credits += number_of_credits
