import first_class
import Rectangle
import Parallelepipede as par
from person import Student as stu
from bank import BankAccount as ba

def menu():
    print('\n===== MENU =====\n'
          '1 - To read a poem\n'
          '2 - How many lines in a story do not start with T\n'
          '3 - Count the number of words in the story file\n'
          '4 - Find the total number of the work "the" in notes\n'
          '5 - Display words in story.text with 4 or less characters\n'
          '6 - Count this and these in a file\n'
          '7- Count words ending with e in story.txt\n'
          '8 - Display attributes from another class\n'
          '9 - Rectangle class\n'
          '10 - Use Parallelepipede class\n'
          '11 - Testing the Student class\n'
          '12 - Use Banking Program\n'
          'e -  Exit program')


def read_a_poem():
    with open("poem.txt", 'r') as poem:
        print(poem.read() + '\n')


def count_lines_without_t():
    count = 0
    with open("story.txt", 'r') as story:
        for i in story:
            if i[0] != 'T':
                count = count + 1
    print(count)


def count_number_of_words_in_story_file():
    words = 0
    with open("story.txt", "r") as story:
        for i in story:
            words = words + len(i.split())
    print(words)


def find_the_in_notes_file():
    count = 0
    with open("notes.txt", "r") as notes:
        x = notes.read().split()
        for i in x:
            if i.lower() == "the":
                count = count + 1
    print(count)


def display_words():
    with open("story.txt", "r") as story:
        x = story.read().split()
        for i in x:
            if len(i) < 4:
                print(i)


def count_this_and_these_in_file():
    count = 0
    with open("article.txt", "r") as article:
        x = article.read().split()
        for i in x:
            if i.lower() == "this" or i.lower() == "these":
                count = count + 1
    print(count)


def count_words_ending_with_e():
    count = 0
    with open("story.txt", "r") as story:
        x = story.read().split()
        for i in x:
            if i[-1] == 'e':
                count = count + 1
    print(count)


def check_uppercase():
    count = 0
    with open("story.txt", "r") as story:
        x = story.read().split()
        for i in x:
            if i[0].isupper():
                count = count + 1
    print(count)

def display_attributes_of_myclass():
    person = first_class.MyClass("Test", "Name")
    person.display_attributes()


def rectangle_class():
    rect = Rectangle.Rectangle(10, 15)
    print(rect.display_data())


def parallelepipede_class():
    p = par.Parallelepipede(10, 15, 10)
    print(p.calculate_volume())


def test_student_class():
    student = stu("Test", 25, "Green")
    student.display_student()


def test_bank_account():
    me = ba(1001, "Test", 150.00)
    print("Add $50.00 to starting balance of $150.00")
    me.deposit(50.00)
    me.display_account_details()
    print("******************")
    print("Withdrawl $25.00 from balance")
    me.withdrawl(25.00)
    me.display_account_details()
    print("*******************")
    print("Apply bank fees ")
    me.bank_fees()
    me.display_account_details()


if __name__ == '__main__':

    while True:
        menu()
        print("")
        selection = input("Plese select from the menu")
        if selection == "e":
            break
        elif  selection == "1":
            read_a_poem()
        elif  selection == "2":
            count_lines_without_t()
        elif  selection == "3":
            count_number_of_words_in_story_file()
        elif  selection == "4":
            find_the_in_notes_file()
        elif  selection == "5":
            display_words()
        elif  selection == "6":
            count_this_and_these_in_file()
        elif  selection == "7":
            count_words_ending_with_e()
        elif  selection == "8":
            check_uppercase()
        elif  selection == "9":
            display_attributes_of_myclass()
        elif  selection == "10":
            rectangle_class()
        elif  selection == "11":
            test_student_class()
        elif  selection == "12":
            test_bank_account()
