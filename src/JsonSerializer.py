# Class to create and test Json creation
import json

# Test data
class TestClass:

    def __init__(self, name, hit_dice):
        self.name = name
        self.hit_dice = hit_dice

# Use the user to make some data
print("Here is a test way to make some data!")
while(True):                                        # NOT IMPLEMENTED YET
    new_char = TestClass
    print("Enter a class name:")
    break

# Main stuff
filepath = 'test.json'
newData = {
    "ArtificerClass": {
        "name": "Artificer", 
        "hit dice": {
            "number":1,
            "faces":8
            }
        }
    
    }

with open(filepath, "w") as file:
    json.dump(newData, file, indent=4)