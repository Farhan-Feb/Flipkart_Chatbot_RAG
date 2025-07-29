from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    with open("requirements.txt", "r") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]

setup(
    name="flipkart",
    version="0.0.1",
    author="Farhan Hameed",
    author_email="farhan@example.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
