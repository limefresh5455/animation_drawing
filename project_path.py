import subprocess
def run(cmd):
    print("running")
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True,shell=True)
    print(completed)
    return completed.stdout.decode("utf-8")