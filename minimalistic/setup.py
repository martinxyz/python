from distutils.core import setup, Extension

setup(ext_modules = [Extension("_hello", ["hello.i"])])
