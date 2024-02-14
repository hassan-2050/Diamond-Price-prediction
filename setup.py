
from setuptools import setup ,find_packages
from typing import List
  



def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[line.replace("/n","")for line in requirements ]
        return requirements






setup( 
    name='Diamond price pred', 
    version='0.1', 
    description='A sample Python package', 
    author='Hassan Imam', 
    author_email='syedhassan2050@gmail.com', 
    packages=find_packages(), 
    install_requires=get_requirements("/home/yoga/Documents/projects/diamond price/requirements.txt"), 
) 