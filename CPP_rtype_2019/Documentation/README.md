# Welcome to CPP_rtype_2019 👋

> In the Advanced C++ track, you will delve deeper into the architecture of a C++ program. You will have to make projects that build and run the same on Unix (which you should be accustomed to now) and Windows systems.
The projects are based on industry usages of C++.

> Therefore, we are going to introduce this very profound philosophic difference between Unix and Windows in a way that serves our purposes: creating software abstractions that allow natively portable programs to be developed on all of the systems. 

> This abstraction focuses on a key concept that governs the entirety of our course's themes: Application Programming Interfaces (API),  which are elements that are inseparable from Object-Oriented Programming, all languages combined. 

> In this unit in particular, you will have to make a copy of the R-Type game.

## Install

First of all, you'll need to add the remote of three conan's repository.

For the conan-center repository :
```sh
conan remote add <REMOTE> https://api.bintray.com/conan/conan/conan-center 
```


For the bintray repository :

```sh
conan remote add <REMOTE> https://api.bintray.com/conan/bincrafters/public-conan 
```

To build the project :

```sh
mkdir build && cd build && conan install .. && cmake .. -G & "Unix Makefiles" && cmake --build .
```

Or execute :
```sh 
./building
```

##### All executables will be in the './build/bin' directory at the root of the project.

## To use the game :

1. Execute ./bin/r-type_server
2. In a new terminal, execute ./bin/r-type_client

3. Enjoy your party !

# How to play ?

Use your arrow to move your ships and use your space bar to shot on the ennemies.

##### ! If you write a wrong command you'll see "Invalid comman. Please check syntax." !


## Author

👤 **Antoine LEVY**



***