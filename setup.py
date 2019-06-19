import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timeSHIT",
    packages=['timeSHIT'],
    package_dir={'timeSHIT': 'timeSHIT'},
    version="0.0.3",
    author="kaushal28",
    entry_points={'console_scripts': ['timeSHIT = timeSHIT.__main__:main' ]},
    author_email="shah.kaushal95@gmail.com",
    description="Ease the pain of logging your time in JIRA timesheets",
    url="https://github.com/Kaushal28/Timesheet-Filler.git",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'schedule == 0.6.0'
   ],
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)