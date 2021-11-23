from setuptools import setup

setup(
    name='proxypool',
    version='V2.0.0',
    packages=['proxyPool', 'schedule'],
    url='https://github.com/ArdenteX/flaskProject',
    license='apache 2.0',
    author='ArdentXu',
    author_email='694022879@qq.com',
    description='A Cross-platform proxy pool.',
    py_modules=['run'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'aiohttp',
        'requests',
        'bs4',
        'flask',
        'redis',
        'lxml'
    ],
    entry_points={
        'console_scripts': ['proxypool_run=run:cli']
    },
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)