from functools import reduce
def groupByKey(data):
    result = dict()
    for key, value in data:
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    return result
        
def reduceByKey(f, data):
    key_values = groupByKey(data)
    ans = list(map(lambda key: 
                   (key, reduce(f, key_values[key])), 
                       key_values))
    print(ans)


data = map(lambda x: (x, 1), "to be or not to be".split())
reduceByKey(lambda x,y:x+y,data)
