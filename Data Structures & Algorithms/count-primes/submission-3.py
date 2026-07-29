class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Create a boolean array of size n, initialized to True
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False # 0 and 1 are not primes
        
        # We only need to check up to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Cross out all multiples of the current prime
                for j in range(i * i, n, i):
                    is_prime[j] = False
                    
        # The number of True values left is the number of primes
        return sum(is_prime)
        
        