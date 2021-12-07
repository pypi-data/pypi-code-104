# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tailwind',
 'tailwind.app_template_v2.{{cookiecutter.app_name}}',
 'tailwind.management',
 'tailwind.management.commands',
 'tailwind.templatetags']

package_data = \
{'': ['*'],
 'tailwind': ['app_template_v2/cookiecutter.json', 'templates/tailwind/tags/*'],
 'tailwind.app_template_v2.{{cookiecutter.app_name}}': ['static_src/*',
                                                        'static_src/src/*',
                                                        'templates/*']}

install_requires = \
['cookiecutter>=1.7.3,<2.0.0', 'django>=4.0']

setup_kwargs = {
    'name': 'django-tailwind',
    'version': '2.3.0',
    'description': 'Tailwind CSS Framework for Django projects',
    'long_description': '# Tailwind CSS integration for Django a.k.a. Django + Tailwind = 💚\n![Django Tailwind Demo](https://raw.githubusercontent.com/timonweb/django-tailwind/master/docs/django-tailwind-demo-800.gif)\n\n## Goal\nThis project aims to provide a comfortable way of using the *Tailwind CSS* framework within a Django project.\n\n## Features\n* An opinionated *Tailwind CSS* setup that makes your life easier;\n* Hot reloading of CSS, configuration files, and *Django* templates. No more manual page refreshes!\n* Out of the box support for CSS imports, SASS-like variables, and nesting;\n* Includes official *Tailwind CSS* plugins like *typography*, *form*, *line-clamp*, and *aspect-ratio*;\n\n## Requirements\nPython 3.7 or newer with Django >= 2.2 or newer.\n\n## Documentation\nThe full documentation is at https://django-tailwind.readthedocs.io/\n\n## Installation\nVia PIP:\n```bash\npip install django-tailwind\n```\n\nCheck docs for the [Installation](https://django-tailwind.readthedocs.io/en/latest/installation.html) instructions.\n\n## Migration from *Django-Tailwind v1.x*:\nCheck docs for the [Migration](https://django-tailwind.readthedocs.io/en/latest/migration.html) instructions.\n\n## Bugs and suggestions\nIf you have found a bug, please use the issue tracker on GitHub.\n\n[https://github.com/timonweb/django-tailwind/issues](https://github.com/timonweb/django-tailwind/issues)\n\n2019 - 2021 (c) [Tim Kamanin - A Full Stack Django Developer](https://timonweb.com)\n',
    'author': 'Tim Kamanin',
    'author_email': 'tim@timonweb.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/timonweb/django-tailwind',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
