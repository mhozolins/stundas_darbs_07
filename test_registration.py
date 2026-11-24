from hello_world import register

assert register("User1", "password123") is True
assert register("User2", "password456") is True

print("Registration test passed")