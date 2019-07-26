from setuptools import setup

setup(
    name="test",
    version="0.1.0",
    description="Help you to build groups from some data randomly.",
    long_description=open('README.md').read(),
    author='Jho Lee',
    author_email="JhoLee.se@gmail.com",
    license='MIT',

    install_requires=[],
    packages="random_group_builder",
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
