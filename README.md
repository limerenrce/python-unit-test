# Sorting Algorithms Project

This project implements and tests two sorting algorithms: **Merge Sort** and **Quick Sort**.

## Directory Structure

project_name/
```
│
├── src/ # Source code directory
│ ├── **init**.py
│ ├── algorithms/
│ │ ├── **init**.py
│ │ ├── merge_sort.py
│ │ └── quick_sort.py
│ ├── tests/
│ │ ├── **init**.py
│ │ ├── test_merge_sort.py
│ │ └── test_quick_sort.py
│ └── utils/
│ ├── **init**.py
│ └── test_helpers.py
│
├── .gitignore # Git ignore file for version control
├── requirements.txt # Dependencies
├── README.md # Project overview
└── setup.py # For packaging and installation
```

## Run Tests

To execute unit tests:

```bash
python -m unittest discover -s src/tests -p "test_*.py"
```

---
