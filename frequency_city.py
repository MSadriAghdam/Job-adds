#frequency function for cities (could be used for all of the columns)
def freq_function(col):
    city = []
    for item in col:
        for j in item:
            city.append(j)
            freq= {x:city.count(x) for x in city}
            sorted_freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
    return sorted_freq