from setuptools import setup, find_packages
# import os, sys


def parse_requirements(requirements):
    # load from requirements.txt
    with open(requirements) as f:
        lines = [l for l in f]
        # remove spaces
        stripped = map((lambda x: x.strip()), lines)
        # remove comments
        nocomments = filter((lambda x: not x.startswith('#')), stripped)
        # remove empty lines
        reqs = filter((lambda x: x), nocomments)
        return reqs

PACKAGE_NAME = "PyDejavu"
PACKAGE_VERSION = "0.1.3"
SUMMARY = 'Audio Fingerprinting'
DESCRIPTION = """
Audio fingerprinting
"""
REQUIREMENTS = parse_requirements("requirements.txt")

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description=SUMMARY,
    long_description=DESCRIPTION,
    author='Will Drevo',
    author_email='will.drevo@gmail.com',
    maintainer="Will Drevo",
    maintainer_email="will.drevo@gmail.com",
    url='http://github.com/tuxdna/dejavu',
    license='MIT License',
    include_package_data=True,
    packages=find_packages(),
    platforms=['Unix'],
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords="python, audio, fingerprinting, music, numpy, landmark",
)
