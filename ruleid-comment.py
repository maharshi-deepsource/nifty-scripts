import os
import re

def replaceRuleidComments(filePath):
    with open(filePath, "r") as f:
        lines = f.readlines()
    with open(filePath, "w") as f:
        for line in lines:
            # replace '# ruleid: ' with '# <expect-error>'
            line = re.sub(r"#\s*ruleid:\s*.*", "# <expect-error>", line)
            # replace '# ok: ' with '# <no-error>'
            line = re.sub(r"#\s*ok:\s*.*", "# <no-error>", line)
            f.write(line)


if __name__ == "__main__":
    # works only on the current directory
    for file in os.listdir():
        # works on python files
        if file.endswith(".py"):
            replaceRuleidComments(file)
            print(f"[INFO] Processed -> {file}")
