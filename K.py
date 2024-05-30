def count_word_occurrences(text):

    words = text.split()


    word_count = {}
    results = []


    for word in words:
        if word not in word_count:
            word_count[word] = 0
        results.append(word_count[word])
        word_count[word] += 1

    return results

def main():
    text = """one two one two three
    She sells sea shells on the sea shore;
    The shells that she sells are sea shells I'm sure.
    So if she sells sea shells on the sea shore,
    I'm sure that the shells are sea shore shells."""

    result = count_word_occurrences(text)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
