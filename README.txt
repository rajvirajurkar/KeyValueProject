Title : Key Value store Web service
author: Rajvi Rajurkar

========================================================================================
Project Setup and running : 
  1. Download or close the project
  2. This is maven project, so make sure u have installed with maven 3.3+ and java 1.8+
  3. Run following command to download and package the project
      cd KeyValueProject
      mvn clean package
  4. It generates target directory containing "keyvaluestore-1.0.jar" file
  5. Run following command to run web service
      java -jar target/keyvaluestore-1.0.jar
========================================================================================
Running CLI :
  1. KVStore_cli.py is script to run CLI. 
     It is built on python 3, so make sure you installed python3 and install "requests" package for python3
     Follow - https://www.python.org/downloads/ Or https://realpython.com/installing-python/ for installing python3
     Follow - https://docs.python.org/3/installing/index.html for installing "requests" package
     Note: "requests" is used to make get and put calls.
  2. Run following command to run CLI
      python3 KVStore_cli.py
  3. It prompt for following options
      Enter command:
        get <key>
        put <key> <value>
        exit
      >>>
========================================================================================

  
