# list1 = [*range(2, 11, 2)]
# print(list1)
# --------------------------------------
# dict1 = {x: x**3 for x in range(2,11,2)}
# print(dict1)
# --------------------------------------
# nums = {"x": "10", "y":"20","z":"30", "p":"40", "q":"50", "r": "60"}
# for key,value in nums.items():
#     try:
#         value = int(value)
#     except:
#         pass
#     nums[key] = value
# print(nums)
# --------------------------------



# def pretty_print (**kwargs):
#         for a,v in kwargs.items():
#             print(f"{a}: {v}")
# pretty_print(title="The Matrix", director="Wachowski", year="1999")
# 
# 
# def pretty_print(**kwargs):
#     for a in kwargs:
#         print(f"{a}: {kwargs[a]}")
# pretty_print(title="The Matrix", director="Wachowski", year="1999")