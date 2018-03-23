# # def expense(exp):
# #     total=0
# #     for item in exp:
# #         total=total+item
# #         return total
# #
# # tom_exp=[2100, 3000, 3500]
# # joe_exp=[200, 500, 700]
# #
# # tom_total=expense(tom_exp)
# # joe_total=expense(joe_exp)
# # print("tom total",tom_total)
# # print("joe total",joe_total)
#
# # def sum(a,b=7):
# #     '''
# #      document
# #     :param a:
# #     :param b:
# #     :return:
# #     '''
# #     sum_total=a+b
# #     return sum_total
# # n=sum(b=5,a=6)
# # print(n)
# # try:
# #     print(sum_total)
# # except NameError:
# #     print("name error")
# # print(sum.__doc__)
# def calculate_area(base, height, shapes='triangle'):
#     area=0
#     if shapes== 'rectangle':
#         area= base*height
#         return area
#     elif shapes=='triangle':
#         area=1/2*base*height
#         return area
#     else:
#         return
#
# areasum=calculate_area(5,2,'zum')
# print(areasum)

for i in range(1,6):
    s=''
    for j in range(i):
        s+='*'
    print(s)