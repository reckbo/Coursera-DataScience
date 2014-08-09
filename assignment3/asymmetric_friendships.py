import MapReduce
import sys
from collections import Counter

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, friend)
    mr.emit_intermediate(friend, person)

def reducer(key, list_of_values):
    asym_list = filter(lambda x: list_of_values.count(x) < 2, list_of_values)
    #print key, list_of_values
    #print key, asym_list
    for i in asym_list:
        mr.emit((key, i))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
