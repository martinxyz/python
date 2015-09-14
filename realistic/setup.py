from distutils.core import setup, Extension
from glob import glob
from subprocess import check_output

setup(ext_modules = [
        Extension("_hello",
                  sources = ["hello.i"],
                  depends = glob("*.hpp") + ["setup.py"],
                  swig_opts = ["-c++"],
                  undef_macros = ["NDEBUG"], # make assert() work

                  # if we use some library:
                  #extra_link_args = ['-lpng'],
                  # or
                  # extra_compile_args = check_output('pkg-config libpng --cflags', shell=True, universal_newlines=True).split(),
                  # extra_link_args = check_output('pkg-config libpng --libs', shell=True, universal_newlines=True).split(),
                  )
        ])
