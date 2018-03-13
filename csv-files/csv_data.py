import csv
# import shutil
# import io
# import sys
# import json
# from tempfile import NamedTemporaryFile


def get_length(filepath):
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile)
        reade_list = list(reader)
    return len(reade_list)

def read_data(filepath, id = None, email = None):
    # open file in read mode
    # unknown_id = None
    # unknown_email = None
    found_id = False
    found_email = False
    with open(filepath, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if id is not None:
                if int(row['id']) == int(id):
                    print(row)
                    found_id = True
                # else:
                #     unknown_id = id
            if email is not None:
                if str(row['email']) == str(email):
                    print(row)
                    found_email =True
                # else:
                #     unknown_email = email
            if id is None and email is None:
                print(row)

        if id and not found_id:
            print('User id {0} not found'.format(id))
        if email and not found_email:
            print('Email {0} not found'.format(email))
def write_data(filepath, name, email):
    # get total numbers of row for creatind id
    id = get_length(filepath)

    # open file in write mode
    with open(filepath, 'w+') as csvfile:
        fieldnames = ['id', 'name', 'email']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        if id == 0:
            writer.writeheader()
            id += 1
            print(id)
        writer.writerow({
            'id':id,
            'name':name,
            'email':email
        })
def append_data(filepath, name, email):

    # get total numbers of row for creatind id
    id = get_length(filepath)

    # open file in append mode
    with open(filepath, 'a') as csvfile:
        fieldnames = ['id', 'name', 'email']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        if id == 0:
            writer.writeheader()
            id += 1
        writer.writerow({
            'id':id,
            'name':name,
            'email':email
        })
# append_data('test.csv', 'rahul', 'r@gmail.com')
# read_data('test.csv')
# read_data('test.csv', id = 6, email = "r@gmail.com")
# read_data('test.csv', email="123")
# read_data('test.csv', id = 15)




# def dict_to_binary(the_dict):
#     str = json.dumps(the_dict)
#     binary = ' '.join(format(ord(letter), 'b') for letter in str)
#     return binary
# temp_file = NamedTemporaryFile(delete = False)
# # # print(sys.version_info)
# # if sys.version_info.major  >= (3.0):
# #     temp_file =  io.StringIO()
# # else:
# #     temp_file =  io.BytesIO()
# with open('test.csv', 'r+') as csvfile, temp_file:
#     fieldnames = ['id', 'name', 'email']
#     reader = csv.DictReader(csvfile)
#
#     # first write data into temperory file
#     writer = csv.DictWriter(temp_file, fieldnames = fieldnames)
#     # .encode('utf-8')
#     # writer = io.StringIO()
#     for row in reader:
#         data = {
#             # 'id':row.get('id'),
#             # 'name':row.get('name'),
#             # 'email':row.get('email')
#         }
#         writer.writerow(data)
