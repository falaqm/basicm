# # exp=[2340,2500,2100,3100,2980]
# # count=0
# # for i in range(len(exp)):
# #     print('Month',i+1,'exp',exp[i])
# #     count=count+exp[i]
# # print(count)
# # key='chair'
# # location=['garage','living room','closet','chair','bathroom']
# # for i in location:
# #     if i==key:
# #         print('key is found at', i)
# #         continue
# #     else:
# #         print('key not found in',i)
# # else:
# #     print('done')
# #
# # for i in range(1,10):
# #     if i%2 == 0:
# #         continue
# #     print(i)
# #
# # result=['heads','tails','tails','heads','tails','heads','heads','tails','tails','tails']
# # count=0
# # for i in result:
# #     if i == 'heads':
# #         count=count+1
# #         continue
# # print('total no of heads:',count)
# expl = [2340, 2500, 2100, 3100, 2980]
# monthl = ['jan', 'feb', 'march', 'april', 'may']
# ml = -1
# e = input("expense amount")
# e=int(e)
# for i in range(len(expl)):
#     if e == expl[i]:
#         ml = i
#         break
# if ml != -1:
#     print('you spent %d in %s month' % (e, monthl[ml]))
# else:
#     print("no money spent")
print('ho')
z=3
for i in range(1,6):
    s=''
    for j in range(i):
        s+='*'
    print(s)
