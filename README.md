# auto-type-tool

Tool for automating something...

# How to build executable file
Information below is for app maintainers only. Feel free to skip if you're just using the executable file.

❗ **NOTE **: You can build .exe files only on Windows.

## Install necessary packages
Below we will assume that you are using Python 3.6 or 3.7 as your main interpreter on the system.
```shell
pip install pandas paramiko PySimpleGUI pywin32 pyinstaller auto-py-to-exe
```

❗ **NOTE **: If you have already installed auto-py-to-exe before, update it to the newest version for compatibility with Python 3.8:
```shell
pip install --upgrade auto-py-to-exe
```

We will be using `auto-py-to-exe`, which is a GUI wrapper around `pyinstaller` module.

## Building executable
1. Open command prompt, go to the script directory and run `auto-py-to-exe` command. This will bring up a GUI interface.
2. Setup build configuration:
    * Browse to `Rude.py` script location
    * Choose `One File`
    * Choose `Window Based (hide the console)`
    * Under `Additional Files`, click `Add Files` and choose `rude.png` in the same folder
3. Confirm and press `CONVERT .PY TO .EXE`. Your executable will be put into `output` folder.
4. Check that your executable works.
