# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['idict',
 'idict.core',
 'idict.data',
 'idict.function',
 'idict.parameter',
 'idict.persistence']

package_data = \
{'': ['*']}

install_requires = \
['datasets>=1.16.1,<2.0.0',
 'dill>=0.3.4,<0.4.0',
 'garoupa>=2.211207.7,<3.0.0',
 'ldict>=3.211204.3,<4.0.0',
 'lz4>=3.1.3,<4.0.0',
 'orjson>=3.5.0,<4.0.0',
 'pdoc3>=0.10.0,<0.11.0',
 'pip>=21.3.1,<22.0.0']

extras_require = \
{'full': ['arff2pandas==1.0.1', 'pandas==1.3.4', 'SQLAlchemy>=1.4.27,<2.0.0']}

setup_kwargs = {
    'name': 'idict',
    'version': '2.211207.3',
    'description': 'Lazy dict with predictable deterministic universally unique identifiers',
    'long_description': '![test](https://github.com/davips/idict/workflows/test/badge.svg)\n[![codecov](https://codecov.io/gh/davips/idict/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/idict)\n<a href="https://pypi.org/project/idict">\n<img src="https://img.shields.io/pypi/v/idict.svg?label=release&color=blue&style=flat-square" alt="pypi">\n</a>\n![Python version](https://img.shields.io/badge/python-3.8%20%7C%203.9-blue.svg)\n[![license: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)\n\n<!--- [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5501845.svg)](https://doi.org/10.5281/zenodo.5501845) --->\n[![arXiv](https://img.shields.io/badge/arXiv-2109.06028-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2109.06028)\n[![API documentation](https://img.shields.io/badge/doc-API%20%28auto%29-a0a0a0.svg)](https://davips.github.io/idict)\n\n# idict\n\nA lazy `dict` with universally unique deterministic identifiers.\n\n[Latest release](https://pypi.org/project/idict) |\n[Current code](https://github.com/davips/idict) |\n[API documentation](https://davips.github.io/idict)\n\n### See also\n\n* identification package used by `idict`: [GaROUPa](https://pypi.org/project/garoupa)\n* only laziness, i.e., without the identification part: [ldict](https://pypi.org/project/ldict)\n\n## Overview\n\nAn `idict` is an identified `dict` with `str` keys.\nWe consider that every value is generated by a process, starting from an `empty` `idict`. The process is a sequence of\ntransformation steps done through the operator `>>`, which symbolizes the ordering of the steps.\nThere are two types of steps:\n\n* **value insertion** - represented by dict-like objects\n* **function application** - represented by ordinary Python functions\n\nFunctions, `idict`s, and values have a deterministic UUID\n(called _hosh_ - **o**perable **h**a**sh**). \nIdentifiers (hoshes) for `idict`s and values are predictable through the\nmagic available [here](https://pypi.org/project/garoupa).\nAn `idict` is completely defined by its key-value pairs so that\nit can be converted from/to a built-in `dict`.\n\nCreating an `idict` is not different from creating an ordinary `dict`. Optionally it can be created through the `>>` operator\nused after `empty` or `Ø` (usually AltGr+Shift+o in most keyboards).\nThe resulting `idict` always contains two extra entries `id` and `ids`:\n![img.png](https://raw.githubusercontent.com/davips/idict/main/examples/img.png)\n\nFunction application is done in the same way. The parameter names define the input fields, while the keys in the\nreturned `dict` define the output fields:\n![img_1.png](https://raw.githubusercontent.com/davips/idict/main/examples/img_1.png)\n\nAfter evaluated, the value will not be calculated again:\n![img_2.png](https://raw.githubusercontent.com/davips/idict/main/examples/img_2.png)\n\nFunctions can accept parameters:\n![img_3.png](https://raw.githubusercontent.com/davips/idict/main/examples/img_3.png)\n\n\n## Installation\n### ...as a standalone lib\n```bash\n# Set up a virtualenv. \npython3 -m venv venv\nsource venv/bin/activate\n\n# Install from PyPI...\npip install --upgrade pip\npip install -U idict\npip install -U idict[full]  # use the flag \'full\' for extra functionality (recommended)\n\n# ...or, install from updated source code.\npip install git+https://github.com/davips/idict\n```\n\n### ...from source\n```bash\ngit clone https://github.com/davips/idict\ncd idict\npoetry install\npoetry install -E full  # use the flag \'full\' for extra functionality (recommended)\n```\n\n## Examples\n\n**Overview**\n<details>\n<p>\n\n```python3\n\n# Creation by direct instantiation.\nfrom idict import idict\n\nd = idict(x=5, y=7, z=10)\n\n# Creation from scratch.\n# The expression \'v >> a >> b\' means "Value \'v\' will be processed by step \'a\' then \'b\'".\n# A step can be a value insertion or a function application.\nfrom idict import empty\n\nd = empty >> {"x": 5} >> {"y": 7, "z": 10}\n\n# Empty alias (\'Ø\') usage.\nfrom idict import Ø\n\nd = Ø >> {"x": 5} >> {"y": 7, "z": 10}\nprint(d)\n"""\n{\n    "x": 5,\n    "y": 7,\n    "z": 10,\n    "_id": "SV_4fc23c71a6bb954f6f2ed40e440cfd2b76087",\n    "_ids": "GS_cb0fda15eac732cb08351e71fc359058b93bd... +1 ...gk_64fdf435fc9aa10be990397ff8fa92888792c"\n}\n"""\n```\n\n```python3\n\n\n# Inverting color theme for a white background.\nfrom garoupa import setup\n\nsetup(dark_theme=False)\nd = idict(x=5, y=7, z=10)\nprint(d)\n\n\n"""\n{\n    "x": 5,\n    "y": 7,\n    "z": 10,\n    "_id": "SV_4fc23c71a6bb954f6f2ed40e440cfd2b76087",\n    "_ids": "GS_cb0fda15eac732cb08351e71fc359058b93bd... +1 ...gk_64fdf435fc9aa10be990397ff8fa92888792c"\n}\n"""\n```\n\n```python3\n\n\n# Function application.\n# The input and output fields are detected from the function signature and returned dict.\ndef f(x):\n    return {"y": x ** 2}\n\n\nd2 = d >> f\nprint(d2)\n"""\n{\n    "y": "→(x)",\n    "x": 5,\n    "z": 10,\n    "_id": "J.WMNtqzVe2LiO8Ez4Wkgpa6zsBS.o529OTeWhNo",\n    "_ids": "j6dsrYpQ-9A6BFtY5T98d-UeFJOS.o529OTeWhNo... +1 ...gk_64fdf435fc9aa10be990397ff8fa92888792c"\n}\n"""\n```\n\n```python3\n\n\n# Anonymous function application.\nd2 = d >> (lambda y: {"y": y / 5})\nprint(d)\n"""\n{\n    "x": 5,\n    "y": 7,\n    "z": 10,\n    "_id": "SV_4fc23c71a6bb954f6f2ed40e440cfd2b76087",\n    "_ids": "GS_cb0fda15eac732cb08351e71fc359058b93bd... +1 ...gk_64fdf435fc9aa10be990397ff8fa92888792c"\n}\n"""\n```\n\n```python3\n\n\n# Resulting values are evaluated lazily.\nd >>= lambda y: {"y": y / 5}\nprint(d.y)\n"""\n1.4\n"""\n```\n\n```python3\n\n\nprint(d)\n"""\n{\n    "y": 1.4,\n    "x": 5,\n    "z": 10,\n    "_id": "7uAa.i.4XbFyFY7OLx2TfzMQOeYZim1XGTCOzwYg",\n    "_ids": "S-Vd.8e3nPaYsNmqhkiGDdvZUvVZim1XGTCOzwYg... +1 ...gk_64fdf435fc9aa10be990397ff8fa92888792c"\n}\n"""\n```\n\n```python3\n\n\n# Parameterized function application.\n# "Parameters" are distinguished from "fields" by having default values.\n# When the default value is None, it means it will be explicitly defined later by \'let\'.\nfrom idict import let\n\n\ndef f(x, y, a=None, b=None):\n    return {"z": a * x ** b, "w": y ** b}\n\n\nd2 = d >> let(f, a=7, b=2)\nprint(d2)\n"""\n{\n    "z": "→(a b x y)",\n    "w": "→(a b x y)",\n    "y": 1.4,\n    "x": 5,\n    "_id": "cLQzLVSJU.N2iT-5OaZWUEnnYWUHK5qjURoS6ymD",\n    "_ids": "u-FenHI5ID.J6D-Hvj.WShqswXAgoL5sYPWsHSoF... +2 ...GS_cb0fda15eac732cb08351e71fc359058b93bd"\n}\n"""\n```\n\n```python3\n\n\n# Parameterized function application with sampling.\n# The default value is one of the following ranges, \n#     list, arithmetic progression, geometric progression.\n# Each parameter value will be sampled later.\n# A random number generator must be given.\nfrom idict import let\nfrom random import Random\n\n\ndef f(x, y, a=None, b=[1, 2, 3], ap=[1, 2, 3, ..., 10], gp=[1, 2, 4, ..., 16]):\n    return {"z": a * x ** b, "w": y ** ap * gp}\n\n\nd2 = d >> Random(0) >> let(f, a=7)\nprint(d2)\n"""\n{\n    "z": "→(a b ap gp x y)",\n    "w": "→(a b ap gp x y)",\n    "y": 1.4,\n    "x": 5,\n    "_id": "JNtKgf-Bz7S5z6QwqzWKKM5OLM4QR7OmcORBo47s",\n    "_ids": "IYglBIPS5j1KqhPE.JPs6GD89DSHtNtvgQncZo9u... +2 ...GS_cb0fda15eac732cb08351e71fc359058b93bd"\n}\n"""\n```\n\n```python3\n\nprint(d2.z)\n"""\n175\n"""\n```\n\n```python3\n\nprint(d2)\n"""\n{\n    "z": 175,\n    "w": "10.541350399999995",\n    "y": 1.4,\n    "x": 5,\n    "_id": "JNtKgf-Bz7S5z6QwqzWKKM5OLM4QR7OmcORBo47s",\n    "_ids": "IYglBIPS5j1KqhPE.JPs6GD89DSHtNtvgQncZo9u... +2 ...GS_cb0fda15eac732cb08351e71fc359058b93bd"\n}\n"""\n```\n\n\n</p>\n</details>\n\n**Identity example**\n<details>\n<p>\n\n```python3\nfrom idict import idict\n\na = idict(x=3)\nprint(a)\n"""\n{\n    "x": 3,\n    "_id": "ME_bd0a8d9d8158cdbb9d7d4c7af1659ca1dabc9",\n    "_ids": "ME_bd0a8d9d8158cdbb9d7d4c7af1659ca1dabc9"\n}\n"""\n```\n\n```python3\n\nb = idict(y=5)\nprint(b)\n"""\n{\n    "y": 5,\n    "_id": "EI_20378979f4669f2e318ae9742e214fd4880d7",\n    "_ids": "EI_20378979f4669f2e318ae9742e214fd4880d7"\n}\n"""\n```\n\n```python3\n\nprint(a >> b)\n"""\n{\n    "x": 3,\n    "y": 5,\n    "_id": "pl_bb7e60e68670707cdef7dfd31096db4c63c91",\n    "_ids": "ME_bd0a8d9d8158cdbb9d7d4c7af1659ca1dabc9 EI_20378979f4669f2e318ae9742e214fd4880d7"\n}\n"""\n```\n\n\n</p>\n</details>\n\n**Merging two idicts**\n<details>\n<p>\n\n```python3\nfrom idict import idict\n\na = idict(x=3)\nprint(a)\n"""\n{\n    "x": 3,\n    "_id": "ME_bd0a8d9d8158cdbb9d7d4c7af1659ca1dabc9",\n    "_ids": "ME_bd0a8d9d8158cdbb9d7d4c7af1659ca1dabc9"\n}\n"""\n```\n\n```python3\n\nb = idict(y=5)\nprint(b)\n"""\n{\n    "y": 5,\n    "_id": "EI_20378979f4669f2e318ae9742e214fd4880d7",\n    "_ids": "EI_20378979f4669f2e318ae9742e214fd4880d7"\n}\n"""\n```\n\n```python3\n\nprint(a >> b)\n"""\n{\n    "x": 3,\n    "y": 5,\n    "_id": "pl_bb7e60e68670707cdef7dfd31096db4c63c91",\n    "_ids": "ME_bd0a8d9d8158cdbb9d7d4c7af1659ca1dabc9 EI_20378979f4669f2e318ae9742e214fd4880d7"\n}\n"""\n```\n\n\n</p>\n</details>\n\n**Lazily applying functions to idict**\n<details>\n<p>\n\n```python3\nfrom idict import idict\n\na = idict(x=3)\nprint(a)\n"""\n{\n    "x": 3,\n    "_id": "ME_bd0a8d9d8158cdbb9d7d4c7af1659ca1dabc9",\n    "_ids": "ME_bd0a8d9d8158cdbb9d7d4c7af1659ca1dabc9"\n}\n"""\n```\n\n```python3\n\na = a >> idict(y=5) >> {"z": 7} >> (lambda x, y, z: {"r": x ** y // z})\nprint(a)\n"""\n{\n    "r": "→(x y z)",\n    "x": 3,\n    "y": 5,\n    "z": 7,\n    "_id": "kgdz8xfS7IuGtukIPe37KhAUrB2P4S3OFdPs8Gab",\n    "_ids": "CXqa2zRRNd7Aj5wI8JTJ0O-7ML0P4S3OFdPs8Gab... +2 ...ZN_eccacd999c26ce18c98f9a17a6f47adcf162a"\n}\n"""\n```\n\n```python3\n\nprint(a.r)\n"""\n34\n"""\n```\n\n```python3\n\nprint(a)\n"""\n{\n    "r": 34,\n    "x": 3,\n    "y": 5,\n    "z": 7,\n    "_id": "kgdz8xfS7IuGtukIPe37KhAUrB2P4S3OFdPs8Gab",\n    "_ids": "CXqa2zRRNd7Aj5wI8JTJ0O-7ML0P4S3OFdPs8Gab... +2 ...ZN_eccacd999c26ce18c98f9a17a6f47adcf162a"\n}\n"""\n```\n\n\n</p>\n</details>\n\n**Parameterized functions and sampling**\n<details>\n<p>\n\n```python3\nfrom random import Random\n\nfrom idict import Ø, let\n\n\n# A function provide input fields and, optionally, parameters.\n# For instance:\n# \'a\' is sampled from an arithmetic progression\n# \'b\' is sampled from a geometric progression\n# Here, the syntax for default parameter values is borrowed with a new meaning.\ndef fun(x, y, a=[-100, -99, -98, ..., 100], b=[0.0001, 0.001, 0.01, ..., 100000000]):\n    return {"z": a * x + b * y}\n\n\ndef simplefun(x, y):\n    return {"z": x * y}\n\n\n# Creating an empty idict. Alternatively: d = idict().\nd = Ø >> {}\nd.show(colored=False)\n"""\n{\n    "_id": "0000000000000000000000000000000000000000",\n    "_ids": {}\n}\n"""\n```\n\n```python3\n\n# Putting some values. Alternatively: d = idict(x=5, y=7).\nd["x"] = 5\nd["y"] = 7\nprint(d)\n"""\n{\n    "x": 5,\n    "y": 7,\n    "_id": "BB_fad4374ca911f344859dab8e4b016ba2fe65b",\n    "_ids": "GS_cb0fda15eac732cb08351e71fc359058b93bd WK_6ba95267cec724067d58b3186ecbcaa4253ad"\n}\n"""\n```\n\n```python3\n\n# Parameter values are uniformly sampled.\nd1 = d >> simplefun\nprint(d1)\nprint(d1.z)\n"""\n{\n    "z": "→(x y)",\n    "x": 5,\n    "y": 7,\n    "_id": "VqfQeuBWL7Xv1FwWe6pzgqJwclRMPNZuFtrAIt6g",\n    "_ids": "9KKem6QL-I8C0Yk0q3URBt-aNXHMPNZuFtrAIt6g... +1 ...WK_6ba95267cec724067d58b3186ecbcaa4253ad"\n}\n35\n"""\n```\n\n```python3\n\nd2 = d >> simplefun\nprint(d2)\nprint(d2.z)\n"""\n{\n    "z": "→(x y)",\n    "x": 5,\n    "y": 7,\n    "_id": "VqfQeuBWL7Xv1FwWe6pzgqJwclRMPNZuFtrAIt6g",\n    "_ids": "9KKem6QL-I8C0Yk0q3URBt-aNXHMPNZuFtrAIt6g... +1 ...WK_6ba95267cec724067d58b3186ecbcaa4253ad"\n}\n35\n"""\n```\n\n```python3\n\n# Parameter values can also be manually set.\ne = d >> let(fun, a=5, b=10)\nprint(e.z)\n"""\n95\n"""\n```\n\n```python3\n\n# Not all parameters need to be set.\ne = d >> Random() >> let(fun, a=5)\nprint("e =", e.z)\n"""\ne = 700000025.0\n"""\n```\n\n```python3\n\n# Each run will be a different sample for the missing parameters.\ne = e >> Random() >> let(fun, a=5)\nprint("e =", e.z)\n"""\ne = 7025.0\n"""\n```\n\n```python3\n\n# We can define the initial state of the random sampler.\n# It will be in effect from its location place onwards in the expression.\ne = d >> Random(0) >> let(fun, a=5)\nprint(e.z)\n"""\n725.0\n"""\n```\n\n```python3\n\n# All runs will yield the same result,\n# if starting from the same random number generator seed.\ne = e >> Random(0) >> let(fun, a=[555, 777])\nprint("Let \'a\' be a list:", e.z)\n"""\nLet \'a\' be a list: 700003885.0\n"""\n```\n\n```python3\n\n# Reproducible different runs are achievable by using a single random number generator.\ne = e >> Random(0) >> let(fun, a=[5, 25, 125, ..., 10000])\nprint("Let \'a\' be a geometric progression:", e.z)\n"""\nLet \'a\' be a geometric progression: 700003125.0\n"""\n```\n\n```python3\nrnd = Random(0)\ne = d >> rnd >> let(fun, a=5)\nprint(e.z)\ne = d >> rnd >> let(fun, a=5)  # Alternative syntax.\nprint(e.z)\n"""\n725.0\n700000025.0\n"""\n```\n\n```python3\n\n# Output fields can be defined dynamically through parameter values.\n# Input fields can be defined dynamically through kwargs.\ncopy = lambda source=None, target=None, **kwargs: {target: kwargs[source]}\nd = empty >> {"x": 5}\nd >>= let(copy, source="x", target="y")\nprint(d)\nd.evaluate()\nprint(d)\n\n"""\n{\n    "y": "→(source target x)",\n    "x": 5,\n    "_id": "xmcjrFNT-2nEr3vizzx-44QwV5kwDfaOqWWvzOrq",\n    "_ids": "3Tv6p5fZ936EK1DUkkcYAgWPbrmwDfaOqWWvzOrq GS_cb0fda15eac732cb08351e71fc359058b93bd"\n}\n{\n    "y": 5,\n    "x": 5,\n    "_id": "xmcjrFNT-2nEr3vizzx-44QwV5kwDfaOqWWvzOrq",\n    "_ids": "3Tv6p5fZ936EK1DUkkcYAgWPbrmwDfaOqWWvzOrq GS_cb0fda15eac732cb08351e71fc359058b93bd"\n}\n"""\n```\n\n\n</p>\n</details>\n\n**Composition of sets of functions**\n<details>\n<p>\n\n```python3\nfrom random import Random\n\nfrom idict import Ø\n\n\n# A multistep process can be defined without applying its functions\n\n\ndef g(x, y, a=[1, 2, 3, ..., 10], b=[0.00001, 0.0001, 0.001, ..., 100000]):\n    return {"z": a * x + b * y}\n\n\ndef h(z, c=[1, 2, 3]):\n    return {"z": c * z}\n\n\n# In the \'idict\' framework \'data is function\',\n# so the alias Ø represents the \'empty data object\' and the \'reflexive function\' at the same time.\n# In other words: \'inserting nothing\' has the same effect as \'doing nothing\'.\nfun = Ø >> g >> h  # \'empty\' or \'Ø\' enable the cartesian product of the subsequent sets of functions within the expression.\nprint(fun)\n"""\n«λ{} × λ»\n"""\n```\n\n```python3\n\n# Before a function is applied to a dict-like, the function free parameters remain unsampled.\n# The result is an ordered set of composite functions.\nd = {"x": 5, "y": 7} >> (Random(0) >> fun)\nprint(d)\n"""\n{\n    "z": "→(c z→(a b x y))",\n    "x": 5,\n    "y": 7,\n    "_id": "YZWooP03q0mFec8tjNwy3YuAohamevfjG3VAFXL-",\n    "_ids": "5PKBLX4-dGDGHUifvK.QYVLeZTgmevfjG3VAFXL-... +1 ...WK_6ba95267cec724067d58b3186ecbcaa4253ad"\n}\n"""\n```\n\n```python3\n\nprint(d.z)\n"""\n105.0\n"""\n```\n\n```python3\n\nd = {"x": 5, "y": 7} >> (Random(0) >> fun)\nprint(d.z)\n"""\n105.0\n"""\n```\n\n```python3\n\n# Reproducible different runs by passing a stateful random number generator.\nrnd = Random(0)\ne = d >> rnd >> fun\nprint(e.z)\n"""\n105.0\n"""\n```\n\n```python3\n\ne = d >> rnd >> fun\nprint(e.z)\n"""\n14050.0\n"""\n```\n\n```python3\n\n# Repeating the same results.\nrnd = Random(0)\ne = d >> rnd >> fun\nprint(e.z)\n"""\n105.0\n"""\n```\n\n```python3\n\ne = d >> rnd >> fun\nprint(e.z)\n"""\n14050.0\n"""\n```\n\n\n</p>\n</details>\n\n<persistence>\n\n## Concept\n\nAn `idict` is like a common Python `dict`, with extra functionality and lazy. \nIt is a mapping between string keys, called\nfields, and any serializable (pickable) object.\nEach `idict` has two extra entries: `id` (identifier) and `ids` (value identifiers).\n\nA custom 40-digit unique identifier (see [GaROUPa](https://pypi.org/project/garoupa))\ncan be provided as an attribute for each function.\nValue objects can have custom identifiers as well, if provided whithin the entry `ids`. \n\nOtherwise, identifiers for functions and values will be calculated through blake3 hashing of their content.\nFor functions, the bytecode is used as content. \nFor this reason, such functions should be simple, with minimal external dependencies or\nwith their import statements inside the function body.\nThis decreases the odds of using two functions with identical local code (and, therefore, identical identifiers) \nperforming different calculations.\n\n## Grants\n\nThis work was supported by Fapesp under supervision of\nProf. André C. P. L. F. de Carvalho at CEPID-CeMEAI (Grants 2013/07375-0 – 2019/01735-0)\nuntil 2021-03-31.\n',
    'author': 'davips',
    'author_email': 'dpsabc@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
