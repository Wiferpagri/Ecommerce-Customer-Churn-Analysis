import os

from setuptools import setup, find_packages

def readme() -> str:
    """Utility function to read the README.md.

    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.

    Args:
        nothing

    Returns:
        String of readed README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='ecommerce_customer_churn_prevention',
    version='0.1.0',
    author='Wiferpagri',
    author_email='wiferpagri19@gmail.com',
    description='Analysis and design a model able to detect when a customer will churn, and determine their reasons, in order to reduce churn.',
    python_requires='>=3',
    license='',
    url='',
    packages=find_packages(),
    long_description=readme(),
)