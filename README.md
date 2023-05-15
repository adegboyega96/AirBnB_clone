# AirBnB clone - The console
![AirBnB Logo](https://miro.medium.com/v2/resize:fit:1400/0*NChTo-XqLOxLabIW)

## Project Description
The initial phase of the AirBnB clone project focused on developing the backend of the application and integrating it with a console interface using the cmd module in Python. Throughout this phase, Python objects were created and managed, and the resulting data was stored in a JSON file format, which can be easily accessed using the json module in Python.

## Description of the command interpreter
The command-line interface of the application resembles the Bash shell, but with a specific set of accepted commands that were designed exclusively for the usage of the AirBnB website. This command-line interpreter serves as the front-end of the web application, allowing users to interact with the back-end, which was developed using object-oriented programming (OOP) techniques in Python.

## How to start it
To start the command interpreter, follow these steps:
1. Clone the repository from GitHub:
```
git clone https://github.com/adegboyega96/AirBnB-clone.git
```
2. Navigate to the project directory:
```
cd AirBnB-clone
```
After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.

> /console.py : The main executable of the project, the command interpreter.
>
> models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances
> 
> models/__ init __.py:  A unique `FileStorage` instance for the application
> 
> models/base_model.py: Class that defines all common attributes/methods for other classes.
> 
> models/user.py: User class that inherits from BaseModel
> 
>models/state.py: State class that inherits from BaseModel
>
>models/city.py: City class that inherits from BaseModel
>
>models/amenity.py: Amenity class that inherits from BaseModel
>
>models/place.py: Place class that inherits from BaseModel
>
>models/review.py: Review class that inherits from BaseModel

## How to use it
It can work in two different modes:
**Interactive** and **Non-interactive**.
In Interactive mode, the command interpreter will present a prompt (hbnb) on the console, signaling that the user can input and execute a command. Once a command is executed, the interpreter will display the output or perform the corresponding action, and then display the prompt again, waiting for a new command. This cycle can continue indefinitely until the user chooses to exit the program.


```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

In Non-interactive mode, the shell should be invoked with a command provided as input through piping, ensuring that the command is executed immediately upon starting the shell. In this mode, no prompt will be displayed, and there will be no further expectation of user input.

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Examples
```

user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
39faff9a-0217-451f-87b6-912505b55907
user@ubuntu:~/AirBnB$ ./console.py

```

or

```
user@ubuntu:~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py
(hbnb)
e47ebcd3-f8e1-4c1f-8095-7b019070b1fa
(hbnb)
user@ubuntu:~/AirBnB$ ./console.py
```

## Available commands and what they do

The recognizable commands by the interpreter are the following:

|Command| Description |
|--|--|
| **quit or EOF** | Exits the program |
| **Usage** | By itself |
| **-----** | **-----** |
| **help** | Provides a text describing how to use a command.  |
| **Usage** | By itself --or-- **help <command\>** |
| **-----** | **-----** |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **Usage** | **create <class name\>**|
| **-----** | **-----** |
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **Usage** | **show <class name\> <id\>** --or-- **<class name\>.show(<id\>)**|
| **-----** | **-----** |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **Usage** | **destroy <class name\> <id\>** --or-- **<class name>.destroy(<id>)** |
| **-----** | **-----** |
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **Usage** | By itself or **all <class name\>** --or-- **<class name\>.all()** |
| **-----** | **-----** |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **Usage** | **update <class name\> <id\> <attribute name\> "<attribute value\>"** ---or--- **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** --or-- **<class name\>.update(<id\>, <dictionary representation\>)**|
| **-----** | **-----** |
| **count** | Retrieve the number of instances of a class.  |
| **Usage** | **<class name\>.count()** |

## Authors
Emmanuel Adetoro | Email: [emmanueladetoro72@gmail.com](mailto:emmanueladetoro72@gmail.com) 
Oladipo Solarin | Email: [justsolarin@gmail.com](mailto:justsolarin@gmail.com) 

