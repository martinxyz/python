%module hello
%{
#include <numpy/arrayobject.h>
#include "hello.hpp"
%}
%include "hello.hpp"

%init %{
import_array();
%}

