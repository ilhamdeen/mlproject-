from setuptools import find_packages,setup
from typing import List

HYPEN_E_DON='-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DON in requirements:
            requirements.remove(HYPEN_E_DON)
    return requirements
setup(
name= 'mlproject2',
version= '0.0.1',
author= 'Ilham',
author_email= 'deenilham@gmail.com',
packages= find_packages(),
install_requires=get_requirements('requirements.txt')



)