  
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Python Dictionary with dot notation support'
LONG_DESCRIPTION = 'Ndict which is a modified python builtin dictionary to support dot notation for accessing and setting'

# Setting up
setup(
    name="Ndict",
    version=VERSION,
    author="Noizrom",
    author_email="Noizrom@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['python', 'ndict', 'dictionary', 'dot notation', 'named dictionary'],
    classifiers=[
        "Development Status :: 1 - Done",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)