import setuptools
setuptools.setup(
    name="timeSHIT",
    packages=['timeSHIT'],
    package_dir={'timeSHIT': 'timeSHIT'},
    version="0.0.1",
    author="kaushal28",
    entry_points={'console_scripts': ['timeSHIT = timeSHIT.__main__:main' ]},
    author_email="shah.kaushal95@gmail.com",
    description="Ease the pain of logging your time in JIRA timesheets",
    install_requires=[
        'schedule == 0.6.0'
   ],
)