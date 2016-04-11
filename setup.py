from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='ped',
        packages=find_packages(),
        version='0.1.0',
        description='Pedigree (ped file) representation and functions.',
        long_description='',
        url='https://github.com/asalomatov/ped',
        author='Andrei Salomatov',
        license='MIT',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Operating System :: OS Independent',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License', 
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
            ],
        install_requires=[
            'pandas>=0.17',
        ],
)
