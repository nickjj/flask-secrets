from setuptools import setup


setup(
    name='Flask-Secrets',
    version='0.1.0',
    author='Nick Janetakis',
    author_email='nick.janetakis@gmail.com',
    url='https://github.com/nickjj/flask-secrets',
    description='A Flask extension to generate random secret tokens.',
    license='MIT',
    long_description=__doc__,
    packages=['flask_secrets'],
    platforms='any',
    python_requires='>=3.6',
    zip_safe=False,
    install_requires=[
        'Flask>=1.0'
    ],
    entry_points={
        'flask.commands': [
            'secrets=flask_secrets.cli:secrets'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Security :: Cryptography'
    ]
)
