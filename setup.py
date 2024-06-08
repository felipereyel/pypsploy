import pathlib

from setuptools import find_packages, setup

version = "0.0.0.dev0"
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8")
requirements = (HERE / "requirements.txt").read_text(encoding="utf-8").split("\n")

setup(
    name="psplot",
    license="MIT",
    version=version,
    description="psplot",
    python_requires=">=3.9, <4",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/felipereyel/pypsplot",
    entry_points={
        "console_scripts": [
            "psplot=psplot.cli:main",
        ],
    },
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
)

