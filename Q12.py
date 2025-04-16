# Define a function fee that takes a base fee (integer) and roll number of a student (as string) and returns the
# total fee the student has paid till 2022-23.

DEPT = ["DS", "CS", "EE", "ME", ]
PROGRAM = [1, 2]


class InvalidRollException(Exception):
    """Raises the error when an invalid roll number is entered."""
    pass


def fee(base_fee, roll_no):
    try:
        if roll_no[:2] not in DEPT:
            raise InvalidRollException
        if int(roll_no[2:4]) < 18:
            raise InvalidRollException
        if int(roll_no[4:5]) not in PROGRAM:
            raise InvalidRollException
        if int(roll_no[4]) == 2 and int(roll_no[2:4]) < 20:
            raise InvalidRollException

    except InvalidRollException as err:
        print(f"InvalidRollException")

    else:
        dept = roll_no[:2]
        year_of_adm = int("20" + roll_no[2:4])
        program = int(roll_no[4])
        number_of_years = 2023 - year_of_adm
        yearly_fees = [base_fee]
        for i in range(1, number_of_years):
            curr_fees = yearly_fees[i-1] + yearly_fees[i-1] * 0.1
            yearly_fees.append(curr_fees)

        return sum(yearly_fees)


input_roll_no = input("Enter roll number: ")
input_fee = int(input("Enter the base fee: "))
print(f"Fees paid till now: {fee(input_fee, input_roll_no)}")
