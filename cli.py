import argparse
import web_server
import sys
sys.path.append("cgi-bin/")
import database_manager

class CLI:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Option Usage: cli.py --option "values" (must include quotes)')
        parser.add_argument('start', type=str, nargs='?', help='Start the web service')
        parser.add_argument('--newUser', metavar='"ORG, FIRST, LAST, PSW, PRIVILEGE"',
                            type=str, help='Create a new user')
        parser.add_argument('--rmUser', metavar='"ORG, FIRST, LAST, PRIVILEGE"',
                            type=str, help='Remove User')
        parser.add_argument('--updPSW', metavar='"ORG, FIRST, LAST, new_PSW"', type=str,
                            help='Change an existing user\'s password')
        parser.add_argument('--updPRV', metavar='"ORG, FIRST, LAST, new_PRV"', type=str,
                            help='Change an existing user\'s privilege')
        parser.add_argument('--lsUsers', metavar='ORG', type=str,
                            help='List all Users in an Organization')
        parser.add_argument('--chkdb', metavar='  DB-NAME',
                            type=str, help='Check if database exists')
        parser.add_argument('--chkcol', metavar=' Col-Name',
                            type=str, help='Check if collection exists')
        args = parser.parse_args()

        db_man = database_manager.MANAGER()
        if(args.newUser != None):
            user_string = str(args.newUser).replace(" ", "")
            organization = user_string.split(',')[0]
            first_name = user_string.split(',')[1]
            last_name = user_string.split(',')[2]
            password = user_string.split(',')[3]
            privilege = user_string.split(',')[4]
            print(db_man.addUser(organization, first_name, last_name, password, privilege))
        elif(args.rmUser != None):
            user_string = str(args.newUser).replace(" ", "")
            organization = user_string.split(',')[0]
            first_name = user_string.split(',')[1]
            last_name = user_string.split(',')[2]
            print(db_man.removeUser(organization, first_name, last_name))
        elif(args.updPSW != None):
            user_string = str(args.newUser).replace(" ", "")
            organization = user_string.split(',')[0]
            first_name = user_string.split(',')[1]
            last_name = user_string.split(',')[2]
            password = user_string.split(',')[3]
            print(db_man.updateUserPASS(organization, first_name, last_name, password))
        elif(args.updPRV != None):
            user_string = str(args.newUser).replace(" ", "")
            organization = user_string.split(',')[0]
            first_name = user_string.split(',')[1]
            last_name = user_string.split(',')[2]
            privilege = user_string.split(',')[3]
            print(db_man.updateUserPRV(organization, first_name, last_name, privilege))
        elif(args.lsUsers != None):
            organization = str(args.lsUsers).split(',')[0]
            print(db_man.findAllUsers(organization))
        elif(args.chkdb != None):
            database_name = str(args.chkdb).split(',')[0]
            print(db_man.checkDBExists(database_name))
        elif(args.chkcol != None):
            collection_name = str(args.chkcol).split(',')[0]
            print(db_man.checkCollectionExists(collection_name))
        elif(args.start != None):
            web_server.SERVER()
        else:
            print("No Option Selected.. Exiting..")


if __name__ == "__main__":
    try:
        main = CLI()
    except Exception as e:
        print("Exception: %s" % e)
        sys.exit()
