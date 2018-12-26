import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='norris-cli',
    version='0.1',
    description="A simple cli app that brightens up your day with Chuck Norris jokes.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/wangonya/norris-cli",
    author="Kinyanjui Wangonya",
    author_email="kwangonya@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    py_modules=['norris-cli'],
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
        'halo'
    ],
    entry_points='''
        [console_scripts]
        norris-cli=app:main
    ''',
)
