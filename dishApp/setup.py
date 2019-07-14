from setuptools import setup, find_packages

setup(
    name='python-package-example',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Application to help with dishes',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/iqaz100/dishApp',
    author='Piotr Lasek',
    author_email='235690@student.pwr.edu.pl'
)