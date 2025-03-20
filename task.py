# a = ["q", "w", "e"]
# b = [1, 2, 3]


# def merge_lists_to_dict(t="ключ", y="значение"):
#     z = zip(t, y)
#     z = list(z)
#     z = dict(z)
#     return z


# print(merge_lists_to_dict(a, b))
# print(merge_lists_to_dict(a))


def update_car_info(**car):
    car["is_available"] = True
    return car


print(update_car_info(brand="q", price=10))
