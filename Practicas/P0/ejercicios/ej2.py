# Function to find the nth Fibonacci number
def fib(n):

	if n <= 1:
		return n

	return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':

    input = open('./inputej2.txt','r')
    n = int(input.read())
    input.close()

    output = open('./outputej2.txt','w')
    
    resultado = str(fib(n))
    print(resultado)
    output.write(resultado)
    output.close()