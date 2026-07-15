using BenchmarkTools
struct Dual{T}
    val::T #valore della funzione
    der::T #valore della derivata della funzione
end

Base.:+(f::Dual, g::Dual) = Dual(f.val + g.val, f.der + g.der)
Base.:+(f::Dual, α::Number) = Dual(f.val + α, f.der)
Base.:+(α::Number, f::Dual) = f + α #f+alpha è equivalente a f.val + alpha

Base.:-(f::Dual, g::Dual) = Dual(f.val - g.val, f.der - g.der)

Base.:*(f::Dual, g::Dual) = Dual(f.val*g.val, f.der*g.val + f.val*g.der)
Base.:*(α::Number, f::Dual) = Dual(f.val * α, f.der * α)
Base.:*(f::Dual, α::Number) = α * f
Base.:^(f::Dual, n::Integer) = Base.power_by_squaring(f, n)

Base.:/(f::Dual, g::Dual) =
            Dual(f.val/g.val, (f.der*g.val - f.val*g.der)/(g.val^2))
Base.:/(α::Number, f::Dual) = Dual(α/f.val, -α*f.der/f.val^2)
Base.:/(f::Dual, α::Number) = f * inv(α)

fd = Dual(3, 2)
gd = Dual(2, 4)

@show 5+fd
@show fd+gd
@show fd * gd
@show fd * (gd + gd)
# testing delle perfomance da 34 a 45
#add(a1, a2, b1, b2) = (a1+b1, a2+b2)
#add(j1, j2) = j1 + j2

#a, b, c, d = 1, 2, 3, 4
#ad = Dual(1, 2)
#bd = Dual(3, 4)

#@btime add($a, $b, $c, $d)
#@btime add($ad, $bd);

#@show add(a, b, c, d)
#@show add(ad, bd);

# differenziazione automatica
derivative(f, x) = f(Dual(x, one(x))).der
println(derivative(x -> 3x^4 + 2x, 2))


