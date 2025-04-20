from class_Stack import Stack

class TestStack:
    def setup_method(self):
        self.stack = Stack()
        self.stack.is_empty()
        self.stack.push('table')
        self.stack.push('floor')
        self.stack.pop()
        self.stack.peek()
        self.stack.size()

    def tear_down(self):
        self.stack()

    def test_create_empty_stack(self):
        stack = Stack()
        assert stack.is_empty() == True

    def push_stack_method(self):
        assert len(self.stack()) == 2

    def pop_stack_method(self):
        assert self.stack.pop() == 'floor'

    def peek_stack_method(self):
        assert self.stack.peek() == 'table'

    def size_stack_method(self):
        assert self.stack.size() == 2




