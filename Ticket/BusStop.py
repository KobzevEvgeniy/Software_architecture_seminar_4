class BusStop:
    def __init__(self, name, attitude, lattitude):
        self.id = id
        self.name = name
        self.attitude = attitude
        self.lattitude = lattitude

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_attitude(self):
        return self.attitude

    def get_lattitude(self):
        return self.lattitude

    def set_name_bus_stop(self, new_name):
        self.name = new_name

    def set_attitude(self, new_attitude):
        self.attitude = new_attitude

    def set_latiitude(self, new_lattitude):
        self.lattitude=new_lattitude
