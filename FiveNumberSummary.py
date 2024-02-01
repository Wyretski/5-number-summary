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
calc([2.3, 8.6, 5.4, 3.1, 2.7, 9.3, 7.4, 8.1, 10.2, 11.3])