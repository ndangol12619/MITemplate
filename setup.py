from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = "-e ."
PROJECT_NAME = "MlTemplate"
version = "0.0.1"
AUTHOR_USER_NAME = "ndangol12619"
AUTHOR_EMAIL = "nareshkadambi@gmail.com"
DESCRIPTION = "Standard ML Project Template"


def get_requirements(file_path:str) -> List[str]:
    ''' This function will return the list of the requirements'''
    requirements = []
    with open(file_path) as file_obj:
        lines=file_obj.readline()
        requirements = [req.replace("\n","") for req in lines]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup (
    name=PROJECT_NAME,
    version=version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")

)