using Test
@testset "Test set" begin
    @test 1 == 1
    @test 1 != 2
    @testset "Nested test set" begin
        @test 2 + 2 == 4
        @test 3 * 3 == 9
	@test 5*6==2
    end
end
