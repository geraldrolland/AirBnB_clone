AirBnB Clone (Console) Overview

This repository houses the fundamental components of the AirBnB project, including the base model for every object and corresponding classes, along with the essential storage file. Serving as a command-line console, it manages the commands required for the actual AirBnB website, offering a glimpse into the world of AirBnB and web applications.

Functionality and Objectives

Parent Class (BaseModel):
Responsible for initializing, serializing, and deserializing future instances.
Establishes a streamlined flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> File.

Creation of AirBnB Classes:
Develops classes for all entities used in AirBnB (User, State, City, Place, etc.), each inheriting from the BaseModel.

Abstracted Storage Engine:
Introduces the initial storage engine for the project, specifically a File storage system
