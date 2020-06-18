import os
import json
from json import JSONEncoder
"""the program must take in an array of projects and scale the priority of
    assignments within projects
    according to ...?"""


class projectEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class user():

    """user holds the name of the user, projects, and project names for initial
    decleration
    and updating"""

    def __init__(self, username):
        self.username = username
        self.projects = []

    def getProjects(self):
        """Reads the index.txt file the user must create to initialize the
        the application"""
        with open("index.txt", "r") as jsonFile:
            data = json.load(jsonFile)
            for i, pro in enumerate(data):
                self.projects.append(project(pro['proName'], pro['proWeight']))
                for assig in pro['assignments']:
                    self.projects[i].addAssig(assignment(
                                              assig['assigName'],
                                              assig['assigWeight'],
                                              assig['deadline']))

    def addProject(self, project):
        """Adds a json project to index"""
        if project not in self.projects:
            self.projects.append(project)
            self.updateJson()

    def clearProjects(self):
        """clears all projects"""
        del self.projects[:]
        self.updateJson()

    def updateJson(self):
        """Updates the index json to include all projects (for when changes are\
                made)"""
        with open("index.txt", "w") as jsonFile:
            json.dump(self.projects, jsonFile, indent=2,
                      cls=projectEncoder)

    def printProjects(self):
        """For testing"""
        for project in self.projects:
            project.printContents()

    def calcPriority(self):
        """Calculates the priority rating for every assignment and returns
        a list of the top 10"""


class project():

    """The project class holds information on a projects name, weight, and
    assignments"""

    def __init__(self, proName, proWeight):
        self.proName = proName
        self.proWeight = proWeight
        # each project has an array of assignment objects
        self.assignments = []

    def printContents(self):
        print('Project name: ' + self.proName)
        print('Projcet weight: ' + str(self.proWeight))
        print('Assignments: ')
        for assig in self.assignments:
            assig.printAssig()
            print()

    def addAssig(self, assig):
        """Adds an assignment to the project"""
        if assig not in self.assignments:
            self.assignments.append(assig)


class assignment():
    """The assignment class holds information on the assignment name, weight,
    and due date"""
    def __init__(self, assigName, assigWeight, deadline, completed=False):
        self.assigName = assigName
        self.assigWeight = assigWeight
        self.deadline = deadline
        self.completed = [] if completed is False else completed

    def printAssig(self):
        print('Name: {}'.format(self.assigName))
        print('Weight: {}'.format(self.assigWeight))
        print('Deadline: {}'.format(self.deadline))

    def setCompleted(self):
        self.completed = True


os.system('clear')
sajjad = user("sajjad")
sajjad.getProjects()
sajjad.printProjects()
