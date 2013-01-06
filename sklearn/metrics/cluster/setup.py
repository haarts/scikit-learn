import os
from os.path import join

import numpy
from numpy.distutils.misc_util import Configuration


def configuration(parent_package="", top_path=None):
    config = Configuration("metrics/cluster", parent_package, top_path)
    libraries = []
    if os.name == 'posix':
        libraries.append('m')
    config.add_extension("expected_mutual_info_fast",
                         sources=["expected_mutual_info_fast.c"],
                         include_dirs=[join('..', '..', 'src', 'fdlibm'),
                                       numpy.get_include()],
                         libraries=libraries + ['fdlibm'])

    config.add_subpackage("tests")

    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(**configuration().todict())
