import MapReduce
import sys
import itertools


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    table = record[0]
    order_id = record[1]
    attributes = record
    mr.emit_intermediate(order_id, attributes)

def reducer(key, list_of_values):
    order_tuples = filter(lambda x: x[0] == "order", list_of_values)
    line_tuples = filter(lambda x: x[0] == "line_item", list_of_values)
    for i,j in itertools.product(order_tuples, line_tuples):
        mr.emit(i+j)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
