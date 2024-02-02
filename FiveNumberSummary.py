import statistics

def calculate_five_number_summary(data):
    order = sorted(data)
    minimum = min(data)
    maximum = max(data)
    quartile_2 = statistics.median(data)
    mean = (sum(data) / len(data))
    standard_deviation = statistics.stdev(data)

#Empty incomplete looking f-strings are incomplete. I'll complete them at some point.
    print(f"Unordered: {data}")
    print(f"Ordered: {order}")
    print(f"Min: {min}")
    print(f"Q1: {}")
    print(f"Q2: {quartile_2}")
    print(f"Q3: {}")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {standard_deviation}")

calc = calculate_five_number_summary
calc([array])
#Replace [array] with an actual array (e.g. [1, 2, 3, 4, 5])
