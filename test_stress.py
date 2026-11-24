from hello_world import register, users

for i in range(10000):
    assert register("User" + str(i), "123456")

assert len(users) == 10000

print("Stress test passed")