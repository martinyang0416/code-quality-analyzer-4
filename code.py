def brokenCalc(X, Y):
    steps = 0
    while Y > X:
        if Y % 2:
            Y += 1
            steps += 1
        Y //= 2
        steps += 1
    return steps + (X - Y)