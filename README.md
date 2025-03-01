# LeetCode Solver VS Code Extension

LeetCode Solver is a Visual Studio Code extension designed to streamline your problem-solving workflow by integrating LeetCode directly into your development environment. This extension allows you to fetch test cases for LeetCode problems, view them in a user-friendly interface, and execute your solutions in C++ or Python without leaving VS Code.

## Features

- **Fetch Test Cases**: Automatically retrieve input and output test cases for a given LeetCode problem using its title slug.
- **Webview Display**: Present fetched test cases in an interactive webview within VS Code, enhancing readability and accessibility.
- **Open Solution Files**: Quickly open corresponding C++ (1.cpp) or Python (solution.py) solution files directly from the webview.
- **Run Solutions**: Compile and execute your C++ or Python solutions against the fetched test cases, with results displayed in the webview.

## Prerequisites

- **Python 3**: Ensure that Python 3 is installed on your system and accessible via the command line.
- **G++ Compiler**: For running C++ solutions, the g++ compiler must be installed and available in your system's PATH.

## Installation

1. **Clone the Repository**:

   
bash
   git clone https://github.com/rohitbokare/leetcode-solver.git


2. **Install Dependencies**:

   Navigate to the extension's directory and install the required Node.js packages:

   
bash
   cd leetcode-solver
   npm install


3. **Open in VS Code**:

   Open the extension folder in Visual Studio Code:

   
bash
   code .


4. **Build the Extension**:

   Compile the extension by running:

   
bash
   npm run compile


5. **Launch the Extension**:

   Press F5 to open a new VS Code window with the extension loaded.

## Usage

1. **Activate the Command**:

   Press Ctrl+Shift+P to open the command palette, type Fetch LeetCode Test Cases, and press Enter.

2. **Enter the Title Slug**:

   Input the LeetCode problem's title slug (the URL-friendly version of the problem's title) when prompted.

3. **View Test Cases**:

   The extension will fetch the test cases and display them in a webview panel within VS Code.

4. **Open Solution Files**:

   Use the provided buttons in the webview to open the corresponding C++ (1.cpp) or Python (solution.py) solution files.

5. **Run Solutions**:

   Click the Run C++ File or Run Python File button in the webview to compile and execute your solution against the fetched test cases. The output will be displayed in the webview.

## Extension Structure

- **src/extension.ts**: Contains the main logic for activating the extension, registering commands, and handling interactions between VS Code and the webview.
- **src/scripts/fetch_leetcode.py**: A Python script responsible for fetching test cases from LeetCode based on the provided title slug.
- **src/scripts/run_testcase.py**: A Python script that executes the compiled C++ solution against the test cases and returns the results.
- **src/scripts/run_python.py**: A Python script that runs the Python solution against the test cases and returns the results.

