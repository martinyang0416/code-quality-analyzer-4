def maxScoreWords(words, letters, score):
    from collections import defaultdict

    # Precompute the count of each letter available
    letters_count = [0] * 26
    for c in letters:
        letters_count[ord(c) - ord('a')] += 1

    # Precompute the count of each character for every word
    word_counts = []
    for word in words:
        cnt = [0] * 26
        for c in word:
            cnt[ord(c) - ord('a')] += 1
        word_counts.append(cnt)

    max_score = 0
    n = len(words)
    # I