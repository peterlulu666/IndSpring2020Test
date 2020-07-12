import csv


# Reference
# I googled how to work with csv data
# https://pythonprogramming.net/reading-csv-files-python-3/

# I do not really understand what is "the average over all years prior to it" and  "the average of previous years"
# So I provided two solutions


# The first solution is like
# Let's say the current year is 1952 and the average temperature of 1952 is 50.
# The average temperature in 1951 is 40. The average temperature in 1950 is 30.
# we compare 50 with 40, compare 50 with 30. Is 50 greater than 40? Is 50 greater than 30?
# If true, we can say the average temperature in year of 1952 is higher than the over all years prior to it.

def average_temperature(csv_file):
    """average_temperature

    :param csv_file:
    Does: print the average temperature fore each year
    Does: Print percentage of years that have an average temperature higher than the average over all years prior to it
    """
    average_of_year_list = []
    # The first year in csv is 1950
    # The last year is in csv 2018
    for year in range(1950, 2019):
        # I googled how to work with csv data
        # https://pythonprogramming.net/reading-csv-files-python-3/
        with open(csv_file) as csvfile:
            readCSV = csv.reader(csvfile)
            average_of_day_list = []
            # The data is like the first row second row etc in csv file
            for data in readCSV:
                # data[0][0:4] is like the year of 1950 1951 etc
                if data[0][0:4] == str(year):
                    # data[6] is the average of the day
                    # Append average temperature from the first day of the year to the last day of the year
                    average_of_day_list.append(float(data[6]))
            # Average temperature of the year
            average_annually = sum(average_of_day_list) / len(average_of_day_list)
            print("The average temperature in the year of " + str(year) + " is ")
            print(round(average_annually, 1))
            # Append average temperature of the year to list
            # We will use this list later on
            average_of_year_list.append(round(average_annually, 1))
    start_year = 1951
    higher_count = 0
    higher_list = []
    # compare the average temperature in 1950 with the average temperature in 1951 etc
    for current_year_index in range(1, len(average_of_year_list)):
        # Set is_higher to True
        is_higher = True
        for previous_year_index in range(0, current_year_index):
            # If the average temperature in the current year is not greater than one of the average temperature in
            # the previous year, We would say that the average temperature in the current year is not higher than the
            # over all years prior to it.
            if average_of_year_list[current_year_index] <= average_of_year_list[previous_year_index]:
                is_higher = False
        if is_higher == True:
            higher_count = higher_count + 1
            higher_list.append(start_year)

        # In the next iteration we will compare the average temperature between the current year and the previous years
        start_year = start_year + 1

    print("The average temperature in the year of " + str(
        higher_list) + " are " + "higher than the over all years prior to it")
    print("The percentage of years that have an average temperature higher than the average over all years prior to it")
    print(str(round(higher_count / (2018 - 1950 + 1) * 100, 2)) + "%")


# The second solution is like
# Let's say the current year is 1960 and the average temperature of 1960 is 50. We compute the average temperature from
# 1950 to 1959, let's say 40. Finally, we compare 50 with 40? Is 50 greater than 40? If true, we can say the average
# temperature in the year of 1960 is higher than the over all years prior to it.

def average_temperature_ind(csv_file):
    """average_temperature_ind

    :param csv_file:
    Does: print the average temperature fore each year
    Does: Print percentage of years that have an average temperature higher than the average over all years prior to it
    """
    average_of_year_list = []
    # The first year in csv is 1950
    # The last year is in csv 2018
    for year in range(1950, 2019):
        # I googled how to work with csv data
        # https://pythonprogramming.net/reading-csv-files-python-3/
        with open(csv_file) as csvfile:
            readCSV = csv.reader(csvfile)
            average_of_day_list = []
            # The data is like the first row second row etc in csv file
            for data in readCSV:
                # data[0][0:4] is like the year of 1950 1951 etc
                if data[0][0:4] == str(year):
                    # data[6] is the average of the day
                    # Append average temperature from the first day of the year to the last day of the year
                    average_of_day_list.append(float(data[6]))
            # Average temperature of the year
            average_annually = sum(average_of_day_list) / len(average_of_day_list)
            print("The average temperature in the year of " + str(year) + " is ")
            print(round(average_annually, 1))
            # Append average temperature of the year to list
            # We will use this list later on
            average_of_year_list.append(round(average_annually, 1))
    higher_temperature_count = 0
    for current_year_index in range(1, len(average_of_year_list)):
        current_year_temperature = average_of_year_list[current_year_index]
        previous_year_list = average_of_year_list[0:current_year_index]
        average_over_all_previous_year = sum(previous_year_list) / len(previous_year_list)
        if current_year_temperature > average_over_all_previous_year:
            higher_temperature_count = higher_temperature_count + 1
    print("The percentage of years that have an average temperature higher than the average over all years prior to it")
    print(str(round(higher_temperature_count / (2018 - 1950 + 1) * 100, 2)) + "%")


def main():
    # The percentage of years that have an average temperature higher than the average over all years prior to it
    # 10.14%
    average_temperature(
        "/Users/YanzhiWang/PycharmProjects/IndSpring2020Test/Indianapolis-Weather-Station-USW00093819-1950-2018.csv")

    # The percentage of years that have an average temperature higher than the average over all years prior to it
    # 65.22%
    average_temperature_ind(
        "/Users/YanzhiWang/PycharmProjects/IndSpring2020Test/Indianapolis-Weather-Station-USW00093819-1950-2018.csv")


main()
