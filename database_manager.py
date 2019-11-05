import pymongo
import password


class MANAGER:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.authdb = self.client["AuthDB"]
        self.pass_hash = password.CYPHER()

    def addUser(self, organization, first_name, last_name, password, privilege):
        organization = str(organization).lower()
        first_name = str(first_name).lower()
        last_name = str(last_name).lower()
        privilege = str(privilege).lower()

        print("Trying to add User %s, %s, %s" %
              (organization, first_name, last_name))
        user = self.authdb["Users"].find_one(
            {"organization": organization, "first name": first_name, "last name": last_name})

        if(user is None):
            password = self.pass_hash.hash_password(password)
            mydict = {"organization": organization, "first name": first_name,
                      "last name": last_name, "privilege": privilege, "password": password}
            self.authdb["Users"].insert_one(mydict)
            return ("Successfully added")
        else:
            db_find_organization = str(user["organization"]).lower()
            db_find_firstname = str(user["first name"]).lower()
            db_find_lastname = str(user["last name"]).lower()
            if(db_find_organization == organization and db_find_firstname == first_name and db_find_lastname == last_name):
                return ("User %s, %s, %s already exists" % (organization, first_name, last_name))
            else:
                return ("Strange error occured on addUser")

    def authUser(self, organization, first_name, last_name, password):
        organization = str(organization).lower()
        first_name = str(first_name).lower()
        last_name = str(last_name).lower()

        user = self.authdb["Users"].find_one(
            {"organization": organization, "first name": first_name, "last name": last_name})
        if(user == None):
            return None
        else:
            return self.pass_hash.verify_password(str(user["password"]), str(password))

    def findUser(self, organization, first_name, last_name):
        organization = str(organization).lower()
        first_name = str(first_name).lower()
        last_name = str(last_name).lower()

        return (self.authdb["Users"].find_one({"organization": organization, "first name": first_name, "last name": last_name}))

    def findAllUsers(self, organization):
        organization = str(organization).lower()
        users = []
        for user in self.authdb["Users"].find({"organization": organization}):
            users.append(user)
        return users

    def findNsort(self, organization, sort_by):
        organization = str(organization).lower()
        return self.authdb["Users"].find({"organization": organization}).sort(sort_by)

    def removeUser(self, organization, first_name, last_name):
        organization = str(organization).lower()
        first_name = str(first_name).lower()
        last_name = str(last_name).lower()

        self.authdb["Users"].delete_one(
            {"organization": organization, "first name": first_name, "last name": last_name})
        user = self.findOne(self.authdb["Users"], {
                            "organization": organization, "first name": first_name, "last name": last_name})
        if(user is None):
            return ("User %s, %s, %s was successfully deleted" % (organization, first_name, last_name))
        else:
            return ("Error occured, User was not removed")

    def removeUsers(self, organization):
        organization = str(organization).lower()

        users = self.authdb["Users"].delete_many(organization)
        return (users.deleted_count, " documents deleted.")

    def removeAllUsers(self):
        users = self.authdb["Users"].delete_many({})
        return (users.deleted_count, " documents deleted.")

    def updateUserPASS(self, organization, first_name, last_name, new_password):
        organization = str(organization).lower()
        first_name = str(first_name).lower()
        last_name = str(last_name).lower()
        new_password = self.pass_hash.hash_password(new_password)

        user = self.findUser(organization, first_name, last_name)
        old_password = str(user["password"])
        query = {"organization": organization,
                 "first name": first_name, "last name": last_name}
        self.authdb["Users"].update_one(
            query, {"$set": {"password": new_password}})
        if(old_password != new_password):
            return ("User %s, %s, %s password was successfully Updated" % (organization, first_name, last_name))
        else:
            return ("Error occured, User was not updated")

    def updateUserPRV(self, organization, first_name, last_name, new_privilege):
        organization = str(organization).lower()
        first_name = str(first_name).lower()
        last_name = str(last_name).lower()
        new_privilege = str(new_privilege).lower()

        user = self.findUser(organization, first_name, last_name)
        old_privilege = str(user["privilege"]).lower()
        query = {"organization": organization,
                 "first name": first_name, "last name": last_name}
        self.authdb["Users"].update_one(
            query, {"$set": {"privilege": new_privilege}})
        if(old_privilege != new_privilege):
            return ("User %s, %s, %s privilege was successfully Updated" % (organization, first_name, last_name))
        elif(old_privilege == new_privilege):
            return ("Privilege given was same as database")
        else:
            return ("Error occured, User was not updated")

    def deleteCollection(self, collection=None):
        collection = self.authdb["Users"]
        collection.drop()
        result = self.checkCollectionExists(collection)
        if(result is None):
            return ("Collection %s successfully deleted" % collection)
        else:
            return ("Error occured, Collection was not removed")

    def checkDBExists(self, db_name=None):
        if(db_name == None):
            db_name = self.authdb
        dblist = self.client.list_database_names()
        if db_name in dblist:
            return ("The database %s exists." % db_name)

    def checkCollectionExists(self, collection=None):
        if(collection == None):
            collection = self.authdb["Users"]
        collist = self.authdb.list_collection_names()
        if collection in collist:
            return ("The collection %s exists." % collection)
