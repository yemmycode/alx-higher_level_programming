#!/usr/bin/python3
"""Module for processing standard input and outputting file metrics.
Prints accumulated file size and status code counts every ten lines or upon keyboard interruption (CTRL + C).
"""

def display_metrics(total_size, code_counts):
    """Displays the collected file metrics.
    Args:
        total_size (int): The total size of the files processed.
        code_counts (dict): The counts of each status code encountered.
    """
    print("File size: {}".format(total_size))
    for code in sorted(code_counts.keys()):
        print("{}: {}".format(code, code_counts[code]))

def main():
    import sys

    total_size = 0
    code_counts = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    line_counter = 0

    try:
        for input_line in sys.stdin:
            line_counter += 1
            parts = input_line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                continue

            try:
                if parts[-2] in code_counts:
                    code_counts[parts[-2]] += 1
            except IndexError:
                continue

            if line_counter % 10 == 0:
                display_metrics(total_size, code_counts)

    except KeyboardInterrupt:
        display_metrics(total_size, code_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
