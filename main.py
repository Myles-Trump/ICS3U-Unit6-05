#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: June 2021
# This program uses a list to determine the average mark of the user


def main():
    # this function uses a list to determine the average mark of the user

    grades = []
    marks_int = 0
    total = 0

    # input
    print("Please enter your grades (%). Enter -1 to end.")

    while marks_int != -1:
        marks = input("Enter your grade: ")

        try:
            marks_int = int(marks)
            if marks_int > -1 and marks_int < 101:
                grades.append(marks_int)
                total = total + marks_int

            elif marks_int < -1 or marks_int > 100:
                print("\nYou have entered an invalid integer, try again")

            else:
                pass

        except Exception:
            print("\nYou have entered an invalid input, try again.")

        finally:
            pass

    grades.pop()
    average = total / len(grades)

    print("\nYour average grade is {0}.".format(average))


if __name__ == "__main__":
    main()
