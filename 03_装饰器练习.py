def add_tag_td(func):
    def put_tag():
        return "<td>" + func() + "</td>"
    return put_tag


def add_tag_h1(func):
    def put_tag():
        return "<h1>" + func() + "</h1>"
    return put_tag


@add_tag_td
@add_tag_h1
def get_str():
    return "hahaha"


print(get_str())
