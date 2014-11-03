from setuptools import setup

setup(
    name='opsworks-update-custom-layers',
    version='0.0.3',
    packages=['opsworks_update_custom_layers',],
    scripts=['bin/opsworks-update-custom-layers'],
    include_package_data=True,
    license='MIT License',
    author='Michael Bertolacci',
    author_email='michael@burnsred.com.au',
    url='',
    long_description=open('README.md').read(),
    install_requires=['boto==2.34.0'],
)