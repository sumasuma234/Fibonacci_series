def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

num_terms = int(input("Enter the number of terms: "))

fibonacci(num_terms)