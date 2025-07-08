file_path = "sample.txt"
anagrams = {}

with open(file_path, "r") as file:
    content = file.read()
    content = content.split("\n")
    for line in content:
        new_word = ''.join(sorted(line))

        if new_word in anagrams:
            anagrams[new_word].append(line)
        else:
            anagrams[new_word] = [line]
        
    for group in anagrams.values():
        print(' '.join(group))
        
     