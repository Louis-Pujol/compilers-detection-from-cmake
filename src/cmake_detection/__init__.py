import argparse
import os
import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

__version__ = "0.0.0"

all = ["__version__"]

def get_os_info():
    return {
        "system": platform.system(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "architecture": platform.architecture(),
        "python_implementation": platform.python_implementation(),
        "python_compiler": platform.python_compiler(),
        "os_name": os.name,
    }

def detect_compilers(out_file, os_info):

    cwd = Path.cwd()
    with tempfile.TemporaryDirectory() as temp_dir:

        os.chdir(temp_dir)

        # Copy CMakeLists.txt to the temporary directory
        cmake_lists_path = Path(__file__).parent / "CMakeLists.txt"
        if cmake_lists_path.exists():
            shutil.copy(cmake_lists_path, temp_dir)
        else:
            msg = f"{cmake_lists_path} does not exist."
            raise FileNotFoundError(msg)

        Path("build").mkdir(exist_ok=True)
        os.chdir("build")

        result = subprocess.run(["cmake", ".."], capture_output=True, check=False)

        with Path.open(out_file, 'w') as f:
            f.write("OS Information:\n")
            for key, value in os_info.items():
                f.write(f"{key}: {value}\n")
            f.write("\nCMake Output:\n")
            f.write(result.stdout.decode())
            f.write("\nErrors\n")
            f.write(result.stderr.decode())

        os.chdir(cwd)

def main():
    parser = argparse.ArgumentParser(description="Detect compilers")
    parser.add_argument("out_file", help="The file where the output will be written", default="detection_result.txt")

    os_info = get_os_info()
    args = parser.parse_args()
    detect_compilers(Path(args.out_file).resolve(), os_info)

if __name__ == "__main__":
    main()
