from pathlib import Path
from setuptools import setup, find_packages

def get_requirements(filename="requirements.txt"):
    req_path = Path(__file__).parent / filename
    requirements = []
    for line in req_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("-e"):
            continue
        requirements.append(line)
    return requirements

setup(
    name="networksecurity",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements(),
)
