def main():
    s = input().strip()
    vowels = {'A', 'E', 'I', 'O', 'U'}
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    print("YES" if count % 2 != 0 else "NO")

if __name__ == "__main__":
    main()