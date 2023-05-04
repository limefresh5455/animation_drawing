import subprocess

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    print(completed)
    return completed.stdout.decode("utf-8")

print(run("python"))

