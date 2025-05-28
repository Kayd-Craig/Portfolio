class File:
    def __init__(self, path: str, contents: str | None = None) -> None:
        self.path = path
        self.name = self.get_name()
        self.contents = contents if contents else self.get_contents()

    def get_name(self) -> str:
        return self.path.split("/")[-1]

    def get_contents(self) -> str:
        with open(self.path, "r") as file:
            return file.read()

    def save_file(self) -> None:
        with open(self.path, "w") as file:
            file.write(self.contents)
