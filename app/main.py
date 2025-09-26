class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        persons.append(Person(name, age))

    for person_dict in people:
        name = person_dict["name"]
        current = Person.people[name]

        if "wife" in person_dict and person_dict["wife"] is not None:
            partner = Person.people[person_dict["wife"]]
            current.wife = partner
            partner.husband = current

        if "husband" in person_dict and person_dict["husband"] is not None:
            partner = Person.people[person_dict["husband"]]
            current.husband = partner
            partner.wife = current

    return persons
