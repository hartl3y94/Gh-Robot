from setuptools import find_packages
import setuptools

setuptools.setup(
    name="Gh-Robot",
    version="V0.0.1",
    author="CoolPlayLin",
    author_email="help@api-coolplaylin.eu.org",
    description="A Github API-based Robot",
    long_description="long_description",
    long_description_content_type='text/markdown',
    license='GPL V3.0',
    project_urls={
        "Bug Report": "https://github.com/CoolPlayLin/Gh-Robot/issues/new/choose"
    },
    url="https://github.com/CoolPlayLin/Gh-Robot",
    install_requires=[
        'requests>=2.28.1'
        'wget>=3.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL V3.0"
    ]
)