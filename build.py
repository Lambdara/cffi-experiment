from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
    float pi(int n);
""")

ffibuilder.set_source("_pi_approx",
"""
    #include "lib/pi_approx.h"
""",
                      sources=["lib/pi_approx.c"],
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
