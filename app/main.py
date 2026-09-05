from os import mkdir, remove


def move_file(command: str) -> None:
    com, old_file, new_file = command.split(" ")
    path = new_file.split("/")
    current_path = ""
    for i in range(len(path) - 1):
        try:
            mkdir(f"{current_path}{path[i]}")
        except FileExistsError:
            continue
        finally:
            current_path += f"{path[i]}/"
    with (open(old_file, "r")) as old, (open(new_file, "w")) as new:
        new.write(old.read())
    remove(old_file)
