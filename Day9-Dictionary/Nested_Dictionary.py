#Nested Dictionary can be with List/Dictionary
#{Key: [List]- to store mmultiple values
# Key: {Dictionary}}- stores as akey value pair 

DICT = {"France": ["Paris", "Lyon", "Marseille"]}
print(DICT["France"][1])

Travel_log = {"Germany": {"countries_visited" : ["Berlin","Hamburg","Stuttgart"], "number_of_times_visited":8},
                                                                                            "France": {"number_of_times_visited": 12, "countries_visited": ["Paris", "Lyon", "Marseille"]}}


print(Travel_log["Germany"]["countries_visited"][2])