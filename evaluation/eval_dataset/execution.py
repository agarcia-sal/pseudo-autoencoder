import contextlib
import faulthandler
import ast
import io
import multiprocessing
import os
import platform
import signal
import tempfile
import subprocess
import re
from typing import Dict, List, Any, Optional, Union


# Remove surrounding quotes if present
def remove_quotes(s):
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    return s

def cmp_outputs(output_1, output_2):
    cleaned_output_1 = remove_quotes(output_1.strip())
    cleaned_output_2 = remove_quotes(output_2.strip())

    # if cleaned_output_1 == cleaned_output_2:
    #     return True
    # check for boolean mismatch:
    bool_map = {'true': True, 'false': False, 'True': True, 'False': False}
    if (cleaned_output_1 in bool_map.keys()) and (cleaned_output_2 in bool_map.keys()) and (bool_map.get(cleaned_output_1) == bool_map.get(cleaned_output_2)):
        return True
    
    # check for space mismatches, eg. [1,2] vs [1, 2]
    try:
        # Parse both strings as Python objects
        expected_obj = ast.literal_eval(cleaned_output_1)
        actual_obj = ast.literal_eval(cleaned_output_2)
        return expected_obj == actual_obj
    except (SyntaxError, ValueError):
        # If parsing fails, fall back to normalized string comparison
        return cleaned_output_1 == cleaned_output_2
    # else:
    #     return False
    
    
def unsafe_execute(problem: Dict, completion: str, timeout: float, result_list):
# def unsafe_execute(problem: Dict, completion: str, timeout: float, result):
    # with create_tempdir():

    #     # These system calls are needed when cleaning up tempdir.
    #     import os
    #     import shutil

    #     rmtree = shutil.rmtree
    #     rmdir = os.rmdir
    #     chdir = os.chdir

    #     # Disable functionalities that can make destructive changes to the test.
    #     reliability_guard()

    #     # Construct the check program and run it.
    #     check_program = (
    #         problem["prompt"] 
    #         + "\n"  
    #         + completion
    #         + "\n"
    #         + problem["test"]
    #         + "\n"
    #         + f"check({problem['entry_point']})"
    #     )

    #     try:
    #         exec_globals = {}
    #         with swallow_io():
    #             with time_limit(timeout):
    #                 exec(check_program, exec_globals)
    #         result.append("passed")
    #     except TimeoutException:
    #         result.append("timed out")
    #     except BaseException as e:
    #         result.append(f"failed: {e}")

    #     # Needed for cleaning up.
    #     shutil.rmtree = rmtree
    #     os.rmdir = rmdir
    #     os.chdir = chdir
    with create_tempdir():
        import os
        import shutil

        # Backup original functions for cleanup
        # rmtree = shutil.rmtree
        # rmdir = os.rmdir
        # chdir = os.chdir

        # reliability_guard()

        # Extract individual test cases by splitting on 'assert' statements
        test_cases = []
        test_code = problem["test"].strip()
        if test_code:
            # Split test cases while preserving assertion lines
            test_lines = test_code.split('\n')
            for line in test_lines:
                if line.strip().startswith('assert '):
                    test_cases.append(line.strip())

        base_program = problem["prompt"] + "\n" + completion + "\n"

        test_results = []
        all_passed = True
        num_test_cases = len(test_cases)
        num_correct = 0

        for idx, test_case in enumerate(test_cases):
            check_program = (
                base_program
                + "def check(candidate):\n    "
                + test_case 
                + "\n" 
                + f"check({problem['entry_point']})"
            )

            # print('check_program:')
            # print(check_program)

            try:
                exec_globals = {}
                # Simple timeout using threads
            #     import threading
            #     result = [None]
                
            #     def execute_code():
            #         try:
            #             exec(check_program, exec_globals)
            #             result[0] = True
            #         except Exception as e:
            #             result[0] = e
                
            #     thread = threading.Thread(target=execute_code)
            #     thread.daemon = True
            #     thread.start()
            #     thread.join(timeout)
                
            #     if thread.is_alive():
            #         test_results.append({"passed": False, "error": "timed out"})
            #         all_passed = False
            #         break
            #     elif isinstance(result[0], Exception):
            #         test_results.append({"passed": False, "error": str(result[0])})
            #         all_passed = False
            #     else:
            #         test_results.append({"passed": True, "error": None})
            # except Exception as e:
            #     test_results.append({"passed": False, "error": str(e)})
            #     all_passed = False
                with swallow_io():
                    with time_limit(timeout):
                        exec(check_program, exec_globals)
                test_results.append({"test_case_id": idx, "test_case": test_case, "passed": True, "error": None})
                num_correct += 1 
                # print('am in the try of unsafe_execute()')
            except TimeoutException:
                test_results.append({"test_case_id": idx, "test_case": test_case, "passed": False, "error": "timed out"})
                all_passed = False
                # print('time out exception in unsafe_execute')
                break  # Timeout applies to the whole problem
            except BaseException as e:
                test_results.append({"test_case_id": idx, "test_case": test_case, "passed": False, "error": str(e)})
                all_passed = False
                # print(f'Exception: {e} in unsage_execute')
                # Continue to next test case (comment this line to stop on first failure)

        # print('\n\nEND OF PROBLEM \n\n')


        if all_passed:
            # result_list.append({"status": "passed", "num_test_cases": num_test_cases, "num_correct": num_correct, "test_results": test_results})
            result = [{"status": "passed", "num_test_cases": num_test_cases, "num_correct": num_correct, "test_results": test_results}]
        else:
            # result_list.append({"status": "failed", "num_test_cases": num_test_cases, "num_correct": num_correct, "test_results": test_results})
            result = [{"status": "failed", "num_test_cases": num_test_cases, "num_correct": num_correct, "test_results": test_results}]
        
        # print('final result in unsafe_execute:')
        # print(result)

        # Restore original functions
        # shutil.rmtree = rmtree
        # os.rmdir = rmdir
        # os.chdir = chdir

        return result

def safe_execute_leet_code(problem: Dict, completion: str, timeout: float):
    """Secure code execution using subprocess isolation"""

    # test_cases = []
    # test_code = problem["test"].strip()
    # if test_code:
    #     # Split test cases while preserving assertion lines
    #     test_lines = test_code.split('\n')
    #     for line in test_lines:
    #         if line.strip().startswith('assert '):
    #             test_cases.append(line.strip())

    base_program = problem["prompt"] + "\n" + completion + "\n"

    # "input_output": [{"input": "strs = [\"flower\",\"flow\",\"flight\"]", "output": "\"fl\""}, {"input": "strs = 

    input_output_list = problem["input_output"]

    test_results = []
    all_passed = True
    # num_test_cases = len(test_cases)
    num_test_cases = len(input_output_list)
    num_correct = 0
    
    with tempfile.TemporaryDirectory() as temp_dir:
        for idx, input_output in enumerate(input_output_list):
            inputs = input_output["input"]
            outputs = input_output["output"]
            # check_program = (
            #     base_program
            #     + "def check(candidate):\n    "
            #     + test_case 
            #     + "\n" 
            #     + f"check({problem['entry_point']})"
            # )
            check_program = (
                base_program
                + f"print({problem['entry_point']}({inputs}))"
            )
        # Write code to a temporary file
            code_path = os.path.join(temp_dir, f"solution_{idx}.py")
            with open(code_path, 'w') as f:
                f.write(check_program)

            # print('this is the check_program:')
            # print(check_program)
        
        # Write test to another file
        # test_path = os.path.join(temp_dir, "test.py")
        # with open(test_path, 'w') as f:
        #     f.write(problem["prompt"] + "\n" + completion + "\n" + problem["test"])
        
        # Execute with subprocess and strict limits
            try:
                result = subprocess.run(
                    ["python3", code_path],
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    cwd=temp_dir,  # Confine to temp directory
                    # Additional security measures:
                    # preexec_fn=lambda: os.setrlimit(...)  # Set resource limits
                )
                # print('compare results for this test case')
                # print('result.stdout: ')
                # print(result.stdout)
                # print('outputs')
                # print(outputs)
                # if result.stdout.strip() == outputs:
                if cmp_outputs(result.stdout, outputs):
                    # print('outputs match!!')
                    test_results.append({"test_case_id": idx, "test_case": input_output, "passed": True, "error": ''})
                    num_correct += 1 
                elif result.stderr:
                    test_results.append({"test_case_id": idx, "test_case": input_output, "passed": False, "error": result.stderr})
                    all_passed = False
                else:
                    test_results.append({"test_case_id": idx, "test_case": input_output, "passed": False, "error": "Outputs do not match"})
                    all_passed = False
                
            except subprocess.TimeoutExpired:
                test_results.append({"test_case_id": idx, "test_case": input_output, "passed": False, "error": "timed out"})
                all_passed = False
                # print('time out exception in unsafe_execute')
                break  # Timeout applies to the whole problem
            except Exception as e:
                test_results.append({"test_case_id": idx, "test_case": input_output, "passed": False, "error": str(e)})
                all_passed = False
                
        if all_passed:
            print(f"outputs match!! for all test cases in problem {problem['task_id']}\n")
            # result_list.append({"status": "passed", "num_test_cases": num_test_cases, "num_correct": num_correct, "test_results": test_results})
            result = [{"status": "passed", "num_test_cases": num_test_cases, "num_correct": num_correct, "test_results": test_results}]
        else:
            # result_list.append({"status": "failed", "num_test_cases": num_test_cases, "num_correct": num_correct, "test_results": test_results})
            result = [{"status": "failed", "num_test_cases": num_test_cases, "num_correct": num_correct, "test_results": test_results}]

        return result

def extract_import_statements(prompt):
    """Extract only import statements from a code prompt"""
    # Pattern to match various import styles
    import_pattern = r'^(from\s+\w+(?:\s+import\s+\w+(?:\s*,\s*\w+)*)?|import\s+\w+(?:\s*,\s*\w+)*)$'
    
    lines = prompt.split('\n')
    imports = []
    
    for line in lines:
        stripped_line = line.strip()
        # Skip empty lines and function definitions
        if not stripped_line or stripped_line.startswith('def ') or stripped_line.startswith('class '):
            continue
        # Check if it's an import statement
        if re.match(import_pattern, stripped_line):
            imports.append(stripped_line)
    
    return imports

    
def safe_execute(problem: Dict, completion: str, timeout: float):
    """Secure code execution using subprocess isolation"""
    # TO DO: fix, this 

    test_cases = []
    test_code = problem["test"]

    # assert_pattern = r'assert candidate\((.*)\) == (.*)'
    assert_pattern_equals = r'assert (.*?) == (.*?)(?:,\s*("[^"]*"|\'[^\']*\'))?(?=\s*assert|$)'
    # this part handles potential error messages like: "This prints if this":
    # (?:,\s*("[^"]*"|\'[^\']*\'))?
    assert_pattern_tolerance = r'assert (.*?) < (.*?)(?:,\s*("[^"]*"|\'[^\']*\'))?(?=\s*assert|$)'

    containers_equals = re.finditer(assert_pattern_equals, test_code, re.DOTALL)

    for match in containers_equals:
        assert_statement = match.group()
        if "assert fails" not in assert_statement:
            if ", \"This prints if this" in assert_statement: #[TO DO]: fix to be more robust and general
                assert_statement = assert_statement[:assert_statement.find(", \"This prints if this")]
            if ", \"Test " in assert_statement:
                assert_statement = assert_statement[:assert_statement.find(", \"Test ")] #[TO DO]: fix to be more robust and general
            test_cases.append(assert_statement)

    containers_tolerance = re.finditer(assert_pattern_tolerance, test_code, re.DOTALL)
    for match in containers_tolerance:
        assert_statement = match.group()
        if "assert fails" not in assert_statement and ", \"This prints if this" not in assert_statement: #[TO DO]: fix to be more robust
            if ", \"This prints if this" in assert_statement: #[TO DO]: fix to be more robust and general
                assert_statement = assert_statement[:assert_statement.find(", \"This prints if this")]
            if ", \"Test " in assert_statement:
                assert_statement = assert_statement[:assert_statement.find(", \"Test ")] #[TO DO]: fix to be more robust and general
            test_cases.append(assert_statement)



    
    # test_code = problem["test"].strip()
    # if test_code:
    #     # Split test cases while preserving assertion lines
    #     test_lines = test_code.split('\n')
    #     for line in test_lines:
    #         if line.strip().startswith('assert '):
    #             test_cases.append(line.strip())

    # test_cases = parse_humaneval_test_cases(test_code=problem["test"])

    # base_program = problem["prompt"] + "\n" + completion + "\n"
    base_program = ''
    import_statements = extract_import_statements(problem['prompt'])
    for import_stmnt in import_statements:
        base_program += import_stmnt 
    base_program += "\n" + completion + "\n"

    test_results = []
    all_passed = True
    num_test_cases = len(test_cases)
    num_correct = 0
    
    with tempfile.TemporaryDirectory() as temp_dir:
        for idx, test_case in enumerate(test_cases):
            check_program = (
                base_program
                + "def check(candidate):\n    "
                + test_case 
                + "\n" 
                + f"check({problem['entry_point']})"
            )
        # Write code to a temporary file
            code_path = os.path.join(temp_dir, f"solution_{idx}.py")
            with open(code_path, 'w') as f:
                f.write(check_program)
        
        # Write test to another file
        # test_path = os.path.join(temp_dir, "test.py")
        # with open(test_path, 'w') as f:
        #     f.write(problem["prompt"] + "\n" + completion + "\n" + problem["test"])
        
        # Execute with subprocess and strict limits
            try:
                result = subprocess.run(
                    ["python3", code_path],
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    cwd=temp_dir,  # Confine to temp directory
                    # Additional security measures:
                    # preexec_fn=lambda: os.setrlimit(...)  # Set resource limits
                )
                # print('\n\nresults.stdout:', result.stdout)
                # print('assertion: ', test_case)
                # print('error:', result.stderr)

                if result.stderr:
                    # print('error:')
                    # print(result.stderr)
                    test_results.append({"test_case_id": idx, "test_case": test_case, "passed": False, "error": result.stderr})
                    all_passed = False
                else:
                    test_results.append({"test_case_id": idx, "test_case": test_case, "passed": True, "error": None})
                    num_correct += 1 
                
            except subprocess.TimeoutExpired:
                test_results.append({"test_case_id": idx, "test_case": test_case, "passed": False, "error": "timed out"})
                all_passed = False
                # print('time out exception in unsafe_execute')
                break  # Timeout applies to the whole problem
            except Exception as e:
                test_results.append({"test_case_id": idx, "test_case": test_case, "passed": False, "error": str(e)})
                all_passed = False
                
        if all_passed:
            # result_list.append({"status": "passed", "num_test_cases": num_test_cases, "num_correct": num_correct, "test_results": test_results})
            result = [{"status": "passed", "num_test_cases": num_test_cases, "num_correct": num_correct, "test_results": test_results}]
        else:
            # result_list.append({"status": "failed", "num_test_cases": num_test_cases, "num_correct": num_correct, "test_results": test_results})
            result = [{"status": "failed", "num_test_cases": num_test_cases, "num_correct": num_correct, "test_results": test_results}]

        return result

def check_correctness(
    dataset_name: str, problem: Dict, completion: str, timeout: float, completion_id: Optional[int] = None
) -> Dict:
    """
    Evaluates the functional correctness of a completion by running the test
    suite provided in the problem.

    :param completion_id: an optional completion ID so we can match
        the results later even if execution finishes asynchronously.
    """

    # manager = multiprocessing.Manager()
    # result = manager.list()
    result_list = []

    # p = multiprocessing.Process(target=unsafe_execute, args=(problem, completion, timeout, result))
    # p.start()
    # p.join(timeout=timeout + 1)
    # if p.is_alive():
    #     p.kill()
    try:
        if "human_eval" in dataset_name:
            result = safe_execute(problem, completion, timeout + 1)
        elif "leet_code" in dataset_name:
            result = safe_execute_leet_code(problem, completion, timeout + 1)
        else:
            # result = safe_execute_leet_code(problem, completion, timeout + 1)
            result = safe_execute(problem, completion, timeout + 1)
        # result = safe_execute(problem, completion, timeout + 1)
        # print('result from unsafe_execute:')
        # print(result)
    except Exception as e:
        print(f"Exception: {str(e)}")
        print('result is None')
        import traceback
        traceback.print_exc()  # This will show exactly where the error occurs
        result = None
    #         problem_case = problem
    #         case_result = (None, f"Exception: {str(e)}")

    # if not result:
    #     result.append("timed out")

    # return dict(
    #     task_id=problem["task_id"],
    #     passed=result[0] == "passed",
    #     result=result[0],
    #     completion_id=completion_id,
    # )
    if not result:
        return dict(
            task_id=problem["task_id"],
            passed=False,
            result="timed out",
            num_test_cases=0,
            num_correct=0,
            completion_id=completion_id,
            test_results=[]
        )

    return dict(
        task_id=problem["task_id"],
        passed=result[0]["status"] == "passed",
        result=result[0]["status"],
        num_test_cases=result[0]["num_test_cases"],
        num_correct=result[0]["num_correct"],
        completion_id=completion_id,
        test_results=result[0]["test_results"] 
    )


@contextlib.contextmanager
def time_limit(seconds: float):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")

    signal.setitimer(signal.ITIMER_REAL, seconds)
    signal.signal(signal.SIGALRM, signal_handler)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)


@contextlib.contextmanager
def swallow_io():
    stream = WriteOnlyStringIO()
    with contextlib.redirect_stdout(stream):
        with contextlib.redirect_stderr(stream):
            with redirect_stdin(stream):
                yield


@contextlib.contextmanager
def create_tempdir():
    with tempfile.TemporaryDirectory() as dirname:
        with chdir(dirname):
            yield dirname


class TimeoutException(Exception):
    pass


class WriteOnlyStringIO(io.StringIO):
    """StringIO that throws an exception when it's read from"""

    def read(self, *args, **kwargs):
        raise IOError

    def readline(self, *args, **kwargs):
        raise IOError

    def readlines(self, *args, **kwargs):
        raise IOError

    def readable(self, *args, **kwargs):
        """Returns True if the IO object can be read."""
        return False


class redirect_stdin(contextlib._RedirectStream):  # type: ignore
    _stream = "stdin"


@contextlib.contextmanager
def chdir(root):
    if root == ".":
        yield
        return
    # cwd = os.getcwd()
    # os.chdir(root)
    # try:
    #     yield
    # except BaseException as exc:
    #     raise exc
    # finally:
    #     os.chdir(cwd)
    if hasattr(os, '_original_getcwd') and os._original_getcwd:
        original_getcwd = os._original_getcwd
        original_chdir = os._original_chdir
    else:
        original_getcwd = os.getcwd
        original_chdir = os.chdir
    
    cwd = original_getcwd()
    original_chdir(root)
    try:
        yield
    except BaseException as exc:
        raise exc
    finally:
        original_chdir(cwd)


def reliability_guard(maximum_memory_bytes: Optional[int] = None):
    """
    This disables various destructive functions and prevents the generated code
    from interfering with the test (e.g. fork bomb, killing other processes,
    removing filesystem files, etc.)

    WARNING
    This function is NOT a security sandbox. Untrusted code, including, model-
    generated code, should not be blindly executed outside of one. See the
    Codex paper for more information about OpenAI's code sandbox, and proceed
    with caution.
    """

    if maximum_memory_bytes is not None:
        import resource

        resource.setrlimit(resource.RLIMIT_AS, (maximum_memory_bytes, maximum_memory_bytes))
        resource.setrlimit(resource.RLIMIT_DATA, (maximum_memory_bytes, maximum_memory_bytes))
        if not platform.uname().system == "Darwin":
            resource.setrlimit(resource.RLIMIT_STACK, (maximum_memory_bytes, maximum_memory_bytes))

    faulthandler.disable()

    import builtins

    builtins.exit = None
    builtins.quit = None

    import os

    os.environ["OMP_NUM_THREADS"] = "1"

    os.kill = None
    os.system = None
    os.putenv = None
    os.remove = None
    os.removedirs = None
    os.rmdir = None
    os.fchdir = None
    os.setuid = None
    os.fork = None
    os.forkpty = None
    os.killpg = None
    os.rename = None
    os.renames = None
    os.truncate = None
    os.replace = None
    os.unlink = None
    os.fchmod = None
    os.fchown = None
    os.chmod = None
    os.chown = None
    os.chroot = None
    os.fchdir = None
    os.lchflags = None
    os.lchmod = None
    os.lchown = None

    # Store original functions before overriding
    if not hasattr(os, '_original_getcwd'):
        os._original_getcwd = os.getcwd
    if not hasattr(os, '_original_chdir'):
        os._original_chdir = os.chdir

    os.getcwd = None
    os.chdir = None

    import shutil

    shutil.rmtree = None
    shutil.move = None
    shutil.chown = None

    import subprocess

    subprocess.Popen = None  # type: ignore

    __builtins__["help"] = None

    import sys

    sys.modules["ipdb"] = None
    sys.modules["joblib"] = None
    sys.modules["resource"] = None
    sys.modules["psutil"] = None
    sys.modules["tkinter"] = None