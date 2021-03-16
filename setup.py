import setuptools
from pathlib import Path

setuptools.setup(
    name="mdcrawler",
    version="1.1.7",
    packages=setuptools.find_packages(),
    description=('Mildom(https://www.mildom.com/) crawler written in Python.'),
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    license="MIT",
    maintainer="kthimuo",
    author='kthimuo',
    url='https://github.com/kthimuo/mildom-crawler',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
)
