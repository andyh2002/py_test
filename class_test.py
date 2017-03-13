class Test(object):
    def __init__(self, text, num):
        self.text = text
        self.num = num

# 定义相等性
    def __eq__(self, other):
        if self.num == other.num:
            return True
        else:
            return False

# 定义不等
    def __ne__(self, other):
        if self.num != other.num:
            return True
        else:
            return False


# 定义打印
    def __str__(self):
        return "Values in this object: text = {}, num = {}".format(self.text, self.num)


def main():
    a = Test(text="Hello", num=10)
    b = Test(text="World", num=5)
    print(a)
    print(b)
    print(a == b)

if __name__ == "__main__":
    main()
