# 🎂 Birthday CLI App

## 1. Purpose

The **Birthday CLI App** is a Command Line Interface (CLI) application
developed in Python that solves the practical problem of forgetting
important dates. It allows you to register, sort, and quickly check
friends' and family members' birthdays directly from the terminal.

------------------------------------------------------------------------

## 📦 Installation

Install the dependencies (in this case, `typer`) and set up the virtual
environment:

``` bash
uv sync
```

------------------------------------------------------------------------

## 🚀 How to Run

The application is executed using the `uv run` command followed by the
path to the main file (`src/cli.py`).

This ensures that the script uses the correct virtual environment where
Typer is installed.

------------------------------------------------------------------------

## 📖 Available Commands

### 🔹 View the help menu

``` bash
uv run src/cli.py --help
```

------------------------------------------------------------------------

### 🔹 Add a new birthday

*(Required arguments: name and date in YYYY-MM-DD format)*

``` bash
uv run src/cli.py add "John" "1995-05-14"
```

------------------------------------------------------------------------

### 🔹 List all birthdays

*(Sorted from the closest upcoming date to the furthest in the year)*

``` bash
uv run src/cli.py list
```

------------------------------------------------------------------------

### 🔹 View upcoming birthdays

*(Using the `--days` option)*

``` bash
uv run src/cli.py upcoming --days 15
```

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python\
-   Typer\
-   uv

------------------------------------------------------------------------

## 📂 Project Structure

    .
    ├── src/
    │   ├── cli.py
    │   ├── data.py  
    │   ├── logic.py
    ├── pyproject.toml
    └── README.md
