import itertools
readings_temp = []
def generate_all_n_digit(num):
    all_n_digit = []
    for p in itertools.permutations(range(1,10),num):
        if p[0] != 0:
            all_n_digit.append(''.join(map(str, p)))
    return all_n_digit

def odo_list (all_n_digit) :
    odo_list_final = []
    for num in all_n_digit :
        if num == "".join(sorted(num)) :
            odo_list_final.append(num)
    return odo_list_final


def initialise (readings) :
    return readings[0]

def next_reading (input_reading) :
    return n_next_reading(input_reading ,1)

def previous_reading(input_reading) :
    return n_previous_reading(input_reading ,1)

def n_next_reading (input_reading ,n) :
    n_next_list = []
    index_of_input = readings.index(input_reading)
    for i in range(1, n+1) :
        if (index_of_input - i  < len(readings)) :
            n_next_list.append(readings[index_of_input + i])
        else :
            break
    return n_next_list

def n_previous_reading (input_reading ,n) :
    n_next_list = []
    index_of_input = readings.index(input_reading)
    for i in range(1, n+1) :
        if (index_of_input - i > 0) :
            n_next_list.append(readings[index_of_input - i])
        else :
            break
    return n_next_list

def dis_between_readings (reading1 , reading2) :
    index1=readings.index(reading1)
    index2= readings.index(reading2)
    return abs (index1 - index2)

n = 3
all_n_digit = generate_all_n_digit(n)
readings = odo_list(all_n_digit)
print(initialise(readings))
print(n_previous_reading(input("reading:"),int(input("n_previous:"))))
print(n_next_reading(input("reading:"),int(input("n_next:"))))
print(dis_between_readings(input("reading1") ,input("reading2")))
