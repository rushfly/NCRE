from cntest.celery import app


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def xsum(numbers):
    return sum(numbers)


@app.task
def writefile():
    f = open('/home/weetao/cntest/celerytest/test.txt', 'wt')
    f.write('abcd')
    f.close()
    return None
