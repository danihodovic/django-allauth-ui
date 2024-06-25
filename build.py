import subprocess


def compile_tailwind():
    subprocess.run(["npm", "run-script", "build"], check=True)


if __name__ == "__main__":
    compile_tailwind()
