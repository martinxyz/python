%module hello
%{
#include <numpy/arrayobject.h>
#include "hello.hpp"
%}
%include "hello.hpp"

// needed if this module is imported before numpy
%init %{
import_array();
%}

