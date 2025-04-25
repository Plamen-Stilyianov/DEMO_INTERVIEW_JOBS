def print_result(employeesInput, friendshipsInput):
    empFrn = {}

    for emp in employeesInput:
        frns = list()
        for frn in friendshipsInput:
            if frn[0] == emp:
                frns.append(frn[1])
            elif frn[1] == emp:
                frns.append(frn[0])
            else:
                continue
        empFrn[emp] = frns

    for item in empFrn.items():
        print(item)


def run():
    employeesInput = {
        '1': ('Richard', 'Engineering'),
        '2': ('Erlich', 'HR'),
        '3': ('Monica', 'Business'),
        '4': ('Dinesh', 'Engineering'),
        '6': ('Carla', 'Engineering')
    }

    friendshipsInput = [
        ('1', '2'),
        ('1', '3'),
        ('2', '4')
    ]

    print_result(employeesInput, friendshipsInput)


if __name__ == '__main__':
    run()
