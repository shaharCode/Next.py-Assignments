
class IDIterator:
    def __init__(self, id):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        while self._id <= 999999999:
            if check_id_valid(self._id):
                valid_id = self._id
                self._id += 1
                return valid_id
            self._id += 1
        raise StopIteration


def check_id_valid(id_number):
    sum_digits = sum([(int(digit) * (1 + i % 2)) if int(digit) * (1 + i % 2) < 10 else (int(digit) * (1 + i % 2)) // 10
                     + (int(digit) * (1 + i % 2)) % 10 for i, digit in enumerate(str(id_number))])
    return sum_digits % 10 == 0


def id_generator(start_id):
    current_id = start_id + 1
    while current_id <= 999999999:
        if check_id_valid(current_id):
            yield current_id
        current_id += 1


def main():
    id = int(input("Enter ID: "))
    method = input("Generator or Iterator? (gen/it)? ")
    if method == "it":
        iterator = IDIterator(id)
    elif method == "gen":
        iterator = id_generator(id)
    else:
        print("Invalid input")
        return

    count = 0
    for valid_id in iterator:
        print(valid_id)
        count += 1
        if count == 10:
            break


if __name__ == "__main__":
    main()
