import random

words = ["life", "universe", "everything", "banana", "pie", "computer", "algorithm", "random", "quote", "code"]

def generate_quote():
    
    quote = " ".join(random.choice(words) for _ in range(5))
    return quote


print(generate_quote())
