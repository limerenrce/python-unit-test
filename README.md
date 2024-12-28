# Sorting Algorithms Project

This project implements and tests two sorting algorithms: **Merge Sort** and **Quick Sort**.

## Directory Structure

project_name/
│
├── src/ # Source code directory
│ ├── **init**.py # Marks this directory as a Python package
│ ├── algorithms/ # Directory for algorithms
│ │ ├── **init**.py
│ │ ├── merge_sort.py
│ │ └── quick_sort.py
│ ├── tests/ # Directory for unit tests
│ │ ├── **init**.py
│ │ ├── test_merge_sort.py
│ │ └── test_quick_sort.py
│ └── utils/ # Utility functions (if needed)
│ ├── **init**.py
│ └── test_helpers.py
│
├── data/ # Sample data files for testing
│ ├── sample_input.txt
│ └── expected_output.txt
│
├── docs/ # Documentation
│ └── report.md
│
├── .gitignore # Git ignore file for version control
├── requirements.txt # Dependencies
├── README.md # Project overview
└── setup.py # For packaging and installation

## Run Tests

To execute unit tests:

```bash
python -m unittest discover -s src/tests -p "test_*.py"
```

---

### 9. **File: `setup.py`**

_(Optional for making your project installable.)_

```python
from setuptools import setup, find_packages

setup(
    name="sorting_algorithms",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="Implementation of sorting algorithms with unit tests",
    author="Your Name",
    install_requires=[],
)
```
