class RingRenderer {
  public:
  int cx, cy;
  void render(PyObject * arr, int radius) {
    int height, width, x, y;
    uint8_t * p;

    assert(PyArray_ISCARRAY(arr));
    assert(PyArray_NDIM(arr) == 3);
    assert(PyArray_DIM(arr, 2) == 3);

    height = PyArray_DIM(arr, 0);
    width  = PyArray_DIM(arr, 1);
    p = (uint8_t*)PyArray_DATA(arr);
    
    int radius2 = radius*radius;

    for (y=0; y<height; y++) {
      for (x=0; x<width; x++) {
        int dist2 = (x-cx)*(x-cx) + (y-cy)*(y-cy);
        if (dist2 < radius2) {
          p[0] = p[0] * dist2 / radius2;
          p[1] = p[1] * dist2 / radius2;
          p[2] = p[2] * dist2 / radius2;
        }
        p += 3;
      }
    }
  }
};


// other (incomplete) examples:

class Gradient {
  public:
  float parm1, parm2;

  PyObject * get_color_at(float x, float y) {
    int r, g, b;
    // ...
    return Py_BuildValue("ddd", r, g, b);
  }
};


void render(PyObject * dst_surface) {
  PyObject * res;
  int x, y, w, h;
  // ...
  res = PyObject_CallMethod(dst_surface, "mark_dirty",
                            "(iiii)", x, y, w, h);
  Py_DECREF(res); // note: crash if callback throws exception
}

