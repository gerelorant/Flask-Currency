from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='FlaskCurrency',
    version='v1.0',
    packages=['flask_currency'],
    url='https://github.com/gerelorant/Flask-Currency',
    license='MIT',
    author='Gere Lóránt',
    author_email='gerelorant@gmail.com',
    description='Currency handling extension for Flask and SQLAlchemy',
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
