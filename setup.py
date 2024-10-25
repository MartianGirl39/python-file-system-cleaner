from setuptools import setup, find_packages

setup(
    name='clean_directory',
    version='0.1.0',
    description='A package to clean and organize file systems.',
    author='Jennifer Forse',
    author_email='mforsejennifer@gmail.com',
    url='https://github.com/MartianGirl39/clean_directory',  # Update with your project URL
    packages=find_packages(),  # Automatically find all packages in the directory
    install_requires=[
        # List your package dependencies here
        # e.g., 'numpy', 'pandas', etc.
    ],
    entry_points={
        'console_scripts': [
            'pyroomba=clean.clean:main',  # Adjust based on your main entry point
            'pyorganizer=organize.secretary:main'  # Adjust based on your main entry point
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python version required
)
