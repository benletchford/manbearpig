class Something():
    MESSAGE = 'Hello there, {name}!'

    def __init__(self, name):
        self.name = name

    def greet(self):
        return Something.MESSAGE.format(**{'name': self.name})
