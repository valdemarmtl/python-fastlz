from distutils.core import setup, Extension


setup(
    name='fastlz',
    version='0.5.0',
    description='Python wrapper for FastLZ, a lightning-fast lossless '
                'compression library.',
    author='Remus M. Prunescu',
    url='https://github.com/remusmp/python-fastlz',
    license='BSD License',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Archiving :: Compression',
        'Topic :: Utilities'
    ],
    ext_modules = [
        Extension(
            'fastlz',
            sources=['fastlz/fastlz.c'],
            include_dirs=['fastlz']
        )
    ]
)
