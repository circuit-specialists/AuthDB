import pymongo


class MANAGER:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.authdb = self.client["AuthDB"]

    def addUser(self, organization, first_name, last_name, privilege):
        organization = str(organization).lower()
        first_name = str(first_name).lower()
        last_name = str(last_name).lower()
        privilege = str(privilege).lower()

        print("Trying to add User %s, %s, %s" %
              (organization, first_name, last_name))
        user = self.authdb["Users"].find_one(
            {"organization": organization, "first name": first_name, "last name": last_name})

        if(user is None):
            mydict = {"organization": organization, "first name": first_name,
                      "last name": last_name, "Privilege": privilege}
            self.authdb["Users"].insert_one(mydict)
            return ("Successfully added")
        else:
            db_find_organization = str(user["organization"]).lower()
            db_find_firstname = str(user["first name"]).lower()
            db_find_lastname = str(user["last name"]).lower()
            if(db_find_firstname == str(first_name).lower() and db_find_lastname == str(last_name).lower()):
                return ("User %s, %s, %s already exists" % (organization, first_name, last_name))

    def findUser(self, organization, first_name, last_name):
        organization = str(organization).lower()
        first_name = str(first_name).lower()
        last_name = str(last_name).lower()
        privilege = str(privilege).lower()

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
            return ("User %s, %s, %s successfully deleted" % (organization, first_name, last_name))
        else:
            return ("Error occured, User was not removed")

    def removeUsers(self, organization):
        organization = str(organization).lower()
        
        users = self.authdb["Users"].delete_many(organization)
        return (users.deleted_count, " documents deleted.")

    def removeAllUsers(self):
        users = self.authdb["Users"].delete_many({})
        return (users.deleted_count, " documents deleted.")

    def updateUser(self, organization, first_name, last_name, new_privilege):
        organization = str(organization).lower()
        first_name = str(first_name).lower()
        last_name = str(last_name).lower()
        privilege = str(privilege).lower()

        user = self.findUser(organization, first_name, last_name)
        old_privilege = str(user["privilege"]).lower()
        query = {"organization": organization,
                 "first name": first_name, "last name": last_name}
        self.authdb["Users"].update_one(
            query, {"$set": {"privilege": new_privilege}})
        new_privilege = str(user["privilege"]).lower()
        if(old_privilege == new_privilege):
            return ("User %s, %s, %s successfully Updated" % (organization, first_name, last_name))
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
        db_name = self.authdb
        dblist = self.client.list_database_names()
        if db_name in dblist:
            return ("The database %s exists." % db_name)

    def checkCollectionExists(self, collection=None):
        collection = self.authdb["Users"]
        collist = self.authdb.list_collection_names()
        if collection in collist:
            return ("The collection %s exists." % collection)
