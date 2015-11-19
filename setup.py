from setuptools import setup, find_packages

setup(
    name='littleweaverweb.com',
    version="0.0",
    description="Little Weaver's website",
    author='Little Weaver',
    author_email='hello@littleweaverweb.com',
    url='https://github.com/littleweaver/littleweaverweb.com',
    packages=find_packages(),
    package_data={'': ["*.*"]},
    include_package_data=True,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django'
    ]
)
