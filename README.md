# BDA - Chatbot
This is the code base of the students @tbjauner and @tbmeile. We want to implement a question answering model. With the goal to be able to answer ionesoft inquiries. We are enhancing the language model with a wikipedia dump.

## Project structure
In order to achieve a clean architecture we are inspired by the onion architecture.
![Onion Architecture](http://blog.cleancoder.com/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg)

For more information see: http://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html

### Entities
Entities encapsulate Enterprise wide business rules. An entity can be an object with methods, or it can be a set of data structures and functions. It doesn’t matter so long as the entities could be used by many different applications in the enterprise.

### Use Cases
The software in this layer contains application specific business rules. It encapsulates and implements all of the use cases of the system. These use cases orchestrate the flow of data to and from the entities, and direct those entities to use their enterprise wide business rules to achieve the goals of the use case.
