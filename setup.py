from os import path

from pbr import packaging
import setuptools


# In python < 2.7.4, a lazy loading of package `pbr` will break
# setuptools if some other modules registered functions in `atexit`.
# solution from: http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass

version = packaging.get_version('pytidbrep')
BASE_DIR = path.dirname(path.abspath(__file__))

with open(path.join(BASE_DIR, 'pytidbrep', 'version.py'), 'w') as f:
    f.write('VERSION="%s"\n' % version)

setuptools.setup(
    setup_requires=['pbr>=1.8'],
    pbr=True)