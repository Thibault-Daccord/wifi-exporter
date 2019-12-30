from setuptools import setup, find_packages

setup(
    name='wifi-password-exporter',
    version='1.0',
    description='Save & restore your linux wifi password',
    url='https://github.com/Thibault-Daccord/wifi-password-exporter',
    author='Thibault Daccord',
    author_email='please use github message',
    license='Apache License 2.0',
    install_requires=['tkinter'],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['rq=src.main:display_quote']
    )
)
