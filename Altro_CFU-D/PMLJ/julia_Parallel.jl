using BenchmarkTools
d = Dict()
a = rand(10^7)

j_builtin = @benchmark sum($a)
d["Julia built-in"] = minimum(j_builtin.times) / 1e6

function mysum(A)
    s = 0.0
    for a in A
        s += a
    end
    return s
end
j_hand = @benchmark mysum($a)

d["Julia hand-written"] = minimum(j_hand.times) / 1e6

using Libdl
C_code = """
    #include <stddef.h>
    double c_sum(size_t n, double *X) {
        double s = 0.0;
        for (size_t i = 0; i < n; ++i) {
            s += X[i];
        }
        return s;
    }
"""

const Clib = tempname()   # make a temporary file

# compile to a shared library by piping C_code to gcc
open(`gcc -fPIC -O3 -msse3 -xc -shared -o $(Clib * "." * Libdl.dlext) -`, "w") do f
    print(f, C_code)
end

# define a Julia function that calls the C function:
c_sum(X::Array{Float64}) = ccall(("c_sum", Clib), Float64, (Csize_t, Ptr{Float64}), length(X), X)

c_bench = @benchmark c_sum($a)
d["C"] = minimum(c_bench.times) / 1e6

using PyCall
pysum = pybuiltin("sum")
pysum(a) ≈ sum(a)

py_builtin = @benchmark pysum($a)
d["Python built-in"] = minimum(py_builtin.times) / 1e6

using Conda
numpy_sum = pyimport("numpy")["sum"]
numpy_sum(a) ≈ sum(a)

py_numpy = @benchmark numpy_sum($a)
d["Python numpy"] = minimum(py_numpy.times) / 1e6

py"""
def py_sum(A):
    s = 0.0
    for a in A:
        s += a
    return s
"""

sum_py = py"py_sum"
sum_py(a) ≈ sum(a)

py_hand = @benchmark sum_py($a)
d["Python hand-written"] = minimum(py_hand.times) / 1e6


function mysum_fast(A)
    s = 0.0
    for a in A
        @fastmath s += a
    end
    s
end

j_hand_fast = @benchmark mysum_fast($a)
d["Julia hand-written fast"] =
    minimum(j_hand_fast.times) / 1e6

println(d)
