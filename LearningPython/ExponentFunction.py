"""
Takes a certain number and raise it by a certain power
The below works like 2 to the power of 3 which is 8
"""
# print(2**3)


def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result *= base_num  # works the same way as result = result * base_num

    return result


# Works the same way but is much shorter
def raise_to_power2(base, power):
    return int(base) ** int(power)


print(raise_to_power(2, 3))
print(raise_to_power2(2, 3))
