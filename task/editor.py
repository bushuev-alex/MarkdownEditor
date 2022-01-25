class MarkdownEditor:

    def __init__(self):
        self.formats = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line',
                        'ordered-list', 'unordered-list']
        self.commands = ['!help', '!done']
        self.user_choice = None
        self.format = None
        self.text = None
        self.result = []

    def help(self):
        print('Available formatters:', *self.formats)
        print('Special commands:', *self.commands)

    def choice(self):
        while True:
            user_choice = input('Choose a formatter: ')
            if user_choice in self.commands:
                self.user_choice = user_choice
                if self.user_choice == '!help':
                    self.help()
                elif self.user_choice == '!done':
                    self.write()
                    break
            elif user_choice in self.formats:
                self.format = user_choice
                if self.format == "plain":
                    self.plain()
                elif self.format == "bold":
                    self.bold()
                elif self.format == "italic":
                    self.italic()
                elif self.format == "header":
                    self.header()
                elif self.format == "link":
                    self.link()
                elif self.format == "inline-code":
                    self.inline_code()
                elif self.format == "new-line":
                    self.new_line()
                elif self.format == "ordered-list":
                    self.ordered_list()
                elif self.format == "unordered-list":
                    self.unordered_list()
                print(*self.result, sep="")
            else:
                print('Unknown formatting type or command')

    def plain(self):
        self.text = input("Text: ")
        self.result.append(self.text)

    def bold(self):
        self.text = input("Text: ")
        line = f"**{self.text}**"
        self.result.append(line)

    def italic(self):
        self.text = input("Text: ")
        line = f"*{self.text}*"
        self.result.append(line)

    def inline_code(self):
        self.text = input("Text: ")
        line = f"`{self.text}`"
        self.result.append(line)

    def link(self):
        label = input("Label: ")
        url = input("URL: ")
        line = f"[{label}]({url})"
        self.result.append(line)

    def header(self):
        while True:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                self.text = input("Text: ")
                line = '#' * level + ' ' + self.text + '\n'
                self.result.append(line)
                break
            else:
                print("The level should be within the range of 1 to 6")

    def new_line(self):
        line = '\n'
        self.result.append(line)

    def ordered_list(self):
        while True:
            n_rows = int(input("Number of rows: "))
            if n_rows > 0:
                for n in range(1, n_rows + 1):
                    row = input(f"Row #{n}: ")
                    self.result.append(str(n) + '. ' + row + '\n')
                break
            else:
                print("The number of rows should be greater than zero")

    def unordered_list(self):
        while True:
            n_rows = int(input("Number of rows: "))
            if n_rows > 0:
                for n in range(1, n_rows + 1):
                    row = input(f"Row #{n}: ")
                    self.result.append('* ' + row + '\n')
                break
            else:
                print("The number of rows should be greater than zero")

    def write(self):
        with open("output.md", "w") as file:
            print(*self.result, sep="", end="", file=file)


my_editor = MarkdownEditor()
my_editor.choice()
