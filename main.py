import datetime

from Payment import Payment
from Person import Person
from Ticket.BusRoute import BusRoute
from Ticket.BusStop import BusStop
from Ticket.Ticket import Ticket
from Ticket.TransportZone import TransportZone

if __name__ == '__main__':
    evgen = Person("Кобзев Евгений Васильевич", 4255711245637894, "evgen", "QWERT111", "kobzev@yandex.ru")
    print(evgen.get_info_person())
    bus_stop = BusStop("Воронеж", 40.28, 12.18)
    bus_route = BusRoute("Мосвка-Ростов-на-Дону", 50, 3812)
    place_start = TransportZone(1, 'Москва')
    place_finish = TransportZone(2, 'Ростов-на-Дону')
    ticket = Ticket(1500)
    ticket.set_date("10/12/2023")
    ticket.set_start_zone("Москва")
    ticket.set_finish_zone("Аксай")
    ticket.set_place(10)
    status_baggage = ticket.set_as_luggage(not True)
    ticket.calculate_price_ticket(status_baggage)
    payment = Payment()
    payment.pay_ticket(ticket, evgen)
    payment.date = payment.date.now()

    print(ticket.ticket_info())
    print(payment.date)

