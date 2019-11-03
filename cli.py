import argparse
import database_manager
import sys


class CLI:
    def __init__(self):
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Options:')
    parser.add_argument('--newUser', metavar='ORG, FIRST, LAST, PRIVILEGE',
                        type=str, help='Create a new user')
    parser.add_argument('--rmUser', metavar='ORG, FIRST, LAST, PRIVILEGE',
                        type=str, help='Remove User')
    parser.add_argument('--updUser', metavar='ORG, FIRST, LAST, PRIVILEGE', type=str,
                        help='Change an existing user')
    parser.add_argument('--lsUsers', metavar='ORG', type=str,
                        help='List all Users in an Organization')
    parser.add_argument('--chkdb', metavar='  DB-NAME',
                        type=str, help='Check if database exists')
    parser.add_argument('--chkcol', metavar=' Col-Name',
                        type=str, help='Check if coself.authdb["Users"].find({"organization": organization})llection exists')
    args = parser.parse_args()
    print(args)

    db_man = database_manager.MANAGER()
    if(not args.newUser is None):
        user_string = str(args.newUser).replace(" ", "")
        organization = user_string.split(',')[0]
        first_name = user_string.split(',')[1]
        last_name = user_string.split(',')[2]
        privilege = user_string.split(',')[3]
        print(db_man.addUser(organization, first_name, last_name, privilege))
    elif(not args.rmUser is None):
        user_string = str(args.newUser).replace(" ", "")
        organization = user_string.split(',')[0]
        first_name = user_string.split(',')[1]
        last_name = user_string.split(',')[2]
        privilege = user_string.split(',')[3]
        print(db_man.removeUser(organization, first_name, last_name, privilege))
    elif(not args.updUser is None):
        user_string = str(args.newUser).replace(" ", "")
        organization = user_string.split(',')[0]
        first_name = user_string.split(',')[1]
        last_name = user_string.split(',')[2]
        privilege = user_string.split(',')[3]
        print(db_man.updateUser(organization, first_name, last_name, privilege))
    elif(not args.lsUsers is None):
        organization = str(args.lsUsers).split(',')[0]
        print(db_man.findAllUsers(organization))
    elif(not args.chkdb is None):
        database_name = str(args.chkdb).split(',')[0]
        print(db_man.checkDBExists(database_name))
    elif(not args.chkcol is None):
        collection_name = str(args.chkcol).split(',')[0]
        print(db_man.checkCollectionExists(collection_name))
    else:
        print("No Option Selected.. Exiting..")
        sys.exit()
