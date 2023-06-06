import os
import json

dataFolder = "./src/data/"
dataAboutUsers = os.path.join(dataFolder, "users.json")
dataAboutPosts = os.path.join(dataFolder, "posts.json")



def getDataAboutUser():
    try:
        with open(dataAboutUsers, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Error: File not found!")
        exit()
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file!")
        exit()
        
        
def getIndividualDataAboutUser():
    try:
        with open(dataAboutUsers, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: File not found!")
        exit()
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file!")
        exit()
        
def getPostsData():
    try:
        with open(dataAboutPosts, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: File not found!")
        exit()
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file!")
        exit()
        
def getIndividualPostData():
    try:
        with open(dataAboutPosts, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error! File not found!")
        exit()
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file!")
        exit()