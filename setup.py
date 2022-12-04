from setuptools import setup
from setuptools import find_namespace_packages

# Load the README file.
with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setup(

    # Define the library name, this is what is used along with `pip install`.
    name='snowflake',

    # Define the author of the repository.
    author='youssaf@',

    # Define the Author's email, so people know who to reach out to.
    author_email='bouraha.youssaf@gmail.com',

    # Define the version of this library.
    # Read this as
    #   - MAJOR VERSION 0
    #   - MINOR VERSION 1
    #   - MAINTENANCE VERSION 0
    version='0.1.0',

    # Here is a small description of the library. This appears
    # when someone searches for the library on https://pypi.org/search.
    description='A python snowflake  library  which  uses a randomly chosen color for each snowflake.',


    # These are the dependencies the library needs in order to run.
    install_requires=[
        'numpy',
        'turtles',
    ],


)