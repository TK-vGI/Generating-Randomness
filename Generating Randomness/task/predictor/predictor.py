MIN_LENGTH = 100
START_MESSAGE = (
    "Please provide AI some data to learn...\n"
    "The current data length is 0, 100 symbols left"
)

GAME_INTRO = (
    "\nYou have $1000. Every time the system successfully predicts your next press, you lose $1.\n"
    "Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!\n"
)


def process_input(raw: str) -> list[str]:
    """Return only the characters '0' and '1' from the raw input."""
    return [ch for ch in raw if ch in ('0', '1')]


def count_triads(data: str) -> dict[str, list[int]]:
    """
    Count how many times each triad (000–111) is followed by 0 or 1.
    Returns a dict: triad -> (count_0, count_1)
    """

    # Initialize all triads with zero counts
    triads = {format(i, "03b"): [0, 0] for i in range(8)}

    # Iterate through data and count followers
    for i in range(len(data) - 3):
        triad = data[i:i + 3]
        follower = data[i + 3]

        if triad in triads:
            if follower == "0":
                triads[triad][0] += 1
            elif follower == "1":
                triads[triad][1] += 1

        # triads[triad][int(follower)] += 1 # this can be used instead

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


def predict_sequence(test: str, model: dict[str, list[int]]) -> str:
    """Generate prediction string based on triad statistics."""
    prediction = test[:3]  # keep first 3 characters unchanged

    # Iterate through test input data and predict followers
    for i in range(len(test) - 3):
        triad = test[i:i + 3]
        count_0, count_1 = model[triad]

        if count_0 > count_1:
            next_bit = '0'
        elif count_1 > count_0:
            next_bit = '1'
        else:
            # equal counts → random choice
            next_bit = random.choice(['0', '1'])

        prediction += next_bit

    return prediction


def evaluate_prediction(test: str, prediction: str) -> tuple[int, int, int, float]:
    """Compare predicted vs actual (excluding first 3 chars)."""
    actual = test[3:]
    predicted = prediction[3:]

    total = len(actual)
    correct = sum(1 for a, p in zip(actual, predicted) if a == p)
    accuracy = round(correct / total * 100, 2)
    wrong = total - correct

    return correct, wrong, total, accuracy


def collect_training_data() -> str:
    """Stage 1 logic: collect ≥100 bits from user."""
    data: list[str] = []

    while len(data) < MIN_LENGTH:
        print("Print a random string containing 0 or 1:\n")
        user_input = input().strip()

        filtered = process_input(user_input)
        data.extend(filtered)

        current = len(data)
        if current < MIN_LENGTH:
            print(f"The current data length is {current}, {MIN_LENGTH - current} symbols left")

    final = "".join(data)
    print("\nFinal data string:")
    print(final)
    return final


def get_game_input() -> str:
    """
    Ask user for a valid game string (≥4 bits) or 'enough'.
    If invalid input, loop again silently
    """
    while True:
        print("\nPrint a random string containing 0 or 1:\n")
        raw = input().strip()

        if raw == "enough":
            return "enough"

        filtered = "".join(process_input(raw))

        if len(filtered) >= 4:
            return filtered


def main():
    print(START_MESSAGE)

    training_data = collect_training_data()
    triad_model = count_triads(training_data)

    print(GAME_INTRO)

    balance = 1000

    while True:
        test_string = get_game_input()
        if test_string == "enough":
            break

        prediction = predict_sequence(test_string, triad_model)

        print("predictions:")
        print(prediction[3:])

        correct, wrong, total, accuracy = evaluate_prediction(test_string, prediction)
        balance += (wrong - correct)

        print(f"\nComputer guessed right {correct} out of {total} symbols right ({accuracy} %)")
        print(f"Your balance is now ${balance})")

        # # Update model with new data AFTER prediction
        # triad_model = count_triads(training_data + test_string)

    print("Game over!")


if __name__ == "__main__":
    import random

    main()
