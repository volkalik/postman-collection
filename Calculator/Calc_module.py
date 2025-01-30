class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Division by zero is not allowed.")

# Пример использования
calc = Calculator()

# Сложение
result_add = calc.add(5, 3)
print("Addition:", result_add)

# Вычитание
result_subtract = calc.subtract(8, 2)
print("Subtraction:", result_subtract)

# Умножение
result_multiply = calc.multiply(4, 6)
print("Multiplication:", result_multiply)

# Деление
try:
    result_divide = calc.divide(10, 2)
    print("Division:", result_divide)
except ValueError as e:
    print("Error:", e)
