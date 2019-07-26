import networkx as nx
import math
import matplotlib.pyplot as plt

users = [
    {"id": 0, "name": "Hero" },
    {"id": 1, "name": "Dunn" },
    {"id": 2, "name": "Sue" },
    {"id": 3, "name": "Chi" },
    {"id": 4, "name": "Thor" },
    {"id": 5, "name": "Clive" },
    {"id": 6, "name": "Hicks" },
    {"id": 7, "name": "Devin" },
    {"id": 8, "name": "Kate" },
    {"id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), 
        (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


friendships = {user["id"]: [] for user in users}
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)



num_friends_by_id = [(user["id"], number_of_friends(user)) 
                        for user in users]

num_friends_by_id_sorted = sorted(num_friends_by_id,
                                key=lambda id_and_friends: id_and_friends[1],
                                reverse=True)

id2name = {user["id"]: "{0}:{1}".format(user["id"], user["name"])  
              for user in users}

print("Users sorted by number of friends")
for (userid, numfriends) in num_friends_by_id_sorted:
    print("{0}    {1}    {2}".format(userid, id2name[userid], numfriends))



# Graph Drawing
maxfriends = num_friends_by_id_sorted[0][1]
node_sizes = []
node_colors = []
for (uid, numfriends) in num_friends_by_id:
    node_sizes.append(math.pow(2, numfriends)*1000/maxfriends)
    if numfriends == maxfriends:
        node_colors.append('r')
    else:
        node_colors.append('c')

G=nx.Graph()
G.add_edges_from(friendship_pairs)
Gt = nx.relabel_nodes(G, id2name)
nx.draw_kamada_kawai(Gt, with_labels=True, node_size=node_sizes, 
        node_color=node_colors)
plt.savefig('key_connectors.png')
plt.show()
