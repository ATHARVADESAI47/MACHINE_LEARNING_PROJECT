from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [r.replace("\n", "") for r in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='ML_project',
    version='0.0.1',
    author='Atharva',
    author_email='atharvadesai05122004@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)
