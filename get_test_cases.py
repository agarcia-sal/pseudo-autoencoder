import logging 
import subprocess
import os
import re
import time
import shutil
from pathlib import Path

code = ''

ROOT_DIR = os.getcwd()
logging.basicConfig(level=logging.INFO)

def make_directory(run_scripts_path):
    # Define the path for the new directory
    path = Path(run_scripts_path) # run_scripts_path is the new directory
    # Create the directory
    path.mkdir(parents=True, exist_ok=True)  # 'parents=True' creates any necessary parent directories
    print(f"Directory '{path}' created successfully")


def move_files_to_scripts_folder(src_dir, dst_dir, num_files):
    # Ensure the destination directory exists
    os.makedirs(dst_dir, exist_ok=True)

    # Loop through each file in the source directory but only up to 3, don't want that many
    num_solutions = 0
    for filename in os.listdir(src_dir):
        if num_solutions == num_files:
            break
        src_file = os.path.join(src_dir, filename)
        dst_file = os.path.join(dst_dir, filename)
        
        # Copy the file
        shutil.copy(src_file, dst_file)
        print(f"File '{src_file}' copied to '{dst_file}' successfully")
        num_solutions += 1
    return num_solutions

def rename_solutions(scripts_path):

    # Define the directory where the files are located
    directory = Path(scripts_path)

    # Loop through each file in the directory
    for i, filepath in enumerate(directory.iterdir(), start=1):
        if filepath.is_file():  # Make sure it's a file, not a directory
            new_filename = f"code-{i}.py"
            new_path = directory / new_filename
            
            # Rename the file
            filepath.rename(new_path)
            print(f"Renamed '{filepath.name}' to '{new_filename}'")

def file_exists_in_directory(directory, filename):
        # Create a Path object for the directory and file
        # filepath = Path(directory) / filename
        # # Check if this path exists and is a file
        # return filepath.is_file()
        # Create the full path to the file
    file_path = os.path.join(directory, filename)

    # Check if the file exists
    if os.path.isfile(file_path):
        print(f"The file '{filename}' exists in '{directory}'")
        return True
    else:
        print(f"The file '{filename}' does not exist in '{directory}'")
        return False
    
def remove_real_suffix(test_cases_path, num_test_cases):
    # if output names have the suffix '-real', and the original output name has not been renamed as well, then it should be deleted and then output file renamed
    directory = Path(test_cases_path)
    for i in range(1, num_test_cases+1):
        input_file = f"{i}_input.txt"
        output_file = f"{i}_output_real.txt"
        if file_exists_in_directory(test_cases_path, output_file):
            if file_exists_in_directory(test_cases_path, f"{i}_output.txt"):
                # delete this file
                old_file_path = Path(test_cases_path + f"/{i}_output.txt")
                old_file_path.unlink()
                print(f"File '{old_file_path}' has been deleted.")

            # rename the -real file to be actual file
            new_file_name = f"{i}_output.txt"
            file_path = directory / f"{i}_output_real.txt"
            new_path = directory / new_file_name
            file_path.rename(new_path)
            print(f"Renamed '{file_path.name}' to '{new_file_name}'")

def remove_standalones(test_cases_path, num_test_cases):
    # now that the '_real' suffix has been removed, need to make sure that there is only one input for one output
    for i in range(1, num_test_cases+1):
        input_file = f"{i}_input.txt"
        output_file = f"{i}_output.txt"
        if not file_exists_in_directory(test_cases_path, input_file): # if there's no input, delete output:
            if file_exists_in_directory(test_cases_path, output_file):
                old_file_path = Path(test_cases_path + f"/{i}_output.txt")
                old_file_path.unlink()
                print(f"File '{old_file_path}' has been deleted.")
        elif not file_exists_in_directory(test_cases_path, output_file):
            if file_exists_in_directory(test_cases_path, input_file): # if there's no output, delete the input
                old_file_path = Path(test_cases_path + f"/{i}_input.txt")
                old_file_path.unlink()
                print(f"File '{old_file_path}' has been deleted.")

def get_indexed_files(test_cases_path):
    """Return a sorted list of tuples (index, filename) for files in the directory named '{index}_input.txt'."""
    files = []
    for filename in os.listdir(test_cases_path):
        match = re.match(r"(\d+)_input\.txt", filename)
        if match:
            index = int(match.group(1))
            files.append((index, filename, f"{index}_output.txt")) # add output at some point
    return sorted(files)

def get_missing_indices(indices):
    if not indices:
        return []
    full_range = range(min(indices), max(indices) + 1)
    return [i for i in full_range if i not in indices]

    # indices = []
    # for i in range(1, num_test_cases+1):
    #     input_file = f"{i}_input.txt"
    #     output_file = f"{i}_output.txt"
    #     if not file_exists_in_directory(test_cases_path, input_file) and not file_exists_in_directory(test_cases_path, output_file):
    #         indices.append(i)

def ensure_order(test_cases_path, num_test_cases):
    # Count files in the directory
    files = get_indexed_files(test_cases_path)
    indices = [index for index, _ , _ in files]
    print("indices: ", indices)
    missing_indices = get_missing_indices(indices)
    print('missing_indices:', missing_indices)

    target_map = {} ## will map indices to what they actually should be
    target_map = {index: index for index in indices}

    # Go through the files in reverse order, renaming to fill gaps
    for missing_index in reversed(missing_indices):
        # Start from the highest file and shift it down to fill the missing index
        for i in range(len(files) - 1, -1, -1):
            current_index, input_file, output_file = files[i]
            if current_index > missing_index:
                target_map[current_index] = current_index - 1
                # print('current_index > missing_index')
                # print('current_index: ', current_index)
                # print('missing_index: ', missing_index)
                # new_input_filename = f"{current_index - 1}_input.txt"
                # new_output_filename = f"{current_index - 1}_output.txt"
                # os.rename(os.path.join(test_cases_path, input_file), os.path.join(test_cases_path, new_input_filename))
                # os.rename(os.path.join(test_cases_path, output_file), os.path.join(test_cases_path, new_output_filename))
                # files[i] = (current_index - 1, new_input_filename, new_output_filename)  # Update list with new filename
            else:
                break
    for index in indices:
        if target_map[index] != index: # was decreased
            old_index = index
            new_index = target_map[index]
            old_input_file = f"{old_index}_input.txt"
            old_output_file = f"{old_index}_output.txt"
            new_input_file = f"{new_index}_input.txt"
            new_output_file = f"{new_index}_output.txt"
            os.rename(os.path.join(test_cases_path, old_input_file), os.path.join(test_cases_path, new_input_file))
            os.rename(os.path.join(test_cases_path, old_output_file), os.path.join(test_cases_path, new_output_file))

    # test_cases_directory = Path(test_cases_path)

    # missing_indices = get_missing_indices(test_cases_path, num_test_cases)

    # for missing_index in reversed(missing_index):
    #     # Start from the highest file and shift it down to fill the missing index
    #     for i in range(num_test_cases, 0, -1):
    #         if i >  missing_index:
    #             file_path = 
    #             new_filename = f"{i-1}_input.txt"
    #             new_path = test_cases_directory / new_filename

    #             new_file_name = f"{i}_output.txt"
    #         file_path = directory / f"{i}_output_real.txt"
    #         new_path = directory / new_file_name
    #         file_path.rename(new_path)
    #         print(f"Renamed '{file_path.name}' to '{new_file_name}'")
            
    #         # Rename the file
    #         filepath.rename(new_path)
    #         print(f"Renamed '{filepath.name}' to '{new_filename}'")

def get_num_test_cases(test_cases_path):
    test_cases_directory = Path(test_cases_path)
    num_files = sum(1 for item in test_cases_directory.iterdir() if item.is_file())
    # oh wait... but there are other files in the directory
    print(f"Number of files in '{test_cases_directory}': {num_files}")
    assert num_files % 2 == 0, "there should be an output for every input and vice versa"
    return num_files // 2

def clean_test_cases(script_path, test_cases_path, num_test_cases):
    # !!!!!! not sure if the way i am handling num_test_cases is very sound to be honest. maybe I should do that differently.
    directory = Path(script_path)
    # some test cases are missing outputs and some are missing inputs
    # also, some output names now have the suffix '-real'
    
    
    
    # now make sure that the inputs and the outputs are in the correct order:

    

def read_file_to_list(file_path):
    with open(file_path, 'r') as file:
        # Read lines, strip newline characters, and store in a set
        temp_list = file.read().split()
        return [elt.strip() for elt in temp_list]
        # return list(line.strip() for line in file if line.strip())
    
def compare_outputs(file_path_expected, file_path_stdout):
    list_expected = read_file_to_list(file_path_expected)
    list_stdout = read_file_to_list(file_path_stdout)
    print("list expected: ", list_expected)
    print("list stdout: ", list_stdout)

    if len(list_expected) != len(list_stdout):
        return False
    # smallest_length = min(len(list_expected), len(list_stdout))
    for i in range(len(list_expected)):
        if(list_expected[i] != list_stdout[i]):
        # if int(float(list_expected[i])) != int(float(list_stdout[i])): # to deal with 10.0 being compared to 10, ok but
            # also this assumes that they are ints when they could also be strings, hmm don't know how to deal with that
            return False
        
    return True

def check_output(test_cases_path, code_name, stdout_filepath, num_test_cases, input_no):
    # see if the output matches the output of any of the files
    # if so, rename that output to correspond to the input
    directory = Path(test_cases_path)
    for i in range(1, num_test_cases+1): #!!! why am i using num_solutions here?? i think it should be no. of test cases?
        output_file = f"{i}_output.txt"
        if file_exists_in_directory(directory, output_file):
            output_file_path = test_cases_path + "/" + output_file
            # with open(output_file_path, 'r') as file:
            #     expected = file.read()
            # with open(stdout_filepath, 'r') as file:
            #     stdout = file.read()
            if compare_outputs(output_file_path, stdout_filepath):
            # if expected == stdout: # it's the correct output.
                # if i != input_no:  # meaning the input number does not match the output number
                # actually do it regardless so we know if it didn't find any solution or not
                file_path = directory / f"{i}_output.txt"
                new_filename = f"{input_no}_output_real.txt"
                new_path = directory / new_filename
                file_path.rename(new_path)
                print(f"Renamed '{file_path.name}' to '{new_filename}'")
                # else: # it is the correct number and we don't rename anything. and then when we clean... i don't think anything happens?
                    # pass

            


def run_code(code_path, test_cases_path, code_name, num_solutions, num_test_cases):
    code_directory = Path(code_path)

    # Define the command as a list (recommended for cross-platform compatibility)
    for i in range(1, num_test_cases+1):
        input_file = f"{i}_input.txt"
        # print('in for loop of run_code()')
        if file_exists_in_directory(test_cases_path, input_file):
            # Run the command and capture output
            print('in if statement of run_code()')
            # try:
            #     with open(test_cases_path + "/" + input_file, 'r') as infile:
            #         print("Input file opened successfully.")
            #         with open(code_path + f"/stdout-{code_name}-input-{i}.txt", 'w') as outfile:
            #             print("Output file opened successfully.")
            # except Exception as e:
            #     print(f"Error during file handling: {e}")

            try: 
                with open(test_cases_path + "/" + input_file, 'r') as infile, open(code_path + f"/stdout-{code_name}-input-{i}.txt", 'w') as outfile:
        # Run the command, passing infile for stdin and outfile for stdout
                    command = ["python", code_path + f"/{code_name}.py"]
                    result = subprocess.run(command, stdin=infile, stdout=outfile, stderr=subprocess.PIPE, text=True)

                    # print('error: ', result.stderr)
                    if result.stderr:
                        print("stderr:", result.stderr)
                    else:
                        print(f"The output has been written to 'stdout-{code_name}-input-{i}.txt'")
            except FileNotFoundError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

            check_output(test_cases_path, f"{code_name}.py", code_path + f"/stdout-{code_name}-input-{i}.txt" , num_test_cases, i) # see if the output matches the output of any of the files


def main():
    problem_name = 'a-team'
    difficulty_level = 'long'
    run_scripts_path = f"{ROOT_DIR}/dataset/{difficulty_level}/{problem_name}/run_scripts"
    solutions_path = f"{ROOT_DIR}/dataset/{difficulty_level}/{problem_name}/solutions_python"
    test_cases_path = f"{ROOT_DIR}/dataset/{difficulty_level}/{problem_name}/samples"
    new_test_cases_path = f"{ROOT_DIR}/dataset/{difficulty_level}/{problem_name}/test_cases"

    # Step 1: organize the code
    # make_directory(run_scripts_path)
    # make_directory(new_test_cases_path)
    # num_solutions = move_files_to_scripts_folder(solutions_path, run_scripts_path, 10) # move python solutions to scripts folder
    # rename_solutions(run_scripts_path)
    # num_test_cases = move_files_to_scripts_folder(test_cases_path, new_test_cases_path, 20) // 2 # move test cases to scripts folder, do so AFTER renaming solutions
    # so that only the solutions are renamed
    # divide by 2 because there's input and output file for every test case
    

    # Step 2: run scripts to figure out which inputs correspond to what
    code_name = 'code-1'
    num_solutions = 1
    # num_test_cases = get_num_test_cases(new_test_cases_path) # need to find a better way to calculate this
    num_test_cases = 5
    run_code(run_scripts_path, new_test_cases_path, code_name, num_solutions, num_test_cases)

    # Step 3: clean the test cases:
    # clean_test_cases(run_scripts_path, new_test_cases_path, num_test_cases) -> don't use this at all right now, will
    # later be a wrapper for clean test cases i am assuming
    num_test_cases = 5
    # remove_real_suffix(new_test_cases_path, num_test_cases)
    # remove_standalones(new_test_cases_path, num_test_cases)
    # num_test_cases = get_num_test_cases(new_test_cases_path)
    ensure_order(new_test_cases_path, num_test_cases)


if __name__ == "__main__":
    main()

