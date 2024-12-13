from setuptools import setup, find_packages

setup(
    name="DTKit",
    version="0.3",
    description=("A package that offers new data types to use in everyday Python use."),
    author="Chase Galloway",
    author_email="chase.h.galloway21@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    Homepage = "https://github.com/chasegalloway/DTKit",
    Issues = "https://github.com/chasegalloway/DTKit/issues",
)
