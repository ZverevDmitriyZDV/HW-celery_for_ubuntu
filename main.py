import time
from func_for import func_toy


def main():
    async1 = func_toy.delay(1, 2)
    var1 = async1.get()
    print(var1)
    return var1


start = time.time()
main()
print(time.time() - start)
