def calculate_max_ones(width, height, sideLength, maxOnes):
    freq = [0] * (sideLength ** 2)
    for i in range(width):
        for j in range(height):
            pos = (i % sideLength) * sideLength + (j % sideLength)
            freq[pos] += 1
    freq.sort(reverse=True)
    return sum(freq[:maxOnes])