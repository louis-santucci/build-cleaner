# build-cleaner
This is a Python CLI application to clean build folders within a given folder

## Usage

Usage: build_cleaner.py [OPTIONS] [PATHS]...

Usage for executable file: build_cleaner.exe [OPTIONS] [PATHS]...

Options:

- -r, --root DIRECTORY  [default: .]
- --help                Show this message and exit.

## Installation
First you have to create a virtual env to install the required dependencies of the project:

`python -m venv ./venv/`

Once it's done, you can activate the virtual env by running your specific environment script available in _venv/Scripts/_

For example on windows in a Powershell terminal you can execute:

`./venv/Scripts/Activate.ps1`

Then you can run the following command to install the required dependencies:

`pip install -r requirements.txt`

From now on you can run the python file.

If you want to build an executable, you can run the following command:

`pyinstaller --onefile build_cleaner.py`

The generated _dist/_ folder will contain your executable file

