import operation

def run_operation(opertype):
    operation.check_bd()
    if opertype == '1':
        operation.show()
    elif opertype == '2':
        operation.add(operation.getinfo())
    elif opertype == '3':
        operation.search()
    else:
        print('Invalid operation')