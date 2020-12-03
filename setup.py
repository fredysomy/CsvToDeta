from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Fredy Somy",
    author_email="fredysomy@gmail.com",
    python_requires=">=3",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="A Lightweight tool to upload CSV files data into Deta Base.",
    install_requires=['fire','deta'],
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    
    version="1.2.0",
    keywords="csv,database,json",
    name="csvtodeta",
    packages=['src'],
    entry_points={
        'console_scripts':[
        'csvtodeta=src.cli:main']
    },
    setup_requires=[],
    url="https://github.com/fredysomy/CsvToDeta",
  
    zip_safe=False,
)
