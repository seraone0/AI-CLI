import subprocess
import sys

os = sys.platform
command = "dir" if os == "win32" else "ls"

result = subprocess.run(command, shell=True, text=True, capture_output=True)

print('return code')
print(result.returncode)
print('standard output')
print(result.stdout)