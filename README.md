
# 📊 University Progression Predictor  
**Predict student outcomes with Python!**  
![Progress Tracker](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcW0yY3V6eGJtN3RlY2R6dGJ6c2V6Y2V4eWZ1bGJ6eGZqZ2N6eGZqZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKTDn976uzZh40s/giphy.gif) *(Replace with your GIF link)*  

---

## 🚀 **Features**  
| Feature | Emoji | Description |
|---------|-------|-------------|
| **Progression Prediction** | 🔍 | Determines outcomes: `Progress`, `Trailer`, `Retriever`, or `Exclude`. |
| **Input Validation** | ✅ | Checks for valid integers, credit ranges, and totals. |
| **Multiple Entries** | 🔄 | Processes data until user quits (`q`). |
| **Histogram** | 📈 | Visualizes results using `graphics.py`. |
| **Data Storage** | 💾 | Saves to **lists** (Part 2) and **text files** (Part 3). |

---

## 🛠️ **Setup**  
1. **Clone the repo**:  
   ```bash
   git clone https://github.com/your-username/university-progression-predictor.git
   ```
2. **Install dependencies**:  
   - Ensure `graphics.py` is in the same directory.  
   - Python 3.x required.  

3. **Run the program**:  
   ```bash
   python w2053121_part1_3.py
   ```

---

## 🎥 **Demo**  
![Program Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcW0yY3V6eGJtN3RlY2R6dGJ6c2V6Y2V4eWZ1bGJ6eGZqZ2N6eGZqZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JIX9t2j0ZTN9S/giphy.gif) *(Replace with a screencast GIF of your program running)*  

**Example Output**:  
```plaintext
Please Enter Your Credit At Pass: 120  
Progress  

Would you like to enter another set of data?  
Enter 'y' for yes or 'q' to quit: q  

📊 Histogram Results...  
Part 2:  
Progress - 120, 0, 0  
Part 3 data saved to file!  
```

---

## 📂 **Project Structure**  
```
.
├── w2053121_part1_3.py    # Main program (replace with your ID)
├── graphics.py            # Required for histogram
├── Part 3.txt             # Auto-generated output (Part 3)
└── README.md              # You're here! 😄
```

---

## 🔍 **How It Works**  
1. **Input Validation**:  
   - 🔢 Credits must be in `[0, 20, 40, 60, 80, 100, 120]`.  
   - ❌ Rejects strings, out-of-range values, or incorrect totals.  

2. **Outcome Logic**:  
   ```python
   if pass_credit == 120:  
       print("Progress")  
   elif fail_credit >= 80:  
       print("Exclude")  
   ```

3. **Data Storage**:  
   - **List**: Stores inputs for Part 2.  
   - **Text File**: Writes outputs for Part 3.  

4. **Histogram**:  
   - Uses `graphics.py` to show student distribution.  

---
