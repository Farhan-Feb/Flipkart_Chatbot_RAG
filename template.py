import os
from pathlib import Path

project_name = "flipkart"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/data_converter.py",
    f"{project_name}/data_ingestion.py",
    f"{project_name}/retrieval_generation.py",
    "static/style.css",
    "templates/index.html",
    "setup.py",
    "app.py",
    "requirements.txt",
    ".env"
]

# Add folder paths (even if no files needed yet)
folders_to_create = [
    "images"
]

# Create necessary folders
for folder in folders_to_create:
    os.makedirs(folder, exist_ok=True)

# Create files if they don't exist or are empty
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
