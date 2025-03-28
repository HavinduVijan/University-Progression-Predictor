# University Progression Predictor

A Python program to predict student progression outcomes based on credit inputs, with validation, looping, histogram visualization, and data storage capabilities.

## Features
1. **Progression Prediction**: Determines outcomes (Progress, Trailer, Retriever, Exclude) per university regulations.
2. **Input Validation**: Checks for:
   - Integer inputs.
   - Valid credit ranges (0, 20, 40, 60, 80, 100, 120).
   - Total credits = 120.
3. **Multiple Entries**: Processes data for multiple students until user quits (`q`).
4. **Histogram**: Visualizes results using `graphics.py`.
5. **Data Storage**:
   - **List**: Stores and displays input data (Part 2).
   - **Text File**: Saves and retrieves data (Part 3).

## Requirements
- Python 3.x
- `graphics.py` module (included in the repository).

## Usage
1. Run the program:  
   ```bash
   python student_id.py
   ```
2. Follow prompts to enter credits (pass, defer, fail).
3. Enter `q` to quit and view the histogram/stored data.

## Project Structure
- `student_id.py`: Main program file (replace `student_id` with your ID).
- `test_cases.docx`: Test plan/results (submitted separately).
- `progression_data.txt`: Output file for Part 3 (auto-generated).
