import platform
import subprocess

def notepad():

    param = "notepad"
    command = [param]

    return subprocess.call(command) == 0

notepad()