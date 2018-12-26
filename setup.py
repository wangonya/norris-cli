from setuptools import setup

setup(
    name='norris-cli',
    version='0.1',
    py_modules=['norris-cli'],
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