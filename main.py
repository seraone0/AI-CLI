import subprocess
import sys

os = sys.platform
# command = "dir" if os == "win32" else "ls"

print("Enter command: ")

while True:
    request = input()

    if request.lower() in ['exit', 'quit', 'выход']:
        break
    if not request.strip():
        continue

    if "test" in request.lower():
        command = "mkdir test" if os == "win32" else "cd test"
        print(f"complete {command}")

        result = subprocess.run(command, shell=True, text=True, capture_output=True)

        if result.returncode == 0: print('folder created')
        else: print(f'folder creation failed {result.stderr}')

    else: print(f"check '{request}', but do not connect OpenAI API, that generation info.\n")

