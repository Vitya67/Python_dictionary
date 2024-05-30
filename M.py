def count_votes(input_data):
    vote_counts = {}

    for line in input_data:
        candidate, votes = line.split()
        votes = int(votes)
        if candidate in vote_counts:
            vote_counts[candidate] += votes
        else:
            vote_counts[candidate] = votes

    sorted_candidates = sorted(vote_counts.keys())

    for candidate in sorted_candidates:
        print(f"{candidate} {vote_counts[candidate]}")

def main():
    input_data = [
        "McCain 10",
        "McCain 5",
        "Obama 9",
        "Obama 8",
        "McCain 1",
        "McCain 16",
        "Obama 17"
    ]

    count_votes(input_data)

if __name__ == "__main__":
    main()
