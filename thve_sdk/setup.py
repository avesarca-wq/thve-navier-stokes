from setuptools import setup, find_packages

setup(
    name='thve_sdk',
    version='2.0.0',
    packages=find_packages(),
    description='Topological High-Dimensional Vector Engine SDK',
    author='Ricardo Dutra Pereira',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
