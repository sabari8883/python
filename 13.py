def generate_pythagorean_triplets(limit):
    triplets = []
    for n in range(1, limit):
        for m in range(n + 1, limit):
            a = m**2 - n**2
            b = 2 * n * m
            c = m**2 + n**2
            if c <= limit:
                triplets.append((a, b, c))
    return triplets

upper_limit = int(input("Enter upper limit: "))

triplets = generate_pythagorean_triplets(upper_limit)

if triplets:
    print("Pythagorean Triplets:")
    for triplet in triplets:
        print(triplet)
else:
    print("No Pythagorean Triplets found within the given limit.")
