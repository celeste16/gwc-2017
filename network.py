class User:
 # Define the fields and methods for your object here.
     def __init__(self, newUsername, newUserID):
         self.username = newUsername
         self.userID = newUserID
         self.friends = []

     def getUserName(self):
         return self.username

     def getUserID(self):
         return self.userID

     def getFriends(self):
         return self.friends


     def addFriends(self, friendID):
         self.friends.append(friendID)


class Network:
  #Define the program flow for your user interface here.
     def __init__(self):
         self.users=[]

     def numUsers(self):
         return len(self.users)

     def addUserID(self, username):
         user_id=len(self.users)
         self.users.append(User(username,user_id))

     def getUserID(self, username):
         for user in self.users:
             if username==user.getUserName():
                user_id=user.getUserID()
         return user_id

     def addConnection(self, user1, user2):
        user1_id=self.getUserID(user1)
        user2_id=self.getUserID(user2)

        user1=self.users[user1_id]
        user2=self.users[user2_id]

        self.users[user2_id].addFriends(user1_id)
        self.users[user1_id].addFriends(user2_id)

     def printUsers(self):
        print("This is the Network")
        for user in self.users:
            print("\tuser {}: {}:".format(user.getUserID(), user.getUserName()))

     def printConnections(self, username):
        user=self.users[self.getUserID(username)]
        connections=user.getFriends()
        print("\t{}'s connections:".format(user.getUserName()))
        for friendID in connections:
            friend=self.users[friendID]
            print("\t{}".format(friend.getUserName()))





def main():
    # Define the program flow for your user interface here.
    mynetwork = Network()
    done=False
    while not done:
        action=input("\nWhat would you like to do?Add a user(u), Add a connection (c), print Users (p), print connections (pc), exit (e)")
        if action=="u":
             username=input("What username?")
             mynetwork.addUserID(username)
        elif action=="c":
             if mynetwork.numUsers()<2:
                print("ERROR.Dont have enough users.")
                continue
             else:
                 user1=input("First User?")
                 user2=input("Second User?")
             mynetwork.addConnection(user1,user2)
        elif action=="pc":
             user = input("What user?")
             mynetwork.printConnections(user)
        elif action=="p":
             mynetwork.printUsers()
        elif action=="e":
             print("Sorry to see you go")
             done=True
        else:
            print("ERROR. No, baby what is you doing?")
#runs your program.
if __name__ == '__main__':
    main()
