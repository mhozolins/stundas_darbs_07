from hello_world import register, users

assert register("Miks", "123456") is True
assert "Miks" in users

print("Integration test passed")