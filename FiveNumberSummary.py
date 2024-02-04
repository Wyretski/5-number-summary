import statistics

def calculate_five_number_summary(data):
    length = len(data)
    order = sorted(data)
    minimum = min(data)
    maximum = max(data)
    quartile_2 = statistics.median(data)
    mean = (sum(data) / len(data))
    standard_deviation = statistics.stdev(data)

    print(f"Length: {length}")
    print(f"Unordered: {data}")
    print(f"Ordered: {order}")
    print(f"Min: {minimum}")
    print(f"Q2: {quartile_2}")
    print(f"Max: {maximum}")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {standard_deviation}")
    
    if length % 2 != 0:
        order.remove(quartile_2)
    
    quartile_1 = statistics.median(order[:length//2])
    quartile_3 = statistics.median(order[length//2:])
   
    print(f"Q1: {quartile_1}")
    print(f"Q3: {quartile_3}")

calc = calculate_five_number_summary
calc([array])
#Replace [array] with an actual array (e.g. [1, 2, 3, 4, 5])
