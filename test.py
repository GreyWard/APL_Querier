import util as ut
prompt = "SELECT * FROM wine LIMIT 5;"
print(f"Original query: {prompt}")
response = ut.prepend_database_name(prompt,"Test_01")
print(f"Modified query: {response}")
