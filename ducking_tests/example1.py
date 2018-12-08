from duckling import DucklingWrapper

d = DucklingWrapper()


def parse_date():
    print(d.parse("Show me revenue of yesterday night"))
    print(d.parse_email(" You can reach me at parvezpathan09@gmail.com , dont hesitate to ask any thing"))


if __name__ == '__main__':
    parse_date()
    parse_date()
    parse_date()

