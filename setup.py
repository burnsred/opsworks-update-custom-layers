from setuptools import setup

setup(
    name='opsworks-update-custom-layers',
    version='0.0.1',
    packages=['opsworks_update_custom_layers',],
    scripts=['bin/opsworks-update-custom-layers'],
    include_package_data=True,
    license='MIT License',
    author='Michael Bertolacci',
    author_email='michael@burnsred.com.au',
    url='',
    install_requires=[
        'create-opsworks-deployment-and-wait==0.0.2'
    ],
    dependency_links=[
        'https://github.com/burnsred/opsworks-create-deployment-and-wait/tarball/master#egg=create-opsworks-deployment-and-wait-0.0.2',
    ],
    long_description=open('README.md').read(),
)