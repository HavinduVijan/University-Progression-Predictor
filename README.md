
# 📊 University Progression Predictor  

** This Python program is designed to predict the progression outcomes for university students at the end of an academic year, based on their credits at pass, defer, and fail levels. The program adheres to specific university regulations to determine outcomes such as Progress, Progress (module trailer), Module Retriever, or Exclude.**

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
