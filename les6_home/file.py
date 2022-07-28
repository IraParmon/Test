from pathlib import Path

path_to_file = input('Название файла: ')

path = Path(path_to_file)

if path.is_file():

    def main():

        with open(path_to_file) as f:
            print('Cамое длинное слово: ', max(f, key=len))


    if __name__ == "__main__":
        main()


else:
    print('Not found')
