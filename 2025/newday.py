import shutil, sys

day = int(sys.argv[1])
name = f"day{day:02}.py"
shutil.copy("template.py", name)
open(f"inputs/day{day:02}.txt", "w").close()
open(f"inputs/day{day:02}_example.txt", "w").close()
print("Created", name)
