from hello_world import register

assert register("ab", "123456") is False
assert register("Miks", "123") is False
assert register("Miks", "123456") is True

print("Unit test passed")