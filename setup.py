from setuptools import setup

requirements = [
    # package requirements go here
]

setup(
    name='condademo',
    version='0.0.1',
    #cmdclass=versioneer.get_cmdclass(),
    description="Short description",
    license="MIT",
    author="Full Name",
    author_email='Email Address',
    url='https://github.com/Destination github org or username/condademo',
    packages=['condademo'],
    entry_points={
        'console_scripts': [
            'condademo=condademo.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='condademo',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
