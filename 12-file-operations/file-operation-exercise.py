words_dict = {}
with open("data/exercise.txt") as f:
    for i, line in enumerate(f):
        if i == 0:
            continue
        clean_line = line.rstrip()
        clean_line = clean_line.lower()
        for char in (".", ",", "!", "?"):
            clean_line = clean_line.replace(char, "")
        words = clean_line.split(" ")
        for word in words:
            if words_dict.get(word) is not None:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

with open("data/result.txt", "w+") as f:
    for word in words_dict:
        f.write(f"word{word} occurred {words_dict[word]} times\n")