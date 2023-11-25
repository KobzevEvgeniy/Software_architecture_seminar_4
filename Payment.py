from datetime import datetime

from Person import Person
from Ticket.Ticket import Ticket


class Payment:
    def __init__(self):
        self.id = id
        self.person = Person
        self.ticket = Ticket
        self.date = datetime.now()

    def get_person(self):
        return self.person

    def get_ticket(self):
        return self.ticket

    def get_date(self):
        return self.date

    def pay_ticket(self, ticket, person):
        pass

    def payment_info(self, ticket, person):
        print(f"{ticket.ticket_info()}\n"
              f"{person.get_info_person()}\n"
              f"{self.get_date()}")

    def return_ticket(self,ticket):
        pass

    def send_to_email(self, ticket):
        pass


