import datetime
import random

def generate_snake():
    today = datetime.date.today()
    seed = today.year * 1000 + today.timetuple().tm_yday
    random.seed(seed)

    snake = ''
    for _ in range(50):
        snake += ' ' * random.randint(0, 10)
        snake += '▒' * random.randint(1, 5)
        snake += '\n'

    return snake

if __name__ == "__main__":
    print(generate_snake())
