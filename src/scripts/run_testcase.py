import os
import subprocess
import sys

def parse_input(file_path):
    """
    Parses the input file and extracts variables into a dictionary.
    Handles arrays and other types of inputs like integers or strings.
    """
    with open(file_path, "r") as infile:
        raw_input = infile.read().strip()
    
    inputs = {}
    for part in raw_input.split(","):
        key_value = part.split("=", 1)
        if len(key_value) == 2:
            key, value = key_value[0].strip(), key_value[1].strip()
            # Handle arrays in square brackets
            if value.startswith("[") and value.endswith("]"):
                value = list(map(int, value.strip("[]").split(",")))  # Convert to list of integers
            else:
                try:
                    value = int(value)  # Convert to integer if possible
                except ValueError:
                    value = value.strip('"')  # Otherwise, keep as a string
            inputs[key] = value
    return inputs

def write_temp_input(parsed_input, temp_input_file):
    """
    Writes the parsed input into a temporary file in the required format for the C++ program.
    """
    with open(temp_input_file, "w") as infile:
        for key, value in parsed_input.items():
            if isinstance(value, list):
                infile.write(" ".join(map(str, value)) + "\n")
            else:
                infile.write(str(value) + "\n")

def run_cpp_solution(cpp_executable, temp_input_file, temp_output_file):
    """
    Runs the compiled C++ solution using the temporary input file and captures the output.
    """
    with open(temp_input_file, "r") as infile, open(temp_output_file, "w") as outfile:
        subprocess.run([cpp_executable], stdin=infile, stdout=outfile)

def compare_output(temp_output_file, expected_output_file):
    """
    Compares the output of the C++ solution with the expected output.
    """
    with open(temp_output_file, "r") as outfile, open(expected_output_file, "r") as expected_file:
        actual_output = outfile.read().strip()
        expected_output = expected_file.read().strip()
        return actual_output == expected_output, actual_output, expected_output

def run_test_cases(cpp_executable, testcase_dir):
    """
    Automates running test cases for the C++ solution.
    - cpp_executable: Path to the compiled C++ program.
    - testcase_dir: Directory containing the input and output files.
    """
    # Temporary files for input and output
    temp_input_file = "/tmp/temp_input.txt"
    temp_output_file = "/tmp/temp_output.txt"
    
    print("Running test cases...\n")
    
    # Iterate over test cases in the directory
    for i in range(1, 100):  # Adjust range based on the number of test cases
        input_file = os.path.join(testcase_dir, f"input_{i}.txt")
        output_file = os.path.join(testcase_dir, f"output_{i}.txt")
        
        if not os.path.exists(input_file) or not os.path.exists(output_file):
            break  # Stop when no more test cases are found

        print(f"Running Test Case {i}...")

        # Step 1: Parse input
        parsed_input = parse_input(input_file)

        # Step 2: Write temporary input file
        write_temp_input(parsed_input, temp_input_file)

        # Step 3: Run C++ solution
        run_cpp_solution(cpp_executable, temp_input_file, temp_output_file)

        # Step 4: Compare outputs
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
        print("Usage: python3 automation_script.py <cpp_executable> <testcase_dir>")
        sys.exit(1)

    cpp_executable = sys.argv[1]
    testcase_dir = sys.argv[2]

    run_test_cases(cpp_executable, testcase_dir)
