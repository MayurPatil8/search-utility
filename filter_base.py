class FilterBase(object):
    __initiated = False
    def __init__(self):
        self.fields = {}
        self.__initiated = True


    def __setattr__(self, key, value):

        if self.__initiated:
            key = key.lower()
            if key == "match":
                #import pdb;pdb.set_trace()
                pass
            self.fields[key]=value
        else:
            super(FilterBase, self).__setattr__(key,value)

    def __repr__(self):
        return "{ " + ", ".join(['\"'+key+'\": ' + repr(value) for key, value in self.fields.items()])+"}"
