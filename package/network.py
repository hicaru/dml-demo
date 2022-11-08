from p2pnetwork.node import Node
from p2pnetwork.nodeconnection import NodeConnection
import time


class MyOwnNodeConnection (NodeConnection):
    # Python class constructor
     def __init__(self, main_node, sock, id, host, port):
        super(MyOwnNodeConnection, self).__init__(main_node, sock, id, host, port)

    # Check yourself what you would like to change and override! See the 
    # documentation and code of the nodeconnection class.


class MyOwnPeer2PeerNode (Node):
    # Python class constructor
    def __init__(self, host, port, id=None, callback=None, max_connections=0):
        super(MyOwnPeer2PeerNode, self).__init__(host, port, id, callback, max_connections)

    # Override event functions...

    # Override this method to initiate your own NodeConnection class.
    def create_new_connection(self, connection, id, host, port):
        return MyOwnNodeConnection(self, connection, id, host, port)


node = MyOwnPeer2PeerNode("127.0.0.1", 10001)
time.sleep(1)

# Do not forget to start your node!
node.start()
time.sleep(1)

# Connect with another node, otherwise you do not create any network!
node.connect_with_node('127.0.0.1', 10002)
time.sleep(2)

# Example of sending a message to the nodes (dict).
node.send_to_nodes({"message": "Hi there!"})

time.sleep(5) # Create here your main loop of the application

node.stop()
