from collections import Counter

def generate_ngrams(text, n):
    text = text.replace(" ", "").upper()
    return [text[i:i+n] for i in range(len(text) - n + 1)]

def ngram_frequencies(text, n):
    ngrams = generate_ngrams(text, n)
    freq = Counter(ngrams)
    return freq

print("N-Gram Frequency Analysis")
message = input("Enter the text: ")
n = int(input("Enter the N for N-gram: "))

frequencies = ngram_frequencies(message, n)
print(f"\nTop {n}-grams:")
for gram, count in frequencies.most_common():
    print(f"{gram} : {count}")
