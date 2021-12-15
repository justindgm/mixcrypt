
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, "mixcrypt", "__about__.py")) as f:
    exec(f.read(), about)


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    long_description=open(os.path.join(here, "README.rst")).read(),
    url=about['__uri__'],
    download_url="",
    author=about['__author__'],
    author_email=about['__email__'],
    license=about['__license__'],
    classifiers=[
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9'
    ],
    keywords="cryptography encryption homomorphic",
    packages=find_packages(),
    extras_require={
        'cli': ['click'],
        'examples': ['numpy', 'scipy', 'sklearn']
    },
    install_requires=[]
)
