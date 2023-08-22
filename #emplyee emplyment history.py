#emplyee emplyment history
print("employee emplyment history and information chart: ")
string0 = input("press enter to continue")
#emplyee names section
emplyee_history_chart_names = ["Dave","Sara","Adam","Roma","Andrew","Jhon","Eric"]
print(emplyee_history_chart_names[0])
#please note:In order to view defferent values, you must run the code again and change the number input in the parentheses
print("history with the company: ")
string1 = input("press enter to continue: ")
print(string1)
#emplyee information section
emplyee_history_chart_names_info = {
    1010: "Dave:\nDave started at the company about two years ago as data analyist\nHe also has shown his skills via using terraform",
    2020: "Sara:\nSara started about 4 years ago and works in Database",
    3030: "Adam:\nAdam start just two months ago as a solutions architect",
    4040: "Roma:\nRoma started just two weeks ago as a solutions architect professional\nHe knows Docker containers very well",
    5050: "Eric:\nEric has been working for the company for 10 years as a network advanced specualist"
}
#emplyee project section
print(emplyee_history_chart_names_info.get(1010))
string2 = input("press enter to continue: ")
print(string2)
past_emplyee_projects_within_the_company = {}
past_emplyee_projects_within_the_company["project"] = "s3 bucket multi cross AZ repplecation"
past_emplyee_projects_within_the_company["peoject discription"] = "setiing up bucket policies for cross AZ replcation so in case of a AZ going out\ncompany data is not compremized"
past_emplyee_projects_within_the_company["poeple who worked on the project"] = "Dave","Sara","Adam"
print(past_emplyee_projects_within_the_company)
string3 = input("press enter to continue: ")
print(string3)
#emplyee certs information section
emplyee_certs_information = {
    1-1010: "Dave\nAWS cloud practitioner\nSulutions architect\nDev ops Engineer\nData Analyst",
    2-2020: "Sara\nAWS cloud practitioner\nSulutions architect\nSulutions architect Professional\nDatabase",
    3-3030: "Adam\nAWS cloud practitioner\nSulutions architect",
    4-4040: "Roma\nAWS cloud practitioner\nSulutions architect\nSulutions architect Professional",
    5-5050: "Eric\nAWS cloud practitioner\nSulutions architect\nSulutions architect Professional\nAdvanced networking specialty"
}
print(emplyee_certs_information.get(1-1010))







