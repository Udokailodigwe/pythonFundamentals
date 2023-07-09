#get user country, capital data and store in dictionary, using three input function

country_capital_dict = {}
country_capital_input = input("Enter country name and its capital, separated by a coma: ")
country_capital_list = country_capital_input.split(",")
# print(country_capital_input)
# print(country_capital_list)
country_capital_dict[country_capital_list[0]] = country_capital_list[1]

country_capital_input = input("Enter country name and its capital, separated by a coma: ")
country_capital_list = country_capital_input.split(",")
# print(country_capital_input)
# print(country_capital_list)
country_capital_dict[country_capital_list[0]] = country_capital_list[1]

country_capital_input = input("Enter country name and its capital, separated by a coma: ")
country_capital_list = country_capital_input.split(",")
# print(country_capital_input)
# print(country_capital_list)
country_capital_dict[country_capital_list[0]] = country_capital_list[1]

print(country_capital_dict)