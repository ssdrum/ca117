#!/usr/bin/env python3

class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} {self.phone} {self.email}"


class ContactList(object):

    def __init__(self, contacts=None):
        self.contacts = {} if contacts is None else contacts

    def add(self, c):
        self.contacts[c.name] = c

    def get(self, cname):
        if cname in self.contacts:
            return self.contacts[cname]
        else:
            return None

    def remove(self, cname):
        try:
            del self.contacts[cname]
        except KeyError:
            pass

    def __str__(self):
        output = ["Contact list", "------------"]
        for cname in sorted(self.contacts):
            c = self.contacts[cname]
            output.append(self.contacts[cname].__str__())
        return "\n".join(output)


def main():
    pass


if __name__ == "__main__":
    main()
