from datetime import datetime

from Ticket.BusRoute import BusRoute
from Ticket.TransportZone import TransportZone


class Ticket:
    def __init__(self, price):
        self.price = price
        self.date = datetime
        self.start_zone = TransportZone
        self.finish_zone = TransportZone
        self.as_luggage = bool
        self.place = int
        self.road_number = BusRoute

    def get_price(self):
        return self.price

    def get_date(self):
        return self.date

    def get_start_zone(self):
        return self.start_zone

    def get_finish_zone(self):
        return self.finish_zone

    def get_as_luggage(self):
        return self.as_luggage

    def get_place(self):
        return self.place

    def get_road_number(self):
        return self.road_number

    def set_price(self, new_price):
        self.price = new_price

    def set_date(self, new_date):
        self.date=new_date


    def set_start_zone(self, new_start_zone):
        self.start_zone = new_start_zone

    def set_finish_zone(self, new_finish_zone):
        self.finish_zone = new_finish_zone

    def set_as_luggage(self, new_status_as_luggage):
        self.as_luggage = new_status_as_luggage

    def set_place(self, new_place):
        self.place = new_place

    def set_road_number(self, new_road_number):
        self.road_number = new_road_number

    def calculate_price_ticket(self, as_luggage):
        a = True
        if as_luggage == a:
            return  self.set_price(self.price * 2)
        else:
            return self.price

    def ticket_info(self):
        return f"Дата отправления:{self.date}\n" \
               f"Место посадки: {self.start_zone}\n" \
               f"Место высадки: {self.finish_zone}\n" \
               f"Место: {self.place}\n" \
               f"Багаж есть/нет: {self.as_luggage}\n" \
               f"Цена билета: {self.price}"
