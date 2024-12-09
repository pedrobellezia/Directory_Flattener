from pathlib import Path
import json


def dir_flattener(directory):
    p = Path(directory)
    filerelations = {}

    stack = [p]
    while stack:
        current = stack.pop()
        for item in current.iterdir():
            if item.is_dir():
                stack.append(item)
            elif item.is_file():
                filerelations[str(item)] = item.name

    return filerelations


def save_json(json_data, j_name):
    with open(f"{j_name}.json", "w", encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
    print(f"Arquivo '{j_name}.json' salvo com sucesso!")


def main(directories, j_name):
    all_data = {}

    for path in directories:
        dir_name = Path(path).name
        all_data[dir_name] = dir_flattener(path)

    save_json(all_data, j_name)


if __name__ == "__main__":
    path_list = [r"C:\Users\pedrobs\Desktop\Nova pasta", r"C:\Users\pedrobs\Desktop\123"]
    json_name = "downloads"

    main(path_list, json_name)
