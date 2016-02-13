import sys


def main():
    filename = sys.argv[1]
    with open(filename, 'r') as fp:
        for line_number, line in enumerate(fp, 1):
            if 'hasattr' in line:
                concern = (
                    'hasattr should be avoided in Python 2,'
                    'see https://hynek.me/articles/hasattr/'
                )
                message = "{file}:{line_number} {concern}".format(
                    file=filename,
                    line_number=line_number,
                    concern=concern
                )
                print(message)

if __name__ == '__main__':
    main()
