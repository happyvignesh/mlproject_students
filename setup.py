from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(filepath:str)->List[str]:
    '''
        this function will return the list of requirements
    '''
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

setup(
    name='students_mlproject',
    version='0.0.1',
    author='Vignesh',
    author_email='mugilvignesh31@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
