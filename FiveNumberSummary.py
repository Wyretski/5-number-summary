import statistics

def calculate_five_number_summary(data):
    length = len(data)
    order = sorted(data)
    minimum = min(data)
    maximum = max(data)
    range = maximum - minimum
    quartile_2 = statistics.median(data)
    mean = (sum(data) / length)
    standard_deviation = statistics.stdev(data)
    quartile_1 = "null"
    quartile_3 = "null"

#Empty incomplete looking f-strings are incomplete. I'll complete them at some point.
    print(f"Length: {data}")
    print(f"Unordered: {data}")
    print(f"Ordered: {order}")
    print(f"Min: {minimum}")
    print(f"Q1: {quartile_1}")
    print(f"Q2: {quartile_2}")
    print(f"Q3: {quartile_3}")
    print(f"Max: {maximum}")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {standard_deviation}")
    print(f"Range: {range}")

calc = calculate_five_number_summary
calc([array])
#Replace [array] with an actual array (e.g. [1, 2, 3, 4, 5])
