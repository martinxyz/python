# slightly advanced example:
# - swig .i file separated from source
# - using an external library (libpng)

from distutils.core import setup, Extension
from glob import glob
from commands import getoutput

setup(ext_modules = [
        Extension("_hello",
                  sources = ["hello.i"],
                  depends = glob("*.hpp") + ["setup.py"],
                  swig_opts = ["-c++"],
                  undef_macros = ["NDEBUG"], # make assert() work

                  # if we use some library:
                  # extra_compile_args = getoutput('pkg-config libpng --cflags').split(),
                  # extra_link_args = getoutput('pkg-config libpng --libs').split(),
                  )
        ])
