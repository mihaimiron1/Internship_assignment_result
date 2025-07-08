# 📝 Design Decisions - Anagram Finder


## ⚙️ Data Structure & Algorithm

### 📌 Approach
- The solution uses a **Python dictionary (`dict`)**, where:
  - The **key** is the sorted characters of the word (e.g. `"care"` → `"acer"`).
  - The **value** is a list of words that match this key.

This ensures that all words that are anagrams (same letters in any order) are grouped under the same key.

### 🚀 Example
| Word | Sorted Key | Dict Entry |
|------|------------|------------|
| care | acer       | acer: [care] |
| race | acer       | acer: [care, race] |
| acre | acer       | acer: [care, race, acre] |

---

## ⏱ Performance & Complexity

### 🔬 Complexity
- Sorting each word takes **O(k log k)** where *k* is the length of the word.
- Inserting into the dictionary is **O(1)** on average.
- Overall complexity for *n* words:  **O(n * k log k)**

This is very efficient and easily handles millions of words on modern hardware.

### 🔧 Maintainability
- The solution is straightforward, with minimal code and no hidden complexities.
- Easy to extend or debug because it relies on Python's built-in data structures.

---

## 🚀 Scalability Considerations

### ✅ 10 million words
- The current implementation will run comfortably in memory on most modern machines.
- Estimated memory usage: **~500MB-1GB RAM**, depending on average word length.

### 🌐 100 billion words
For datasets this large, a single machine will not be feasible.  
We would need to use a **distributed system**, such as:

- **MapReduce (Hadoop / Spark):**
- **Map phase:** emit (sorted_key, word).
- **Shuffle & Reduce phase:** group by sorted_key.
- This allows parallel processing across many nodes, handling massive datasets efficiently.

---

## ❌ External Libraries

- ✅ This project uses **only Python’s standard library**.
- No third-party dependencies are required.  
- This makes the code portable and easy to run on any system with Python installed.

---

## 💡 Why This Solution?

- 🧩 **Simplicity:** minimal, clear logic, easy to read and maintain.
- 🚀 **Speed:** dictionary lookups and insertions are fast.
- 📈 **Scalability:** can transition to distributed approaches with the same core idea (mapping by sorted key).

---

## 🔗 Future Improvements

- Support reading input in a streaming fashion (line by line) to reduce memory usage for very large files.
- Export grouped anagrams directly to disk in batches, to handle cases where the final dictionary is too large for memory.
- Add multi-threading or asynchronous IO for faster disk operations on large datasets.

---

✅ **Conclusion:**  
This solution balances **simplicity, performance, and scalability**, making it a solid choice for both small scripts and potential expansion into big data processing.

