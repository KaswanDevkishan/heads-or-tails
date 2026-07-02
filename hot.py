import random

def toss():
    return random.choice(["Heads", "Tails"])

def main():
    print("Tossing a coin...")
    heads = 0
    tails = 0
    for round_num in range(1, 4):
        result = toss()
        print(f"Round {round_num}: {result}")
        if result == "Heads":
            heads += 1
        else:
            tails += 1
    print(f"Heads: {heads}, Tails: {tails}")
    if heads > tails:
        print("You won")
    else:
        print("You lost")

if __name__ == "__main__":
    main()
