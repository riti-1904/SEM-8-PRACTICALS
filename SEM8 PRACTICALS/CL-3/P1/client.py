import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Get input from user
n = int(input("Enter a non-negative integer: "))

# Call the remote factorial method
result = proxy.factorial(n)

print(f"Factorial of {n} is {result}")
