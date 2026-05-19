class jar:
    def __init__(self, capacity, cookie_n):
        self.capacity = capacity
        self.cookie_n = cookie_n

    def __str__(self):
        return "🍪" * self.cookie_n
    
    def deposit(self):
        self.cookie_n += 1
        return self.cookie_n
    
    def withdraw(self):
        self.cookie_n -= 1
        return self.cookie_n
    
jar1 = jar(10, 2)
print(jar1)
jar1.deposit()
print(jar1)
jar1.withdraw()
jar1.withdraw()
print(jar1)
