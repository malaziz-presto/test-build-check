from setuptools import find_namespace_packages, setup

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="PNLU-entity_recognizer",
    packages=find_namespace_packages(include=["PNLU.*"]),
    python_requires=">=3.10,<3.11",
    package_data={
        "utilities": ["py.typed"],
    },
    install_requires=install_requires,
)
