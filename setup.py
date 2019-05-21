from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='webhose_api_image_search',
    packages=['webhose_api_image_search'],
    version='0.4',
    author='Omer Turner',
    author_email='omer@webhose.io',
    url='https://github.com/Webhose/webhoseio-python',
    license='MIT',
    description='Access image metadata and labels using the Webhose API image recognition feature',
    long_description="",
    install_requires=[
        "webhoseio==0.5"
    ],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    )
)
