n, m = map(int, input().split())
w = list(map(int, input().split()))
b = list(map(int, input().split()))

last_occurrence = {book: -1 for book in range(1, n + 1)}
for idx in range(m):
    book = b[idx]
    last_occurrence[book] = idx  # Using zero-based index for ordering

# Sort books by their last occurrence in ascending order
sorted_books = sorted(range(1, n + 1), key=lambda x: last_occurrence[x])

stack = sorted_books.copy()
total = 0

for book in b:
    index = stack.index(book)
    # Calcu