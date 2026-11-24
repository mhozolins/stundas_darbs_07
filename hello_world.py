users = []


def register(username, password):
    if len(username) < 3:
        return False

    if len(password) < 6:
        return False

    if username in users:
        return False

    users.append(username)
    return True


if __name__ == "__main__":
    print("Registration system is running")
