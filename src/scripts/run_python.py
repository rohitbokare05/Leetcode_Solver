import os
import subprocess
import sys

def write_temp_input(input_file, temp_input_file):
    """
    Copies the content of the input file directly into a temporary input file.
    """
    with open(input_file, "r") as infile, open(temp_input_file, "w") as temp_infile:
        temp_infile.write(infile.read())

def run_python_solution(python_file, temp_input_file, temp_output_file):
    """
    Runs the Python solution using the temporary input file and captures the output.
    """
    with open(temp_input_file, "r") as infile, open(temp_output_file, "w") as outfile:
        subprocess.run(["python3", python_file], stdin=infile, stdout=outfile)

def compare_output(temp_output_file, expected_output_file):
    """
    Compares the output of the Python solution with the expected output.
    """
    with open(temp_output_file, "r") as outfile, open(expected_output_file, "r") as expected_file:
        actual_output = outfile.read().strip()
        expected_output = expected_file.read().strip()
        return actual_output == expected_output, actual_output, expected_output

def run_test_cases(python_file, testcase_dir):
    """
    Automates running test cases for the Python solution.
    - python_file: Path to the Python program.
    - testcase_dir: Directory containing the input and output files.
    """
    # Temporary files for input and output
    temp_input_file = "/tmp/temp_input.txt"
    temp_output_file = "/tmp/temp_output.txt"

    for i in range(1, 100):  # Adjust range based on the number of test cases
        input_file = os.path.join(testcase_dir, f"input_{i}.txt")
        output_file = os.path.join(testcase_dir, f"output_{i}.txt")
        
        if not os.path.exists(input_file) or not os.path.exists(output_file):
            break  # Stop if files are not found

        # Step 1: Write temporary input file
        write_temp_input(input_file, temp_input_file)

        # Step 2: Run Python solution
        run_python_solution(python_file, temp_input_file, temp_output_file)

        # Step 3: Compare outputs
        is_correct, actual_output, expected_output = compare_output(temp_output_file, output_file)
        
        # Display results
        if is_correct:
            print(f"Test Case {i}: PASSED")
        else:
            print(f"Test Case {i}: FAILED")
            print(f"  Expected Output: {expected_output}")
            print(f"  Actual Output: {actual_output}")
            print()
    
    print("Test cases execution completed.")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 automation_script.py <python_file> <testcase_dir>")
        sys.exit(1)

    python_file = sys.argv[1]
    testcase_dir = sys.argv[2]

    run_test_cases(python_file, testcase_dir)
