def Generator(file_name, file_mode: 'r'):
    print('Execution is started')
    with open(file_name,file_mode) as file:
        while True:
            yield file.readline().strip()


f = Generator('task11_3.txt', 'r')
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))



