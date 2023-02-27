class HistoryDict:
    my_list = []

    def __init__(self, new_dict: dict):
        self.new_dict = new_dict

    def set_value(self, key, value):
        self.new_dict[key] = value
        self.my_list.append(key)

    def get_history(self):
        return self.my_list

d = HistoryDict({'car': 'Ford'})

d.set_value('city','NYC')
print(d.get_history())

