#ifdef SWIG
%module hello
%{
#include "hello.i"
%}
#endif

double distance(double dx, double dy) {
    return hypot(dx, dy);
}
