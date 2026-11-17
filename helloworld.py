print("Hello, World!")
print("My Name is Julian Ortiz")
print("I am a relearning Python.")
print("This is a simple Python program.")
print("It demonstrates basic syntax and output.")

print("These are teh current projects in this file: ")

from pathlib import Path

project = Path(".")  # current folder

print("These are the current folders in this project:")
for item in sorted(project.iterdir()):
    if item.is_dir():
        print(f"  {item.name}")





