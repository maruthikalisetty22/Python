def count_primes(n):
    prime_lst = []
    
    for num in range(2, n+1):
        is_prime  = True 
        for i in range(2, int(num**0.5) + 1):
            if num % 2 == 0:
                is_prime = False
                break
        if is_prime == True:
            prime_lst.append(num)
    print(f"Prime numbers up to {n}: {prime_lst}")
    print(f"Total prime count: {len(prime_lst)}")
        

n = 30        
count_primes(n)
