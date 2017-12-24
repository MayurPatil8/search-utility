from ast import literal_eval
class BaseList(object):
    def __init__(self):
        self.List = list()
    def add(self, ele):
        self.List.append(ele)

    def __repr__(self):
        return "["+", ".join([repr(ele) for ele in self.List ]) +"]"