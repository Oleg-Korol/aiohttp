import pathlib
from typing import List, Callable

from setuptools import setup, find_packages

BASE_DIR = pathlib.Path(__file__).parent.absolute()


def get_version() -> str:
    with open(BASE_DIR / "VERSION") as file:
        return file.readline().strip()


def get_licence() -> str:
    with open(BASE_DIR / "LICENCE") as file:
        return file.readline().strip()


def get_desc() -> str:
    with open(BASE_DIR / "README.md") as file:
        return file.readline().strip()


def get_packages() -> list[Callable[[str | None], str]]:
    with open(BASE_DIR / "requirements.txt") as file:
        return [
            package.strip for package in file if package or not package.startswith("#")
        ]


setup(
    name="anet",
    version=get_version(),
    author="OLeg",
    author_email="admin@google.com",
    url="doc.site.com",
    packages=find_packages(".", include=["anet"], exclude=["*tests*.py,*tests*"]),
    package_dir={"": "."},
    include_package_data=True,
    license=get_licence(),
    description="anet",
    long_description=get_desc(),
    long_description_content_tipe="text/markdown",
    install_requeres=get_packages(),
    python_requeres=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha"
        if "dev" in get_version()
        else "Development Status :: 4 Beta"
        if "rc" in get_version()
        else "Development Status :: 5 Production/Stable"
    ],
    # entry_points = {
    #    "console_scripts": ["a_net = anet.app:run"]
    #               }
)
