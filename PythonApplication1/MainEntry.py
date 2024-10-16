from DreamsAndHopes import AsciiTableWritable


def main():
    Ascii = AsciiTableWritable.ASCII()

    path = "ASCII.txt"

    Ascii.create_ascii_table()
    Ascii.debug_print()
    Ascii.write_file(path)
    Ascii.print_from_file(path)

if __name__ == "__main__":
    main()