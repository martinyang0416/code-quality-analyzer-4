def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"
    
    num1_reversed = num1[::-1]
    num2_reversed = num2[::-1]
    len1, len2 = len(num1_reversed), len(num2_reversed)
    result = [0] * (len1 + len2)
    
    # Multiply each digit and accumulate the result
    for i in range(len1):
        for j in range(len2):
            digit1 = int(num1_reversed[i])
            digit2 = int(num2_reversed[j])
            result[i + j] += digit1 * digit2
   