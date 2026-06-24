import subprocess

command = "dir"

result = subprocess.run(command, shell=True, text=True, capture_output=True)

print('return code')
print(result.returncode)
print('standard output')
print(result.stdout)