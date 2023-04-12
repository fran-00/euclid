def disuguaglianza_triangolare(a: int, b: int, c: int):
    
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

a, b, c = map(int, input("Inserisci tre numeri separati da uno spazio: ").split())

print(disuguaglianza_triangolare(4, 5, 6))