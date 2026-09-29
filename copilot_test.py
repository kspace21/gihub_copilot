import platform
import subprocess


def print_uptime():
    system = platform.system()
    try:
        if system == "Windows":
            output = subprocess.check_output(
                "systeminfo | findstr /C:\"System Boot Time\"",
                shell=True,
                text=True,
                stderr=subprocess.STDOUT,
            )
            print(output.strip())
        else:
            output = subprocess.check_output("uptime", shell=True, text=True, stderr=subprocess.STDOUT)
            print(output.strip())
    except Exception as exc:
        print(f"Unable to get system uptime: {exc}")


if __name__ == "__main__":
    print_uptime()
