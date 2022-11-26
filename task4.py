import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file_name, delimiter=",", new_line="\n") -> list[dict]:
    with open(file_name) as scv:
        datas = scv.readlines()
        headers = datas[0].rstrip(new_line).split(delimiter)
        values = [datas[i].rstrip(new_line).split(delimiter) for i in range(1, len(datas))]
        list_dict_ = [{headers[j]: values[i][j] for j in range(len(headers))} for i in range(len(values))]
        return list_dict_


if __name__ == "__main__":
    print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
