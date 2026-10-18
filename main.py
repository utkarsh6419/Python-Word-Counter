"""Count lines, words, and characters in pasted text."""


def main():
    print("Paste text. Enter a blank line when finished.")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    text = "\n".join(lines)
    print(f"Lines: {len(lines)}")
    print(f"Words: {len(text.split())}")
    print(f"Characters: {len(text)}")


if __name__ == "__main__":
    main()
