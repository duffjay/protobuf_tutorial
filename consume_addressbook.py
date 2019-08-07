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

# is it properly initialized?
person.Isinitialized()

# Abe
abe = addressbook_pb2.Person()
abe.id = 2000
abe.name = "Abe Lincoln"
abe.email = "abe@aol.com"

abe_phone = abe.phones.add()
abe_phone.number = "555-2000"
abe_phone.type = addressbook_pb2.Person.WORK

print ("Abraham Lincoln:", abe)

# George
geo = addressbook_pb2.Person()
geo.id = 3000
geo.name = "George Washington"
geo.email = "geo@hotmail.com"

geo_phone = geo.phones.add()
geo_phone.number = "555-3000"
geo_phone.type = addressbook_pb2.Person.HOME

print ("George Washington:", geo)

# create Martha Washington
# copy from Geo
martha = addressbook_pb2.Person()
martha.CopyFrom(geo)
print (martha)

# Serialize - bytes
serialized_geo = geo.SerializeToString()
print (type(serialized_geo)

