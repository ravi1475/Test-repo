import os

for i in range(100):
    with open("commits.txt", "a") as file:
        file.write(f"Commit number {i + 1}\n")
    
    os.system("git add commits.txt")
    os.system(f'git commit -m "Commit number {i + 1}"')

os.system("git push origin main")
