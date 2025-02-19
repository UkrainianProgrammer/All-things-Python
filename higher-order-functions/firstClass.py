# assigning a function to a variable
def greet(n):
    return f"Hello, {n}!"

sayHi = greet
print(sayHi("Alice"))

# passing a function as an argument
def apply(f, v):
    return f(v)

res = apply(sayHi, "Bob")
print(res)

# returning a function from another function
def makeMult(f):
    def mult(v):
        return f * v
    return mult

double = makeMult(2)
print(double(5))