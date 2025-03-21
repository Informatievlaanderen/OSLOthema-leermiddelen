# Codelist generator

This project makes use of Python virtual environments

## Set-up

First, activate the virtual environment (make sure your cwd is folder this README is in)

> Do `python3 -m venv myenv` if it's your first time doing a venv

```bash
source myenv/bin/activate   # on Linux/Mac
myenv\Scripts\activate.bat  # on Windows
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Update `codelijst.xlsx` to create the right members and definitions of a SKOS codelist.
To create the technical artefacts, run

```bash
python codelist_generator.py
```

Then, copy all relevant codelists to `../codelijsten/`

## Update code

Make sure, after updating dependencies, to update `requirements.txt`

```bash
pip freeze > requirements.txt
```
