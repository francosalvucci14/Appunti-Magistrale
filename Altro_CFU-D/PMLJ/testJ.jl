f1(x)=x+1
function f2(x)
	eval(:(f1(x)=x))
	f1(x)
end
println(f1(1))
println(f2(1))
