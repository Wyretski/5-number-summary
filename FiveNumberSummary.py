import statistics

def calculate_five_number_summary(data):
    length = len(data)
    order = sorted(data)
    minimum = min(data)
    maximum = max(data)
    quartile_2 = statistics.median(data)
    mean = (sum(data) / len(data))
    standard_deviation = statistics.stdev(data)
    range = maximum - minimum

    print(f"Length: {length}")
    print(f"Unordered: {data}")
    print(f"Ordered: {order}")
    print(f"Min: {minimum}")
    print(f"Q2: {quartile_2}")
    print(f"Max: {maximum}")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {standard_deviation}")
    print(f"Range: {range}")
    
    if length % 2 != 0:
        order.remove(quartile_2)
    else:
        print("")
    
    quartile_1 = statistics.median(order[:length//2])
    quartile_3 = statistics.median(order[length//2:])
    interquartile_range = quartile_3 - quartile_1
   
    print(f"Q1: {quartile_1}")
    print(f"Q3: {quartile_3}")
    print(f"IQR: {interquartile_range}")

calc = calculate_five_number_summary
calc([85, 87, 98, 82, 77, 88])
#Replace [array] with an actual array (e.g. [1, 2, 3, 4, 5])
