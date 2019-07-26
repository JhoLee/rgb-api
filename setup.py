from setuptools import setup, find_packages

setup(
    name='random-group-builder',

    version='0.0.1',
    author='Jho Lee',
    author_email='JhoLee.se@gmail.com',
    license='MIT',

    description='Help you to build groups from some data randomly.',
    long_description=open('README.md').read(),
    long_descripton_content_type="text/markdown",

    url="https://github.com/jholee/jho-rgb-api",
    packages=find_packages(),
    install_requires=[],
    keywords=['random', 'group', 'builder', 'helper', 'api', 'rgb'],
    python_requires='>=3',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
