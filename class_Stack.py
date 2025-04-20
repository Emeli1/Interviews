
class Stack(list):
    def is_empty(self):
        return len(self) == 0

    def push(self, el):
        self.append(el)

    def pop(self):
        if not self.is_empty():
            el = self[-1]
            self.__delitem__(-1)
            return el

    def peek(self):
        el = self[-1]
        return el

    def size(self):
        return len(self)

