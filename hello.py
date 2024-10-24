def print_hello(value: str)  -> str:
    if isinstance(value, str):
        return f'Hello, {value}'
    else:
        return 'this is not string.'


if  __name__=='__main__':
    result = print_hello('Jhon')
    print(result)
    
