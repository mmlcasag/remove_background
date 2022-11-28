After git cloning the project into a local folder, please follow these steps:

## 1. Install python and pip locally.

### python ###

Use the most recent version available <a href="https://www.python.org/downloads/">here</a>.

The project currently uses Python version 3.9.2.

### pip ###

To check if pip is installed, run:

*Using Linux?*
```
python -m pip --version
```

*Using Windows?*
```
C:\> py -m pip --version
```

If not installed, run the following commands to install:

*Using Linux?*
```
sudo apt update
sudo apt install python3-pip
```

*Using Windows?*
```
C:\> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
C:\> python get-pip.py
```

## 2. Install pipenv

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.

To check if pipenv is installed, run:
```
pipenv check
```

If not installed, run the following command to install:
```
pip install pipenv
```

For Linux, it is important to check if the current bash has a path to `~/.local/bin`.

## 3. Run project using virtual environment (venv)

*Using Linux?*

First, set variable PIPENV_VENV_IN_PROJECT to pipenv install packages inside project folder (.venv)

```
export PIPENV_VENV_IN_PROJECT="enabled" 
```

*Using Windows?*

Inside the project's folder, run the following command:

```
mkdir .venv
```

Now, inside the project's folder, run the following command:

```
pipenv shell
```

This command spawns a shell within the virtualenv.

All `python` and `pip` commands will be executed using the binaries created by the virtual enviroment.

Type 'exit' or 'Ctrl+D' to return.

## 4. Install the project dependencies

This command should be executed within the virtual environment.
Execute the `pipenv shell` before install the packages:

Inside the project's folder, run the following command:
```
pipenv install
pipenv install --dev
```

Remember to copy the ai/u2net.onnx file and paste it in the C:\Users\{USERNAME}\.u2net folder

All packages inside `Pipfile` will be installed.

## 5. Build the project

Run command:
```
pyinstaller remove_background.py --onefile
```

## 6. Run the project

Run command:
```
python remove_background.py
```

## 7. Exit the virtual environment:

Run command:
```
exit
```