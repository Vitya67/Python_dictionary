def most_frequent_word(text):
    words = text.split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_frequent = None
    max_count = 0

    for word in word_count:
        if word_count[word] > max_count or (word_count[word] == max_count and word < most_frequent):
            most_frequent = word
            max_count = word_count[word]

    return most_frequent


def main():

    text = "apple orange banana banana orange"


    result = most_frequent_word(text)
    print(result)


if __name__ == "__main__":
    main()
