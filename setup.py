# dev: 'python setup.py develop' or 'pip install -e'
from setuptools import setup, find_packages
# python setup.py check
# python setup.py --help-commands
setup(
    name='python-radio',
    version='0.1.0.dev1',
    description='Package provides command-lined interface radio.',
    url='http://github.org/jrbalderrama/python-radio',
    author='jrbalderrama',
    author_email='jrbalderrama@gmail.com',
    license='BSD License',
    keywords='console radio client',
    platforms='MacOS, POSIX',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Utilities',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        # cython is required before installing bintrees
        # python setup.py build_ext install (for local bintrees install)
        'bintrees',  # 2.0.1
        'fuzzywuzzy',  # 0.5.0
    ],
    # Install optional dependencies (without space after '.'):
    # pip install -e .[levenshtein]
    extras_require={
        'levenshtein': ["python-Levenshtein"],  # 0.12.0
    },
    package_data={
        'radio': ['stations.ini'],
    },
    # entry_points={
    #     'console_scripts': [
    #         'radio=radio:main',
    #     ],
    # },
)
