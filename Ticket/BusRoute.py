from Ticket.BusStop import BusStop


class BusRoute:

    def __init__(self, remark, capacity, id):
        self.id = id
        self.remark = remark
        self.capacity = capacity
        self.bus_stop = [BusStop]

    def get_id(self):
        return self.id

    def get_remark(self):
        return self.remark

    def get_capacity(self):
        return self.capacity

    def get_bus_stop(self):
        return self.bus_stop

    def set_remark(self, new_remark):
        self.remark = new_remark

    def set_capacity(self, new_capacity):
        self.capacity = new_capacity

    def set_bus_stop(self, new_bus_stop=[BusStop]):
        self.bus_stop = new_bus_stop
