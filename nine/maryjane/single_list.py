class SingleList(list):


    def __init__(self, initialList=None):

        list.__init__(self)

        if initialList:
            self.merge(initialList)

    def raiseIfNotUnique (self, value):

        if value in self:
            raise ValueError

    def __setitem__(self, key, value):
        self.raiseIfNotUnique(value)

    def __add__(self, other):
        return SingleList(list.__add__(self, other))
