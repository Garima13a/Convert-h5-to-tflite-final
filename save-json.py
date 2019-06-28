# import json
#
# f = open("C:\\data\\book.txt", "w+")
# phone_book = {}
# command = ""
# while command != 'exit':
#     command = input('Enter a command(options: new,get,save): ')
#     if command == "new":
#         name = input('Enter name of the person')
#         p = input('Phone number: ')
#         a = input('Address: ')
#         phone_book[name] = {'phone': p, 'address': a}
#     elif command == 'get':
#         name = input('Enter name of the person')
#         if name in phone_book:
#             print(phone_book[name])
#         else:
#             print('person not found in address book')
#     elif command == 'save':
#         f.write(json.dumps(phone_book))

import json


def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp, indent=2)


data = {}
command = ""
while command != 'exit':
    command = input('Enter a command(options: new,save): ')
    if command == "new":
        Filter = input('Enter number of filters')
        Kernel = input('Kernel_size: ')
        Padd = input('Padding: ')
        data = {'Filter size': Filter, 'Kernel': Kernel, 'Padding': Padd}
    # elif command == 'get':
    #     name = input('Enter name of the person')
    #     if name in data:
    #         print(data[name])
    #     else:
    #         print('person not found in address book')
    elif command == 'save':
        writeToJSONFile('./', 'file-name', data)
        # fp.write(json.dumps(data))

#
#
# # Example
# data ={
#   "layers": [
#     {
#       "filters": 32,
#       "kernel_size": 3,
#       "strides": 2,
#       "padding": "valid"
#     },
#     {
#       "filters": 16,
#       "kernel_size": 3,
#       "strides": 1,
#       "padding": "same"
#     }
#   ]
# }
#
#
# #data['key'] = 'value'
#
# writeToJSONFile('./','file-name',data)
# print(type(data))
# # './' represents the current directory so the directory sav0e-file.py is in
# # 'test' is my file name
#
# #data1 = json.loads(data)
#
# for new in data['layers']:
#     print(new['filters'])
