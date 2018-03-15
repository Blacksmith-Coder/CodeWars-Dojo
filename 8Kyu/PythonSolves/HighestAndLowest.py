def high_and_low(numbers):
    nums = list(map(int, numbers.split(' ')))
    for item in nums:
        print(item)
    mmax = max(nums)
    print("maximum = {}".format(mmax))
    mmin = min(nums)
    print("minimum = {}".format(mmin))
    return "{0} {1}".format(mmax, mmin)
