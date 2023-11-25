class TransportZone:

    def __init__(self, id, remark):
        self.id = id
        self.remark = remark

    def get_remark(self):
        return self.remark

    def get_id(self):
        return self.id

    def set_remark(self, new_remark):
        self.remark = new_remark
