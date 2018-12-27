from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='norris-cli',
    version='2.0',
    description="A simple cli app that brightens up your day with Chuck Norris jokes.",
    long_description=long_description,
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
