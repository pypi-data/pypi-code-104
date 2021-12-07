# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['garoupa',
 'garoupa.algebra',
 'garoupa.algebra.abs',
 'garoupa.algebra.cyclic',
 'garoupa.algebra.dihedral',
 'garoupa.algebra.matrix',
 'garoupa.algebra.product',
 'garoupa.algebra.symmetric',
 'garoupa.misc',
 'garoupa.misc.encoding']

package_data = \
{'': ['*']}

install_requires = \
['ansi2html>=1.6.0,<2.0.0',
 'blake3>=0.2.0,<0.3.0',
 'colored==1.4.2',
 'wheel>=0.37.0,<0.38.0']

extras_require = \
{'algebra': ['progress>=1.6,<2.0', 'pathos>=0.2.8,<0.3.0'],
 'experiments': ['bigfloat>=0.4.0,<0.5.0']}

setup_kwargs = {
    'name': 'garoupa',
    'version': '2.211207.1',
    'description': 'Predictable operable hash-based identifiers and abstract algebra groups',
    'long_description': '![test](https://github.com/davips/garoupa/workflows/test/badge.svg)\n[![codecov](https://codecov.io/gh/davips/garoupa/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/garoupa)\n<a href="https://pypi.org/project/garoupa">\n<img src="https://img.shields.io/pypi/v/garoupa.svg?label=release&color=blue&style=flat-square" alt="pypi">\n</a>\n![Python version](https://img.shields.io/badge/python-3.8%20%7C%203.9-blue.svg)\n[![license: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)\n\n[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5501845.svg)](https://doi.org/10.5281/zenodo.5501845)\n[![arXiv](https://img.shields.io/badge/arXiv-2109.06028-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2109.06028)\n[![API documentation](https://img.shields.io/badge/doc-API%20%28auto%29-a0a0a0.svg)](https://davips.github.io/garoupa)\n\n\n# GaROUPa - Identification based on group theory\n \n\n\nGaROUPa solves the identification problem of multi-valued objects or sequences of events.<br>This [Python library](https://pypi.org/project/garoupa) / [code](https://github.com/davips/garoupa) provides a reference implementation for the UT*.4 specification presented [here](https://arxiv.org/abs/2109.06028).  | ![fir0002  flagstaffotos [at] gmail.com Canon 20D + Tamron 28-75mm f/2.8, GFDL 1.2 &lt;http://www.gnu.org/licenses/old-licenses/fdl-1.2.html&gt;, via Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Malabar_grouper_melb_aquarium.jpg/256px-Malabar_grouper_melb_aquarium.jpg)\n:-------------------------:|:-------------------------:\n\nWe adopt a novel paradigm to universally unique identification (UUID), making identifiers deterministic and predictable, \neven before an object is generated by a (possibly costly) process.   \nHere, data versioning and composition of processing steps are directly mapped as simple operations over identifiers.\nWe call each of the latter a Hosh, i.e., an identifier is an _**o**perable **h**a**sh**_.\n\nA complete implementation of the remaining ideas from the [paper](https://arxiv.org/abs/2109.06028) is provided in this\n[cacheable lazy dict](https://pypi.org/project/ldict/2.211016.3) which depends on GaROUPa and serves as an advanced usage example.\n<br>\nA more robust (entirely rewritten) version is available in the package [idict](https://pypi.org/project/idict).\n\n## Overview\nA product of identifiers produces a new identifier as shown below, where sequences of bytes (`b"..."`) are passed to simulate binary objects to be hashed.\n\n![img.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img.png) | New identifiers are easily <br> created from the identity <br> element `ø`. Also available as `identity` for people <br>or systems allergic to <br>utf-8 encoding.\n-------------------------|-------------------------\n\n![img_1.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_1.png) | Operations can be reverted by the inverse of the identifier.\n-------------------------|-------------------------\n\n![img_2.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_2.png) | Operations are associative. <br>They are order-sensitive by default, <br>in which case they are called _ordered_ ids.\n-------------------------|-------------------------\n\nHowever, order-insensitive (called _unordered_) and order-insensitive-among-themselves (called _hybrid_) identifiers are also available. | .\n-------------------------|-------------------------\n![img_3.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_3.png) | .\n\nThis is how they affect each other: | .\n-------------------------|-------------------------\n![img_4.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_4.png) | .\n\nThe chance of collision is determined by the number of possible identifiers of each type.\nSome versions are provided, e.g.: UT32.4, UT40.4 (default), UT64.4.\nThey can be easily implemented in other languages and are \nintended to be a specification on how to identify multi-valued objects and multi-step processes.\nUnordered ids use a very narrow range of the total number of identifiers.\nThis is not a problem as they are not very useful.\n\nOne use for unordered ids could be the embedding of authorship or other metadata into an object without worrying about the timing, since the resulting id will remain the same, no matter when the unordered id is operated with the id of the object under construction. | . \n-------------------------|-------------------------\n![img_5.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_5.png) | . \n\nConversely, hybrid ids are excelent to represent values in a data structure like a map, \nsince the order is not relevant when the consumer process looks up for keys, not indexes.\nConverselly, a chain of a data processing functions usually implies one step is dependent on the result of the previous step.\nThis makes ordered ids the perfect fit to identify functions (and also their composition, as a consequence).\n\n### Relationships can also be represented\nHere is another possible use. ORCIDs are managed unique identifiers for researchers.\nThey can be directly used as digests to create operable identifiers.\nWe recommend the use of 40 digits to allow operations with SHA-1 hashes. \nThey are common in version control repositories among other uses.\n![img_orcid.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_orcid.png)\n\nUnordered relationships are represented by hybrid ids.\nAutomatic transparent conversion between ORCID dashes by a hexdecimal character can be implemented in the future if needed.\n![img_orcid-comm.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_orcid-comm.png)\n\n## More info\nAside from the [paper](https://arxiv.org/abs/2109.06028), [PyPI package](https://pypi.org/project/garoupa) \nand [GitHub repository](https://github.com/davips/garoupa), \none can find more information, at a higher level application perspective, \nin this presentation:\n![image](https://raw.githubusercontent.com/davips/garoupa/14cb45b888eb8a18ae093d200075c1a8a7e9cacb/examples/capa-slides-gdocs.png)\nA lower level perspective is provided in the [API documentation](https://davips.github.io/garoupa).\n\n## Python installation\n### from package\n```bash\n# Set up a virtualenv. \npython3 -m venv venv\nsource venv/bin/activate\n\n# Install from PyPI\npip install garoupa\n```\n\n### from source\n```bash\ngit clone https://github.com/davips/garoupa\ncd garoupa\npoetry install\n```\n\n### Examples\nSome usage examples.\n\n**Basic operations**\n<details>\n<p>\n\n```python3\nfrom garoupa import Hosh, ø  # ø is a shortcut for identity (AltGr+O in most keyboards)\n\n# Hoshes (operable hash-based elements) can be multiplied.\na = Hosh(content=b"Some large binary content...")\nb = Hosh(content=b"Some other binary content. Might be, e.g., an action or another large content.")\nc = a * b\nprint(f"{a} * {b} = {c}")\n"""\n8CG9so9N1nQ59uNO8HGYcZ4ExQW5Haw4mErvw8m8 * 7N-L-10JS-H5DN0-BXW2e5ENWFQFVWswyz39t8s9 = z3EgxfisgqbNXBd0eqDuFiaTblBLA5ZAUbvEZgOh\n"""\n```\n\n```python3\nprint(~b)\n# Multiplication can be reverted by the inverse hosh. Zero is the identity hosh.\nprint(f"{b} * {~b} = {b * ~b} = 0")\n"""\nQ6OjmYZSJ8pB3ogBVMKBOxVp-oZ80czvtUrSyTzS\n7N-L-10JS-H5DN0-BXW2e5ENWFQFVWswyz39t8s9 * Q6OjmYZSJ8pB3ogBVMKBOxVp-oZ80czvtUrSyTzS = 0000000000000000000000000000000000000000 = 0\n"""\n```\n\n```python3\n\nprint(f"{b} * {ø} = {b * ø} = b")\n"""\n7N-L-10JS-H5DN0-BXW2e5ENWFQFVWswyz39t8s9 * 0000000000000000000000000000000000000000 = 7N-L-10JS-H5DN0-BXW2e5ENWFQFVWswyz39t8s9 = b\n"""\n```\n\n```python3\n\nprint(f"{c} * {~b} = {c * ~b} = {a} = a")\n"""\nz3EgxfisgqbNXBd0eqDuFiaTblBLA5ZAUbvEZgOh * Q6OjmYZSJ8pB3ogBVMKBOxVp-oZ80czvtUrSyTzS = 8CG9so9N1nQ59uNO8HGYcZ4ExQW5Haw4mErvw8m8 = 8CG9so9N1nQ59uNO8HGYcZ4ExQW5Haw4mErvw8m8 = a\n"""\n```\n\n```python3\n\nprint(f"{~a} * {c} = {~a * c} = {b} = b")\n"""\nRNvSdLI-5RiBBGL8NekctiQofWUIeYvXFP3wvTFT * z3EgxfisgqbNXBd0eqDuFiaTblBLA5ZAUbvEZgOh = 7N-L-10JS-H5DN0-BXW2e5ENWFQFVWswyz39t8s9 = 7N-L-10JS-H5DN0-BXW2e5ENWFQFVWswyz39t8s9 = b\n"""\n```\n\n```python3\n\n# Division is shorthand for reversion.\nprint(f"{c} / {b} = {c / b} = a")\n"""\nz3EgxfisgqbNXBd0eqDuFiaTblBLA5ZAUbvEZgOh / 7N-L-10JS-H5DN0-BXW2e5ENWFQFVWswyz39t8s9 = 8CG9so9N1nQ59uNO8HGYcZ4ExQW5Haw4mErvw8m8 = a\n"""\n```\n\n```python3\n\n# Hosh multiplication is not expected to be commutative.\nprint(f"{a * b} != {b * a}")\n"""\nz3EgxfisgqbNXBd0eqDuFiaTblBLA5ZAUbvEZgOh != wwSd0LaGvuV0W-yEOfgB-yVBMlNLA5ZAUbvEZgOh\n"""\n```\n\n```python3\n\n# Hosh multiplication is associative.\nprint(f"{a * (b * c)} = {(a * b) * c}")\n"""\nRuTcC4ZIr0Y1QLzYmytPRc087a8cbbW9Nj-gXxAz = RuTcC4ZIr0Y1QLzYmytPRc087a8cbbW9Nj-gXxAz\n"""\n```\n\n\n</p>\n</details>\n\n### Examples (abstract algebra)\nAlthough not the focus of the library, GaROUPa hosts also some niceties for group theory experimentation.\nSome examples are provided below.\n\n**Abstract algebra module**\n<details>\n<p>\n\n```python3\nfrom itertools import islice\nfrom math import factorial\n\nfrom garoupa.algebra.cyclic import Z\nfrom garoupa.algebra.dihedral import D\nfrom garoupa.algebra.symmetric import Perm\nfrom garoupa.algebra.symmetric import S\n\n# Direct product between:\n#   symmetric group S4;\n#   cyclic group Z5; and,\n#   dihedral group D4.\nG = S(4) * Z(5) * D(4)\nprint(G)\n"""\nS4×Z5×D4\n"""\n```\n\n```python3\n\n# Operating over 5 sampled pairs.\nfor a, b in islice(zip(G, G), 0, 5):\n    print(a, "*", b, "=", a * b, sep="\\t")\n"""\n«[0, 1, 3, 2], 3, dr3»\t*\t«[1, 2, 0, 3], 0, dr7»\t=\t«[1, 3, 0, 2], 3, dr2»\n«[2, 0, 1, 3], 3, ds6»\t*\t«[1, 2, 0, 3], 1, ds5»\t=\t«[0, 1, 2, 3], 4, dr1»\n«[2, 1, 0, 3], 3, dr5»\t*\t«[1, 0, 2, 3], 3, dr0»\t=\t«[1, 2, 0, 3], 1, dr1»\n«[2, 3, 0, 1], 1, ds3»\t*\t«[0, 3, 1, 2], 1, ds5»\t=\t«[2, 1, 3, 0], 2, dr2»\n«[1, 3, 0, 2], 3, ds2»\t*\t«[0, 3, 1, 2], 0, ds0»\t=\t«[1, 2, 3, 0], 3, dr2»\n"""\n```\n\n```python3\n\n# Operator ~ is another way of sampling.\nG = S(12)\nprint(~G)\n"""\n[11, 3, 8, 5, 0, 7, 10, 2, 1, 4, 6, 9]\n"""\n```\n\n```python3\n\n# Manual element creation.\nlast_perm_i = factorial(12) - 1\na = Perm(i=last_perm_i, n=12)\nprint("Last element of S35:", a)\n"""\nLast element of S35: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]\n"""\n```\n\n```python3\n\n# Inverse element. Group S4.\na = Perm(i=21, n=4)\nb = Perm(i=17, n=4)\nprint(a, "*", ~a, "=", (a * ~a).i, "=", a * ~a, "= identity")\n"""\n[1, 3, 2, 0] * [3, 0, 2, 1] = 0 = [0, 1, 2, 3] = identity\n"""\n```\n\n```python3\n\nprint(a, "*", b, "=", a * b)\n"""\n[1, 3, 2, 0] * [1, 2, 3, 0] = [3, 2, 0, 1]\n"""\n```\n\n```python3\n\nprint(a, "*", b, "*", ~b, "=", a * b * ~b, "= a")\n"""\n[1, 3, 2, 0] * [1, 2, 3, 0] * [3, 0, 1, 2] = [1, 3, 2, 0] = a\n"""\n```\n\n\n</p>\n</details>\n\n**Commutativity degree of groups**\n<details>\n<p>\n\n```python3\n\nfrom garoupa.algebra.cyclic import Z\nfrom garoupa.algebra.dihedral import D\nfrom garoupa.algebra.matrix.m import M\n\n\ndef traverse(G):\n    i, count = G.order, G.order\n    for idx, a in enumerate(G.sorted()):\n        for b in list(G.sorted())[idx + 1 :]:\n            if a * b == b * a:\n                count += 2\n            i += 2\n    print(\n        f"|{G}| = ".rjust(20, " "),\n        f"{G.order}:".ljust(10, " "),\n        f"{count}/{i}:".rjust(15, " "),\n        f"  {G.bits} bits",\n        f"\\t{100 * count / i} %",\n        sep="",\n    )\n\n\n# Dihedral\ntraverse(D(8))\n"""\n             |D8| = 16:              112/256:  4.0 bits\t43.75 %\n"""\n```\n\n```python3\ntraverse(D(8) ^ 2)\n"""\n          |D8×D8| = 256:         12544/65536:  8.0 bits\t19.140625 %\n"""\n```\n\n```python3\n\n# Z4!\ntraverse(Z(4) * Z(3) * Z(2))\n"""\n       |Z4×Z3×Z2| = 24:              576/576:  4.584962500721157 bits\t100.0 %\n"""\n```\n\n```python3\n\n# M 3x3 %4\ntraverse(M(3, 4))\n\n# Large groups (sampling is needed).\nGs = [D(8) ^ 3, D(8) ^ 4, D(8) ^ 5]\nfor G in Gs:\n    i, count = 0, 0\n    for a, b in zip(G, G):\n        if a * b == b * a:\n            count += 1\n        if i >= 10_000:\n            break\n        i += 1\n    print(\n        f"|{G}| = ".rjust(20, " "),\n        f"{G.order}:".ljust(10, " "),\n        f"{count}/{i}:".rjust(15, " "),\n        f"  {G.bits} bits",\n        f"\\t~{100 * count / i} %",\n        sep="",\n    )\n"""\n           |M3%4| = 64:            2560/4096:  6.0 bits\t62.5 %\n       |D8×D8×D8| = 4096:          815/10000:  12.0 bits\t~8.15 %\n    |D8×D8×D8×D8| = 65536:         345/10000:  16.0 bits\t~3.45 %\n |D8×D8×D8×D8×D8| = 1048576:       157/10000:  20.0 bits\t~1.57 %\n"""\n```\n\n\n</p>\n</details>\n\n**Detect identity after many repetitions**\n<details>\n<p>\n\n```python3\n\nimport operator\nfrom datetime import datetime\nfrom functools import reduce\nfrom math import log, inf\nfrom sys import argv\n\nfrom garoupa.algebra.dihedral import D\nfrom garoupa.algebra.symmetric import S\n\nexample = len(argv) == 1 or (not argv[1].isdecimal() and argv[1][0] not in ["p", "s", "d"])\n\nprimes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,\n          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,\n          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,\n          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,\n          499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,\n          643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,\n          797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,\n          947, 953, 967, 971, 977, 983, 991, 997, 1009]\n\nif example:\n    limit, sample = 30, 100\n    lst = []  # See *.\n    for n in primes[:5]:\n        lst.append(D(n, seed=n))\n    G = reduce(operator.mul, lst)\nelse:\n    limit, sample = int(argv[2]), int(argv[3]) if len(argv) > 2 else 1_000_000_000_000\n    if argv[1] == "s25d":\n        G = S(25) * reduce(operator.mul, [D(n) for n in primes[:9]])\n    elif argv[1] == "s57":\n        G = S(57)\n    elif argv[1] == "p384":\n        G = reduce(operator.mul, [D(n) for n in primes[:51]])\n    elif argv[1] == "p64":\n        G = reduce(operator.mul, [D(n) for n in primes[:12]])\n    elif argv[1] == "p96":\n        G = reduce(operator.mul, [D(n) for n in primes[:16]])\n    elif argv[1] == "p128":\n        G = reduce(operator.mul, [D(n) for n in primes[:21]])\n    elif argv[1] == "p256":\n        G = reduce(operator.mul, [D(n) for n in primes[:37]])\n    elif argv[1] == "64":\n        G = reduce(operator.mul, [D(n) for n in range(5, 31, 2)])\n    elif argv[1] == "96":\n        G = reduce(operator.mul, [D(n) for n in range(5, 41, 2)])\n    elif argv[1] == "128":\n        G = reduce(operator.mul, [D(n) for n in range(5, 51, 2)])\n    else:\n        G = reduce(operator.mul, [D(n) for n in range(5, 86, 2)])\n\nprint(f"{G.bits} bits   Pc: {G.comm_degree}  order: {G.order} {G}", flush=True)\nprint("--------------------------------------------------------------", flush=True)\nfor hist in G.sampled_orders(sample=sample, limit=limit):\n    tot = sum(hist.values())\n    bad = 0  # See *.\n    for k, v in hist.items():\n        if k[0] <= limit:\n            bad += v\n    print(hist, flush=True)\n    hist = hist.copy()\n    if (inf, inf) in hist:\n        del hist[(inf, inf)]\n    hist = {int((k[0] + k[1]) / 2): v for k, v in hist.items()}\n    print(\n        f"\\nbits: {log(G.order, 2):.2f}  Pc: {G.comm_degree or -1:.2e}   a^<{limit}=0: {bad}/{tot} = {bad / tot:.2e}",\n        G,\n        G._pi_core(hist),\n        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),\n        flush=True,\n    )\n# * -> [Explicit FOR due to autogeneration of README through eval]\n"""\n21.376617194973697 bits   Pc: 0.004113533525298232  order: 2722720 D5×D7×D11×D13×D17\n--------------------------------------------------------------\n{(-1, 10): 9, (9, 20): 7, (19, 30): 9, (inf, inf): 75}\n\nbits: 21.38  Pc: 4.11e-03   a^<30=0: 25/100 = 2.50e-01 D5×D7×D11×D13×D17 0.125 07/12/2021 16:43:38\n"""\n```\n\n\n</p>\n</details>\n\n**Tendence of commutativity on Mn**\n<details>\n<p>\n\n```python3\nfrom itertools import chain\n\nfrom garoupa.algebra.matrix.m import M\nfrom garoupa.algebra.matrix.m8bit import M8bit\n\n\ndef traverse(G):\n    i, count = G.order, G.order\n    for idx, a in enumerate(G.sorted()):\n        for b in list(G.sorted())[idx + 1:]:\n            if a * b == b * a:\n                count += 2\n            i += 2\n    print(f"|{G}| = ".rjust(20, \' \'),\n          f"{G.order}:".ljust(10, \' \'),\n          f"{count}/{i}:".rjust(15, \' \'), f"  {G.bits} bits",\n          f"\\t{100 * count / i} %", sep="")\n\n\nM1_4 = map(M, range(1, 5))\nfor G in chain(M1_4, [M8bit(), M(5)]):\n    traverse(G)\n# ...\nfor G in map(M, range(6, 11)):\n    i, count = 0, 0\n    for a, b in zip(G, G):\n        if a * b == b * a:\n            count += 1\n        i += 1\n        if i >= 1_000_000:\n            break\n    print(f"|{G}| = ".rjust(20, \' \'),\n          f"{G.order}:".ljust(10, \' \'),\n          f"{count}/{i}:".rjust(15, \' \'), f"  {G.bits} bits",\n          f"\\t~{100 * count / i} %", sep="")\n\n"""\n|M1| = 1:                        1/1:  0 bits\t100.0 %\n|M2| = 2:                        4/4:  1 bits\t100.0 %\n|M3| = 8:                      40/64:  3 bits\t62.5 %\n|M4| = 64:                 1024/4096:  6 bits\t25.0 %\n|M8bit| = 256:              14848/65536:  8 bits\t22.65625 %\n|M5| = 1024:           62464/1048576:  10 bits\t5.95703125 %\n|M6| = 32768:              286/32768:  15 bits\t0.872802734375 %\n|M7| = 2097152:          683/1000000:  21 bits\t0.0683 %\n|M8| = 268435456:         30/1000000:  28 bits\t0.003 %\n|M9| = 68719476736:        1/1000000:  36 bits\t0.0001 %\n|M10| = 35184372088832:     0/1000000:  45 bits\t0.0 %\n"""\n```\n</p>\n</details>\n\n**Groups benefit from methods from the module \'hosh\'**\n<details>\n<p>\n\n```python3\nfrom garoupa.algebra.matrix import M\n\nm = ~M(23)\nprint(repr(m.hosh))\n```\n<a href="https://github.com/davips/garoupa/blob/main/examples/7KDd8TiA3S11QTkUid2wy87DQIeGQ35vB1bsP5Y6DjZ.png">\n<img src="https://raw.githubusercontent.com/davips/garoupa/main/examples/7KDd8TiA3S11QTkUid2wy87DQIeGQ35vB1bsP5Y6DjZ.png" alt="Colored base-62 representation" width="380" height="18">\n</a>\n</p>\n</details>\n\n\n\n## Performance\nComputation time for the simple operations performed by GaROUPa can be considered negligible for most applications,\nsince the order of magnitude of creating and operating identifiers is around a few μs:\n![img_6.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_6.png)\nOn the other hand, we estimate up to ~7x gains in speed when porting the core code to  _rust_.\nThe package [hosh](https://pypi.org/project/hosh) was a faster implementation of an earlier version of GaROUPa,\nIt will be updated to be fully compatible with current GaROUPa at major version `2.*.*`.\nAs the performance of garoupa seems already very high, an updated \'rust\' implementation might become unnecessary.\nSome parts of the algebra module need additional packages, they can be installed using:\n`poetry install -E full`\n\n## Grants\nThis work was partially supported by Fapesp under supervision of\nProf. André C. P. L. F. de Carvalho at CEPID-CeMEAI (Grants 2013/07375-0 – 2019/01735-0).\n',
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
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
