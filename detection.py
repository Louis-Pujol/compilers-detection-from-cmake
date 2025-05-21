import os
import subprocess
from pathlib import Path

Path("build").mkdir(exist_ok=True)
os.chdir("build")
result = subprocess.run(["cmake", ".."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(result.stdout.decode())
print("\nErrors\n")
print(result.stderr.decode())