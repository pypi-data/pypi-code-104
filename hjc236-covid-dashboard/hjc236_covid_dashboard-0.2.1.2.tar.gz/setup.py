from distutils.core import setup
setup(
    name = 'hjc236_covid_dashboard',
    packages = ['hjc236_covid_dashboard'],
    version = '0.2.1.2',
    license='MIT',
    description = 'A python project which generates a web dashboard with COVID-19 data and relevant news articles.',
    long_description="file: README.md",
    long_description_content_type="text/markdown",
    author = 'hjc236',
    author_email = '',
    url = 'https://github.com/hjc236/hjc236_covid_dashboard',
    download_url = 'https://github.com/hjc236/hjc236_covid_dashboard/archive/refs/tags/v0.2.2.tar.gz',
    keywords = ['coronavirus', 'event-driven', 'dashboard'],
    install_requires=[
        'uk_covid19',
        'flask',
        'pytest'

    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)