class Array:

    def __init__(self, arr):
        self.__arr = arr

    def get(self, position):
        return self.__arr[position]

    def append(self, add):
        self.__arr.append(add)
        return self.__arr

    def pop(self):
        self.__arr.pop()
        return self.__arr

    def extend(self, z):
        self.__arr += z
        return self.__arr

    def insert(self, var_loc, new_var):
        self.__arr.insert(var_loc+1, new_var)
        return self.__arr

    def index(self, index):
        x = self.__arr.index(index)
        return x

    def length(self):
        the_length = len(self.__arr)
        return the_length

