from setuptools import setup, find_packages

setup(
    name="demo",
    version="1.0",
    keywords=("demo", "xxx"),
    description="demo sdk",
    long_description="demo sdk for python",
    license="MIT Licence",

    url="http://demo.com",
    author="danao",
    author_email="danao@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[],

    scripts=[],
    entry_points={
        'console_scripts': [
            'demo = main'
        ]
    }
)
