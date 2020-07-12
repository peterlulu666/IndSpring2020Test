import csv


# Reference
# I googled how to sort dictionary by value
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value


# This solution is like
# Append tuple (total number, country) to countries_list
# Sort the countries_list
# Print the top 10 countries
# There are multiple china, let's say tuple (1000, china) and tuple (100, china), (1000, china) will be printed,
# but (100, china) will not be printed
def covid(csv_file):
    """covid

    :param csv_file:
    Does: Print the top 10 total number and country on the date
    """
    header_list = []
    # The first row contains date
    # Store the first row in the header_list
    with open(csv_file) as csvfile:
        readCSV = csv.reader(csvfile)
        for data in readCSV:
            header_list = data
            break
    header_index = 0
    for date_index in range(len(header_list) - 1, 3, -1):
        print("Date " + str(header_list[len(header_list) - 1 - header_index]))
        header_index = header_index + 1
        with open(csv_file) as csvfile:
            readCSV = csv.reader(csvfile)
            next(readCSV, None)
            countries_list = []
            countries_dict = dict()
            for data in readCSV:
                if data[date_index] != '':
                    countries_list.append((int(data[date_index]), data[1]))
        countries_list.sort(reverse=True)
        for i in range(0, 10):
            print("Country of " + str(countries_list[i][1]),
                  "has total of " + str(countries_list[i][0]))
        #     if str(header_list[len(header_list) - 1 - header_index]) != "3/23/20":
        #         print(number_difference(
        #             "/Users/YanzhiWang/PycharmProjects/IndSpring2020Test/time_series_19-covid-Deaths.csv",
        #             str(header_list[len(header_list) - 1 - header_index - 1]),
        #             str(header_list[len(header_list) - 1 - header_index]), countries_list[i][1]))
        #
        # print("\n")


def number_difference(csv_file, prev_date, current_date, country):
    with open(csv_file) as csvfile:
        readCSV = csv.reader(csvfile)
        header_list = []
        with open(csv_file) as csvfile:
            readCSV = csv.reader(csvfile)
            for data in readCSV:
                header_list = data
                break

        current_number = 0
        with open(csv_file) as csvfile:
            readCSV = csv.reader(csvfile)
            for data in readCSV:
                if data[1] == country:
                    current_number = data[header_list.index(current_date)]
                    break
        prev_number = 0
        with open(csv_file) as csvfile:
            readCSV = csv.reader(csvfile)
            for data in readCSV:
                if data[1] == country:
                    prev_number = data[header_list.index(prev_date)]
                    break

        return int(current_number) - int(prev_number)


# This solution is like
# Create a dictionary countries_dict
# We would use country as the key and use total number as the value
# If the country is not in the dictionary, create the country as the key and initiate the value
# If the country is in the dictionary, add more value
# Sort the dictionary by value
# Print the top 10 countries
def covid_dict(csv_file):
    """covid_dict

    :param csv_file:
    Does: Print the top 10 total number and country on the date
    """
    header_list = []
    # The first row contains date
    # Store the first row in the header_list
    with open(csv_file) as csvfile:
        readCSV = csv.reader(csvfile)
        for data in readCSV:
            header_list = data
            break
    header_index = 0
    for date in range(len(header_list) - 1, 3, -1):
        print(header_list[len(header_list) - 1 - header_index])
        header_index = header_index + 1
        with open(csv_file) as csvfile:
            readCSV = csv.reader(csvfile)
            next(readCSV, None)
            countries_list = []
            countries_dict = dict()
            for data in readCSV:
                if data[date] != '':
                    if data[1] not in countries_dict:
                        countries_dict[data[1]] = int(data[date])
                    else:
                        countries_dict[data[1]] = countries_dict[data[1]] + int(data[date])
        print("countries_dict", countries_dict)
        # I googled how to sort dictionary by value
        # python dictionary sort value
        # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        countries_dict_sort = {key: value for key, value in
                               sorted(countries_dict.items(), reverse=True, key=lambda item: item[1])}
        print("countries_dict_sort", countries_dict_sort)
        for key in list(countries_dict_sort)[0:10]:
            print("Country of " + str(key) + " has total number of " + str(countries_dict_sort[key]))

        print("\n")


def main():
    covid("/Users/YanzhiWang/PycharmProjects/IndSpring2020Test/time_series_19-covid-Deaths.csv")
    covid_dict("/Users/YanzhiWang/PycharmProjects/IndSpring2020Test/time_series_19-covid-Deaths.csv")


main()
