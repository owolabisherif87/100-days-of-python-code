from dataclasses import dataclass
import uuid
import questionary
from questionary import Choice, Question
from typing import Literal, Any
from enum import Enum


print("================ Contact Book ==============================")


@dataclass
class Contact:
    id: str | None
    name: str
    phone: str
    email: str | None
    address: str | None
    company: str | None
    occupation: str | None

    # def __repr__(self):
    #     return f"Contact(id={self.id}, name={self.name}, phone={self.phone}, \
    #     email={self.email}, address={self.address}, compnay={self.company}, occupation={self.occupation})"


class Action(Enum):
    ADD = 1
    LIST = 2
    EDIT = 3
    DELETE = 4
    EXIT = 5


ops: list[Choice] = [
    Choice(title="Add contact", value=Action.ADD),
    Choice(title="List contacts", value=Action.LIST),
    Choice(title="Edit contact", value=Action.EDIT),
    Choice(title="Delete contact", value=Action.DELETE),
    Choice(title="Exit", value=Action.EXIT)
]


add_questions: dict[str, Question] = {
    "name": questionary.text("Enter contact name", validate=lambda x: x != ""),
    "phone": questionary.text("Enter phone number"),
    "email": questionary.text("Enter email"),
    "address": questionary.text("Enter address"),
    "company": questionary.text("Enter company"),
    "occupation": questionary.text("Enter occupation")
}


def build_question(contact: Contact | None = None):
    if not contact:
        return {
            "name": questionary.text("Enter contact name", validate=lambda x: x != ""),
            "phone": questionary.text("Enter phone number"),
            "email": questionary.text("Enter email"),
            "address": questionary.text("Enter address"),
            "company": questionary.text("Enter company"),
            "occupation": questionary.text("Enter occupation")
        }

    return {
        "name": questionary.text(f"Edit contact name ({contact.name}) ", validate=lambda x: x != "", default=contact.name),
        "phone": questionary.text(f"Edit phone number ({contact.phone}) ", default=contact.phone),
        "email": questionary.text(f"Edit email ({contact.email}) "),
        "address": questionary.text(f"Edit address ({contact.address}) "),
        "company": questionary.text(f"Edit company ({contact.company}) "),
        "occupation": questionary.text(f"Edit occupation ({contact.company}) ")
    }


class ContactBook:
    def __init__(self):
        self.contacts: list[Contact] = []

    def add(self, contact: Contact) -> None:
        self.contacts.append(contact)

    def read(self):
        if not len(self.contacts):
            print("Contact list empty.")
            return

        print("======= Contact List ====================")
        for item in self.contacts:
            print(
                f"Name: {item.name}, Phone: {item.phone}, Email: {item.email}")
        print("=========================================")

    def edit(self, contact: Contact):
        index = [i for i, item in enumerate(
            self.contacts) if item.id == contact.id]

        if not len(index):
            print("Unable to edit contact")
            return

        self.contacts[index[0]] = contact

    def delete(self, contact: Contact):
        self.contacts.remove(contact)


book = ContactBook()

while True:
    action: Action = questionary.select(
        "Choose the action to perform", ops).ask()

    if action == Action.ADD:
        contact = Contact(id=str(uuid.uuid4()), **
                          questionary.form(**build_question()).ask())
        book.add(contact)
        print("New contact was added!")

    if action == Action.LIST:
        book.read()

    if action == Action.EDIT:
        if not len(book.contacts):
            print("Conctacts empty, please add first.")
            continue

        contact: Contact = questionary.select("Select the contact to edit.", [Choice(
            title=f"{item.name} ({item.phone})", value=item) for item in book.contacts]).ask()

        edited_contact = Contact(id=contact.id,
                                 **questionary.form(**build_question(contact)).ask())

        edited_contact = Contact(
            id=contact.id,
            name=edited_contact.name or contact.name,
            phone=edited_contact.phone or contact.phone,
            email=edited_contact.email or contact.email,
            address=edited_contact.address or contact.address,
            company=edited_contact.company or contact.company,
            occupation=edited_contact.occupation or contact.occupation
        )

        book.edit(edited_contact)

        print("Contact updated.")

    if action == Action.DELETE:
        if not len(book.contacts):
            print("Conctacts empty, please add first.")
            continue

        contact: Contact = questionary.select("Select the contact to delete.", [Choice(
            title=f"{item.name} ({item.phone})", value=item) for item in book.contacts]).ask()

        book.delete(contact)

        print(f"{contact.name} was deleted.")

    if action == Action.EXIT:
        print("Bye!")
        break
