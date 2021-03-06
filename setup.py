from setuptools import setup

setup(
    name='netconf-console-mely',
    version='0.1.0',    
    description='A example Python package',
    url='git@github.com:melihteke/Netconf_Console.git',
    author='melih Teke',
    author_email='melihteke@gmail.com',
    license='BSD 2-clause',
    packages=['pyexample'],
    install_requires=['netmiko',
                      'numpy',
                      'scrapli'                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
