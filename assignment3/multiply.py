import MapReduce
import sys
from operator import itemgetter

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

a_row=5
b_col=5

def mapper(record):
    matrix = record[0]
    val = record[3]
    if matrix == "a":
        i = record[1]
        j = record[2]
        for k in range(0, b_col):
            mr.emit_intermediate((i, k), (matrix, j, val))
    else:
        j = record[1]
        k = record[2]
        for i in range(0, a_row):
            mr.emit_intermediate((i, k), (matrix, j, val))

def reducer(key, list_of_values):
    i, j = key
    As = sorted(filter(lambda x: x[0] == "a", list_of_values), key=itemgetter(1))
    Bs = sorted(filter(lambda x: x[0] == "b", list_of_values), key=itemgetter(1))
    total=0
    print "key is ", i, j
    print list_of_values
    print
    for a in As:
        for b in Bs:
            if a[1] == b[1]:
                total += a[2] * b[2]
    mr.emit((i, j, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
