example_num = 0

def start_theme(name):
    print('*' * 30 + name + '*' * 30)
    global example_num
    example_num = 0 

def start_example(doc):
    global example_num
    example_num += 1
    print(f'EXAMPLE {example_num}: {doc}')

def end_example():
    print()

