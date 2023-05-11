from setuptools import setup, find_packages

setup(
    name='spotipy-pandas',
    version='0.1',
    description='A Spotipy-based Pandas wrapper for Spotify API calls',
    url='https://github.com/opbenesh/spotipy-pandas',
    author='Ben Esh',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Spotify',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='spotify pandas',
    packages=find_packages(),
    python_requires='>=3.7',
)
