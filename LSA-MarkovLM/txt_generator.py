import os

os.makedirs("generated_files", exist_ok=True)

s = ""
cnt = 1

with open('txt_files/original.txt', 'r') as f:
    for line in f:
        if line.strip():
            s += line.strip() + "\n"
        else:
            if s == "":
                continue
            with open(f'generated_files/paragraph_{cnt}.txt', 'w') as out:
                out.write(s.strip())
            cnt += 1
            s = ""
