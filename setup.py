from setuptools import Extension, setup

setup(
    name='fastlz',
    version='0.5.0',
    ext_modules = [
        Extension(
            name='fastlz',
            sources=['fastlz.c', 'fastlz/fastlz.c'],
            include_dirs=['fastlz']
        )
    ]
)
