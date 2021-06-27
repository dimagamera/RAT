from cx_Freeze import setup, Executable

base = None

executables = [Executable("client.py", base=base)]

packages = ["requests", "PIL", "subprocess", "sys", "socket", "os"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="LOGER",
    options=options,
    version="1.0",
    description='',
    executables=executables
)