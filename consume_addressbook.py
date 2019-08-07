import addressbook_pb2

# create the person object
person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"

# add a phone to the person
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME  # HOME is an enumerated value

