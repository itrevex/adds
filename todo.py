import glob
import re
files = glob.glob("./**/*.py", recursive=True)

printed = []
for file in files:
    with open(file) as f:
        for line in f.readlines():
            if line.strip() != "":
                if re.search("(?=#.*$)(?=.*\\bTODO\\b).*$", line, re.IGNORECASE):
                    if file not in printed:
                        print("\n"+file)
                    print(line.strip()) #todo print the work to a file
                    printed.append(file)
    # break;