
import os

import sys
from setuptools import setup, Extension, find_packages
print(find_packages(where='src'))
setup(
	name = "muldemo",
	version = "1.0",
	include_package_data=True,
	packages=find_packages(where='src'),
	package_dir={'': 'src'},
	ext_modules = [Extension("demo.cext.cadd", ["src/demo/cext/bind.c", "src/demo/cext/libmypy.c"])],

	)


