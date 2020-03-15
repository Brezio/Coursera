import csv
import statistics as stat

def cluster_window(pixel_temperature, x_location, y_location, coordinate_set, filename):

    interest_matrix = []
    x_interest_matrix = []
    y_interest_matrix = []


    coord = []

    hotspot_matrix = []
    x_coordinate_list = []
    y_coordinate_list = []

    minimum = 10000
    maximum = 0
    average = 0

    minimum_hp = 10000
    average_hotspot = 0
    counter = 0

#Obtaining the Interest Matrix

    for items in coordinate_set:
        interest_matrix.append(pixel_temperature[items[1]][items[0]])
        x_interest_matrix.append(items[1])
        y_interest_matrix.append(items[0])


    for index in range(len(interest_matrix)):
        if(float(interest_matrix[index]) > 0 and float(interest_matrix[index]) < float(minimum)):
            minimum = float(interest_matrix[index])
        if(float(interest_matrix[index]) > maximum):
            maximum = float(interest_matrix[index])

        average = average + float(interest_matrix[index])

# Obtaining the Percentile Matrix

    for i in range(len(interest_matrix)):
        if (float(interest_matrix[i]) >= 0.97 * maximum):
            hotspot_matrix.append(interest_matrix[i])

    for items in coordinate_set:
        if ((float(pixel_temperature[items[1]][items[0]])) >= 0.85 * maximum):
            coord.append([items[1], items[0]])
            counter = counter + 1

    for index in range(len(hotspot_matrix)):
        if (float(hotspot_matrix[index]) < float(minimum_hp)):
            minimum_hotspot = float(hotspot_matrix[index])

        average_hotspot = average_hotspot + float(hotspot_matrix[index])

    average = average/len(interest_matrix)
    average_hotspot = average_hotspot/len(hotspot_matrix)

    percentage = (float(len(hotspot_matrix))/float(len(interest_matrix)))*100

    return hotspot_matrix, maximum, minimum, average,\
           minimum_hotspot, average_hotspot, percentage, coord

def cluster_facade(pixel_temperature, x_location, y_location, coordinate_set, filename):

    interest_matrix = []
    x_interest_matrix = []
    y_interest_matrix = []


    coord = []

    hotspot_matrix = []
    x_coordinate_list = []
    y_coordinate_list = []

    minimum = 10000
    maximum = 0
    average = 0

    minimum_hp = 10000
    average_hotspot = 0
    counter = 0

#Obtaining the Interest Matrix

    for items in coordinate_set:
        interest_matrix.append(pixel_temperature[items[1]][items[0]])
        x_interest_matrix.append(items[1])
        y_interest_matrix.append(items[0])


    for index in range(len(interest_matrix)):
        if(float(interest_matrix[index]) > 0 and float(interest_matrix[index]) < float(minimum)):
            minimum = float(interest_matrix[index])
        if(float(interest_matrix[index]) > maximum):
            maximum = float(interest_matrix[index])

        average = average + float(interest_matrix[index])

# Obtaining the Percentile Matrix

    for i in range(len(interest_matrix)):
        if (float(interest_matrix[i]) >= 0.97 * maximum):
            hotspot_matrix.append(interest_matrix[i])
    
    stddev_hp = stat.pstdev(hotspot_matrix, mu= None)
    
    print(stddev_hp)

    for items in coordinate_set:
        if ((float(pixel_temperature[items[1]][items[0]])) >= (2*stddev_hp) * maximum):
            coord.append([items[1], items[0]])
            counter = counter + 1

    for index in range(len(hotspot_matrix)):
        if (float(hotspot_matrix[index]) < float(minimum_hp)):
            minimum_hotspot = float(hotspot_matrix[index])

        average_hotspot = average_hotspot + float(hotspot_matrix[index])

    average = average/len(interest_matrix)
    average_hotspot = average_hotspot/len(hotspot_matrix)

    percentage = (float(counter)/float(len(interest_matrix)))*100

    return hotspot_matrix, maximum, minimum, average,\
           minimum_hotspot, average_hotspot, percentage, coord