import json
with open('D:\\code\\PycharmProjects\\Project3\\address.txt','w+') as f:
    phonebook={}
    cmd=""
    while cmd != 'exit':
        cmd=input("enter cmd(new,save,get,exit)")
        if cmd=='new':
            name=input('enter name of person ')
            p=input('enter phone number ')
            a=input('address ')
            phonebook[name]={'phone':p,'address':a}
        elif cmd=='get':
            name=input('enter name of person ')
            if name in phonebook:
                print(phonebook[name])
            else:
                print('not in phonebook\n')
        elif cmd=='save':
            f.write(json.dumps(phonebook))