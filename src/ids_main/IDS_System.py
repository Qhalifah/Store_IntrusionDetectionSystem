###
#
# Parser's the SQL query
#
###

import os
import socket

from template_detect import MatchTemplate
from template_train import TrainTemplate


class IDS:

    def __init__(self):
        self.trainTemplate = TrainTemplate()
        self.template = None

    def train(self, path="train.txt"):
        if not os.path.exists(path):
            print("Training file not found!")
            return False
        self.trainTemplate.train(path)
        self.template = self.trainTemplate.getTemplate()
        return True

    def detect(self, query="UPDATE table SET a=b"):
        if self.template is None:
            print("Template is not trained, please train the template first. Thanks!")
            return False
        self.matchTemplate = MatchTemplate(self.template)
        return self.matchTemplate.checkMatch(query)


    ###
    # Listens at a perticular port listening to for the connection
    # from the user end of the applicationself.
    # Binds to port 9999
    #
    # saves the connection in self.app and the server address in self.appAddr
    ###
    def connectToApplication(self):
        try:
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Bind the socket to the port
            sock.bind(('127.0.0.1', 8000))
            print("waiting for connection")
            sock.listen(1)
            self.app, self.appAddr = sock.accept()
            print("Successfull connected to application")
        except:
            print("Connection failed")
            return False
        return True

    ###
    # Receives upto 2048 bytes of data from the client application.
    # Any SQL query wont be more than 2048 bytes.
    ###
    def recvParse(self):
        queries = self.app.recv(2048)
        return queries.split(';')

    def sendToApp(self, data):
        self.app.send(data)

    ###
    # callQueryNode function passes the query to the query parser.
    # This class parsers the query and updates it the form of node.
    # Which could be further used to create template
    ###
    def callQueryNode(self, query):
        #parse query
        #query = Query(query)
        pass


    def run(self):
        validConnection = False
        while not validConnection:
            print("Connecting to Application")
            validConnection = ids.connectToApplication()
            print("Attemt failed, trying again!")

        self.start()

    def start(self):
        self.train()

        while True:
            transactionQueries = self.recvParse()
            result = True
            for query in transactionQueries:
                if not self.detect(query):
                    result = False
                    break
            self.sendToApp(result)


if __name__ == '__main__':
    ids = IDS()
    # ids.train()
    # ids.detect()
    ids.connectToApplication()
    # ids.start()