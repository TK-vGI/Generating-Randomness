MIN_LENGTH = 100

def process_input(raw: str) -> list[str]:
    """Return only the characters '0' and '1' from the raw input."""
    return [ch for ch in raw if ch in ('0', '1')]

def count_triads(data: str) -> dict[str, list[int]]:
    """
    Count how many times each triad (000–111) is followed by 0 or 1.
    Returns a dict: triad -> (count_0, count_1)
    """

    # Initialize all triads with zero counts
    # triads = {format(i, "03b"): [0, 0] for i in range(8)}
    triads = {'000': [0, 0],
              '001': [0, 0],
              '010': [0, 0],
              '011': [0, 0],
              '100': [0, 0],
              '101': [0, 0],
              '110': [0, 0],
              '111': [0, 0]}

    # Iterate through data and count followers
    for i in range(len(data) - 3):
        triad = data[i:i+3]
        follower = data[i+3]

        if triad in triads:
            if follower == "0":
                triads[triad][0] += 1
            elif follower == "1":
                triads[triad][1] += 1

    return triads

def print_triads(triad_counts: dict[str, list[int]]):
    """
    Print triad counts in ascending decimal order.
    """
    print()
    for i in range(8):
        triad = format(i, "03b")
        count_0, count_1 = triad_counts[triad]
        print(f"{triad}: {count_0},{count_1}")

def main():
    data: list[str] = []

    while len(data) < MIN_LENGTH:
        print("Print a random string containing 0 or 1:\n")
        user_input = input().strip()

        filtered = process_input(user_input)
        data.extend(filtered)

        current_len = len(data)
        if current_len < MIN_LENGTH:
            remaining = MIN_LENGTH - current_len
            print(f"Current data length is {current_len}, {remaining} symbols left")

    final_string = "".join(data)
    print("\nFinal data string:")
    print(final_string)

    triad_counts = count_triads(final_string)
    print_triads(triad_counts)

if __name__ == "__main__":
    main()