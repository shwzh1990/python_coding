
my_list1 = [4341,3157,3150,4704,5284,3781,3079,758,319,1598,3931,2093,338,2043,431,1514,1500,5166,2449,478,954,643,2214,3611,2371,3631,4190,147,1328,575,4556,4811,4691,761,3947,146,4936,4955,223,611,4808,2664,4808,2076,3580,2245,1086,334,2204,2988,3354,4907,3175,4962,3041,2780,3542,1317,1728,4198,848,2443,1429,3720,1504,1429,1797,4129,211,3448,3224,1500,3373,5298,4171,4041,3565,3683,1112,4557,3941,5167,4910,4291,2371,4764,4672,2201,2757,1087,3389,5095,1058,576,1817,4111,684,2071,687,2250,425,2419,507,2468]
my_list2 = [5269,1817,3265,3033,1003,2747,4622,986,4030,2790,407,4815,2363,4089,2348,4020,1287,98,2637,4716,1246,1372,3665,1281,4261,4987,1192,2439,1706,468,3935,1172,4878,1089,5275,2349,567,2437,4533,5241,4513,3652,1380,1099,4339,896,884,1221,4065,3887,1505,732,1820,748,1249,4333,4181,872,336,1162,2504,1013,1935,4614,2226,1510,436,4039,2497,942,3825,4206,4749,2131,1692,1113,4802,1991,4290,2840,2613,3730,3685,3603,339,3834,3810,779,1012,721,854,1150,2879,2839,3255,709,4428,4322,340,943,890,3071,4152,2486]

#i = 0
#result_list = []
#for i in range(0,len(my_list1)-1):
#    result = my_list1[i] - my_list2[i]
#    result_list.append(result)
result_list = [my_list1[i] - my_list2[i] for i in range(0,len(my_list1)-1)]
print(result_list)


def help_info_function():
    print("This is help info function")

def menu():
    num = input("XXXXXXXXXx")
    if num == "1":
        help_info_function()

menu()