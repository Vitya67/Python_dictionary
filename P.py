def frequency_analysis(text):

    words = text.split()


    word_count = {}


    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    word_freq_list = [(count, word) for word, count in word_count.items()]


    word_freq_list.sort(key=lambda x: (-x[0], x[1]))


    for count, word in word_freq_list:
        print(word)


def main():

    text = """hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme"""


    frequency_analysis(text)


if __name__ == "__main__":
    main()
