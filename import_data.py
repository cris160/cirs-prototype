from datasets import load_dataset


ds = load_dataset("roneneldan/TinyStories", split="train")


with open("tinystories.txt", "w", encoding="utf-8") as f:
    for item in ds:
        f.write(item["text"] + "\n")
with open("tinystories.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"Number of lines written: {len(lines)}")
    print(f"First line: {lines[0]}")