# 📝 Anagram Finder


## 🚀 How It Works

The program uses a **dictionary**, where:
- The **key** is the word sorted alphabetically (e.g. `"care"` -> `"acer"`).
- The **value** is a list of words that share this key, meaning they are anagrams.

This way, all anagrams end up grouped under the same key.

---


## 📂 Usage

### 1️⃣ Prerequisites
- Python 3.x installed on your system.

### 2️⃣ Prepare input file
Place a file named `sample.txt` in the same directory, with one word per line:
```
act

cat

tree

race

care

acre

bee
```


### 3️⃣ Run the program
Run it from terminal / command prompt:

```bash
python anagram_finder.py
```
```
act cat

tree

acre care race

bee

```

## 🚫 No External Libraries

This project is implemented using only Python’s standard library.
It does not rely on any external packages.



