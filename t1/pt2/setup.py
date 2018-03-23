from setuptools import find_packages, setup

setup(
    name='gomoku',
    packages=find_packages(),
    entry_points={
        'gui_scripts': [
            'gomoku = gomoku.__main__:run'
        ],
    },
    install_requires=[
        'PyQt5',
        'wheel',
        'pytest'
    ],
)
