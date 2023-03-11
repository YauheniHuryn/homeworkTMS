class OpenFile:
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        self.file = open(self.file_name, self.file_mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with OpenFile('test11.txt', 'w+') as test:
    test.write('hello, i am Yauhen')