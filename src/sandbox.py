class MyClass:
    def __init__(self):
        print("インスタンスできたよ")

    def ore(self, anata):
        print(f"{anata}, ore")


if __name__ == "__main__":
    instance_1 = MyClass
    type(instance_1)

    instance_2 = MyClass()
    type(instance_2)

    instance_2.ore(5)
    instance_1.ore(5)
