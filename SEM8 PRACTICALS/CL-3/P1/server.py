from xmlrpc.server import SimpleXMLRPCServer

# Define the factorial function
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")

# Register the factorial function
server.register_function(factorial, "factorial")

# Run the server forever
server.serve_forever()
