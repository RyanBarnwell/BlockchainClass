#Ryan Barnwell
#Overtake

import math

def poisson_probability(lambda_, k):
    return (lambda_**k * math.exp(-lambda_)) / math.factorial(k)

def lambdaFind(p, q, z):
    return z*(q/p)

def successProbability(q, z):
    p = 1 - q
    lambda_ = lambdaFind(p, q, z)
    sum = 0
    #+1 accounts for 0, +2 for overtake
    for k in range(z + 2):
        lambdaMath = poisson_probability(lambda_, k)
        #+1 for overtake
        prob = 1 - (q / p) ** ((z+1) - k) 
        sum += lambdaMath * prob
    
    return 1 - sum

q = float(input("Enter attacker mining power(ie: 0.32): "))
z = int(input("Enter number of blocks: "))

probability = str(successProbability(q, z))
print("Probability of a successful attack: " + probability)