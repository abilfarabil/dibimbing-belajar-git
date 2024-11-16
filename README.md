# CSV File Reader with Git Implementation

## Overview
This project demonstrates Git workflow implementation and CSV file handling in Python. Created as part of the Data Engineer Bootcamp at Dibimbing, this project showcases version control best practices and basic data handling capabilities.

## Prerequisites
- Python 3.8+
- Git
- Basic understanding of CSV file structure

## Installation & Setup
1. Clone the repository
   ```bash
   git clone https://github.com/[your-username]/dibimbing-belajar-github.git
   ```
2. Navigate to project directory
   ```bash
   cd dibimbing-belajar-github
   ```
3. Run the Python script
   ```bash
   python read_csv.py
   ```

## Project Structure
```
dibimbing-belajar-github/
├── read_csv.py          # Main Python script for CSV reading
├── username.csv         # Sample CSV file
├── images/             # Screenshots directory
│   ├── 1_Membuat_Repository_di_GitHub.png
│   ├── 2_Clone_Repository_ke_Local.png
│   ├── 3_Membuat_File_Python_untuk_Membaca_File_CSV.png
│   ├── 4_Membuat_Branch_Baru.png
│   ├── 5_Commit_dan_Push_File_ke_Branch_Baru.png
│   ├── 6_Membuat_Pull_Request.png
│   └── 7_Pull_Perubahan_dari_Remote_ke_Local.png
└── README.md           # Project documentation
```

## Features
- CSV File Reading: Implements basic CSV file reading functionality
- Git Workflow: Demonstrates complete Git workflow including branching and PR
- Documentation: Includes comprehensive documentation with visual guides

## Implementation Details

### Python Implementation
```python
import csv

def read_csv(filename):
    """
    Reads and displays contents of a CSV file
    
    Parameters:
        filename (str): Path to the CSV file
    
    Returns:
        None: Prints each row of the CSV file
    """
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
```

### Git Workflow Implementation

#### 1. Repository Creation
Created a new GitHub repository named `dibimbing-belajar-github`.
![Screenshot of Repository Creation](images/1_Membuat_Repository_di_GitHub.png)

#### 2. Local Repository Setup
Cloned the repository to local machine.
![Screenshot of Cloning Repository](images/2_Clone_Repository_ke_Local.png)

#### 3. Feature Development
Created Python script for CSV reading functionality.
![Screenshot of Python Code](images/3_Membuat_File_Python_untuk_Membaca_File_CSV.png)

#### 4. Branch Management
Created and switched to feature branch `feature/read_csv`.
![Screenshot of Branch Creation](images/4_Membuat_Branch_Baru.png)

#### 5. Code Integration
Committed and pushed changes to feature branch.
![Screenshot of Commit and Push](images/5_Commit_dan_Push_File_ke_Branch_Baru.png)

#### 6. Pull Request
Created and managed pull request for code review.
![Screenshot of Pull Request](images/6_Membuat_Pull_Request.png)

#### 7. Main Branch Update
Pulled merged changes to local repository.
![Screenshot of Pull Changes](images/7_Pull_Perubahan_dari_Remote_ke_Local.png)

## Best Practices Implemented
1. **Version Control**
   - Proper branch naming (`feature/read_csv`)
   - Meaningful commit messages
   - Pull request workflow

2. **Code Organization**
   - Modular function definition
   - Proper file handling
   - Clear code documentation

3. **Documentation**
   - Visual guides with screenshots
   - Step-by-step instructions
   - Clear project structure

## Technologies Used
- Python 3.8+
- Git 2.x
- CSV Module (Python Standard Library)
- GitHub for version control hosting

## Future Improvements
- Add error handling for file operations
- Implement CSV validation
- Add data processing capabilities
- Include unit tests

## References
- [Git Documentation](https://git-scm.com/doc)
- [Python CSV Documentation](https://docs.python.org/3/library/csv.html)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Python Best Practices](https://www.python.org/dev/peps/pep-0008/)

## Author
Abil Farabil
Data Engineering Bootcamp Student at Dibimbing
