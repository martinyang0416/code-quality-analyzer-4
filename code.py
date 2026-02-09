def main():
    s = input().strip()
    vowels = {'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    print("YES" if count == 2 else "NO")

if __name__ == "__main__":
    main()