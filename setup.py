from setuptools import setup


setup(
    name="django-sms-gateway",
    version="0.1.5",
    description="django generic sms through gateway",
    url="http://bitbucket.org/schinckel/django-sms-gateway",
    author="Matthew Schinckel",
    author_email="matt@schinckel.net",
    packages=[
        "sms",
        "sms.migrations",
        "sms.models",
        "sms.management",
        "sms.management.commands",
    ],
    package_data={
        "": [
            "fixtures/*",
        ]
    },
    install_requires=[
        'requests>=2.2',
        'django-jsonfield>=0.9.13',
        'django-picklefield>=0.3.1',
        'django-uuidfield>=0.5.0',
    ],
    classifiers=[
        'Programming Language :: Python',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
