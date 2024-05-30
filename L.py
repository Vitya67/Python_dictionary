def find_synonym(pairs, word):
    synonym_dict = {}

    for word1, word2 in pairs:
        synonym_dict[word1] = word2
        synonym_dict[word2] = word1

    return synonym_dict.get(word, )

def main():
    n = int(input())
    pairs = []

    for _ in range(n):
        pair = input().split()
        pairs.append((pair[0], pair[1]))

    word = input()


    synonym = find_synonym(pairs, word)
    print(synonym)

if __name__ == "__main__":
    main()
