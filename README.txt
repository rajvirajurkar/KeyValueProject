Title : Key Value store
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
  1. KVStore_cli.py is script to run CLI. It is build on python 3, so make sure you have python3 installed.
  2. Run following command to run CLI
      python3 KVStore_cli.py
  3. It prompt for following options
      Enter command:
        get <key>
        put <key> <value>
        exit
      >>>
========================================================================================

  
