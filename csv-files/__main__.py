from argparse import ArgumentParser

from csv_data import read_data


parser = ArgumentParser(prog = 'csv-files')
parser.add_argument('type', type=str, choices = ['view', 'message'])
parser.add_argument('-id','--user_id', type = int)
parser.add_argument('-e', '--email', type = str)

args = parser.parse_args()
print(args)

if args.type == 'view':
    read_data(id = args.user_id, email = args.email)
elif args.type == 'message':
    print("message sent")
else:
    pass
