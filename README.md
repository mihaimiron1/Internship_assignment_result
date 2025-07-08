# 📝 Anagram Finder


## 🚀 How It Works

The program uses a **dictionary**, where:
- The **key** is the word sorted alphabetically (e.g. `"care"` -> `"acer"`).
- The **value** is a list of words that share this key, meaning they are anagrams.

This way, all anagrams end up grouped under the same key.

---

## ⚙️ Design & Complexity

- Sorting each word takes **O(k log k)** where *k* is the word length.
- Inserting into the dictionary is **O(1)** on average.
- Processing is linear in the number of words, plus the small cost of sorting each word.

---

## 🏗 Scalability

- ✅ For **10 million words**:  
  Should work directly in memory on most machines (~500MB-1GB RAM estimated).

- 🚀 For **100 billion words**:  
  Would require a distributed solution, such as:
  - **MapReduce**, mapping each word to `(sorted_key, word)` and reducing by key.
  - Tools like **Apache Hadoop** or **Apache Spark** would be ideal.

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

## 💡 Why This Approach?

✅ Simple, clean and easy to maintain.

✅ Efficient: good performance even for millions of words.

✅ Easily extendable to distributed systems if needed.


