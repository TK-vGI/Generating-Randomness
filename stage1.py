MIN_LENGTH = 100

def process_input(raw: str) -> list[str]:
    """Return only the characters '0' and '1' from the raw input."""
    return [ch for ch in raw if ch in ('0', '1')]

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

if __name__ == "__main__":
    main()