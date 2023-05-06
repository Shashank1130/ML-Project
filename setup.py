# The setup script is the centre of all activity in building, distributing, and installing modules using the Distutils. 


from setuptools import find_packages, setup # Automatically find packages that we need in the entire ML application
from typing import List



HYPEN_E_DOT='-e .'

# get_requirements function
def get_requirements(file_path:str)->List[str]:
    """
        This function will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements

        


setup(
    name='mlproject',
    version='0.1.1',
    author='Shashank',
    author_email='shashankdubey1130@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt') 
)