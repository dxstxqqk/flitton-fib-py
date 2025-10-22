from setuptools import setup, find_packages
setup(
    name='flitton-fib-py',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    install_requires=[],
    author='dxstxqqk',
    author_email='dxstxqqk@gmail.com',
    description='A Python package for calculating Fibonacci numbers',
    url='https://github.com/dxstxqqk/flitton-fib-py',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    test_requires=['pytest'],
) 