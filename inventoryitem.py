# noinspection PyBroadException
class InventoryItem(object):
    def __init__(self, title, description, price, store_id):
        self.title = title
        self.description = description
        self.price = price
        self.store_id = store_id

    def __str__(self):
        return self.title

    def __eq__(self, other):
        if self.store_id == other.store_id:
            return True
        else:
            return False

    def change_description(self, description=''):
        if not description:
            description = input("Please give me a description: ")
        self.description = description

    def change_price(self, price=-1):
        while price < 0:
            price = float(input("Please give me the new price [X.XX]: "))
            try:
                price = float(price)
                break
            except:
                print("I'm sorry, but {} isn't valid".format(price))
        self.price = price


class Book(InventoryItem):
    def __init__(self, title, description, price, author, store_id):
        super(Book, self).__init__(title=title, description=description, price=price, store_id=store_id)
        self.format = format
        self.author = author

    def __str__(self):
        book_line = "{title} by {author}".format(title=self.title, author=self.author)
        return book_line


def main():
    hamlet = Book(title="Hamlet",description="A Dane has a bad time.", price=5.99,
                  store_id="29382918", author="William Shakespeare")
    print(hamlet)

if __name__ == "__main__":
    main()

