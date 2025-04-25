def get_project_name(s: str) -> str:
    names = s.split('get')
    split_names = []
    idx_flag = 0
    for idx, n in enumerate(names[1]):
        if n == str(n).upper() and idx != 0:
            split_names.append(names[1][idx_flag:idx])
            idx_flag = idx
    split_names.append(names[1][idx_flag:])
    rtr_str = '_'.join(split_names)
    return rtr_str


if __name__ == '__main__':
    s = "getProjectNameJava"

    expected = 'Project_Name_Java'
    print(expected == get_project_name(s))