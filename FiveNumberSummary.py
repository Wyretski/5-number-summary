import statistics

def calculate_five_number_summary(data):

    print(data)

    order = sorted(data)
    print(order)

    minimum = min(data)
    print(f"Min: {minimum}")

    quartile_2 = statistics.median(data)
    print(f"Q2: {quartile_2}")

    maximum = max(data)
    print(f"Max: {maximum}")

    mean = (sum(data) / len(data))
    print(f"Mean: {mean}")

    standard_deviation = statistics.stdev(data)
    print(f"Standard Deviation: {standard_deviation}")

calc = calculate_five_number_summary
calc([array])
#Replace array with an actual array (e.g. [1, 2, 3, 4, 5])
