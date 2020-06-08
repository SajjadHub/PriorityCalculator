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
            if data['proName'] not in self.projects:
                self.projects.append(project(data['proName'], data['proWeight']))
        
    def addProject(self, proName, proWeight):
        """Adds a json project to index"""
        if proName not in self.projects:
            newProject = project(proName, proWeight)
            self.projects.append(newProject)
            with open("json/" + str(proName) + ".txt", "w") as jsonFile:
                jsonProject = json.dumps(newProject, indent=2, cls=projectEncoder)
                print(jsonProject)

    def printProjects(self):
        """For testing"""
        for project in self.projects:
            project.printContents()



class project():

    """The project class holds information on a projects name, weight, and
    assignments, and assignment weights"""

    def __init__(self, proName, proWeight):
        self.proName = proName
        self.proWeight = proWeight
        self.assignments = {}

    def printContents(self):
        print('Project name is ' + self.proName)
        print('Projcet weight is ' + str(self.proWeight))
        for assig in self.assignments:
            print(assig)


os.system('clear')
sajjad = user("sajjad")
sajjad.addProject("Priority Calculator", 10)
sajjad.addProject("Machine Learning", 12)
sajjad.printProjects()
