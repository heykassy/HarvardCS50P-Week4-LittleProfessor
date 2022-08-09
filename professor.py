from random import randint

def main():
    level = get_level()

    count_errors = 0
    score = 10
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        while True:
            answer = int(input(f"{x} + {y} = "))
            if answer != x + y:
                print("EEE")
                count_errors += 1
                if count_errors > 2:
                    print(f"{x} + {y} = {x + y}")
                    score -= 1
                    break
            else:
                break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 3 and level >= 1:
                return level
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return randint(0, 9)
        case 2:
            return randint(10, 99)
        case 3:
            return randint(100, 999)


if __name__ == "__main__":
    main()