import random

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self):
        if self.length() > 0:
            return self.queue.pop(-1)
        else:
            return False

    def length(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # iterate through numUsers and create a new user for each one

        # Add users
        # loop over a range of 0 to numUsers
        for i in range(0, numUsers):
            # add user to the graph
            self.addUser(f"User {i}")

        # create friendships

        # Generate all friendship combinations
        # make a list of possible friendships
        possibleFriendships = []
        # avoid duplicates ensuring that the first number is smaller than the second
        
        # loop over userID in users
        for userID in self.users:
            # loop over friend id in a range from user id + 1 to the lastID +1
            for friendID in range(userID + 1, self.lastID + 1):
                # append the tuple of (user id , friend id) to the possible friendships list
                possibleFriendships.append((userID, friendID))
        # shuffle the possible friendships using the random.shuffle method
        random.shuffle(possibleFriendships)
        # create a friendship of the first x amount of pairs in the list   
        # X determined by the formula: numusers * avgFriendships // 2
        # we need to divide by to as each createFriendship adds 2 friendships
        # loop over a range to numUsers * avgFriendships // 2
        for i in range(numUsers * avgFriendships // 2):
            # set the friendship to possible friends at i
            friendship = possibleFriendships[i]
            # addfriendship of friendship[0] and friendship[1]
            self.addFriendship(friendship[0], friendship[1])
            

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # create a queue
        frontier = Queue()
        # add the user element to the queue as a list
        frontier.enqueue([userID])
        # while the queue is not empty keen looping
        while frontier.length() > 0:
            # dequeue the first item and set to path
            path = frontier.dequeue()
            # access the last element and set it to current_person
            current_person = path[-1]
            # loop through all the friends of that item
            for friend in self.friendships[current_person]:
                 # check to see if node has already been visited
                if friend not in visited.keys() and current_person not in visited.keys():
                    # create a new list from the path
                    new_path = list(path)
                    # append the friend
                    new_path.append(friend)
                    # add the path to the queue
                    frontier.enqueue(new_path)
                    # add the path to the visited under the key of current_item
                    visited[current_person] = new_path

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    connections = sg.getAllSocialPaths(1)
    print(connections)
