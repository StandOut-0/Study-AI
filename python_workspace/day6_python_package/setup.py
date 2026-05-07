from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1.0',
    description='mypackage is a python package',
    author='Sanghee Park',
    author_email='sanghee.park@gmail.com',
    url='https://github.com/sangheepark/mypackage',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)