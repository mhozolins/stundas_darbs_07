from hello_world import register

assert register("Miks", "123456") is True
assert register("Miks", "123456") is False

print("Regression test passed")