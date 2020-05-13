from typing import List, Dict
from .table_formatter import TableFormatter


class TableBuilder:
    def __init__(self):
        pass

    def build_table(self, header: List[str], data: List[List[str]], formatter: TableFormatter = TableFormatter()) -> None:
        maximum_width = self._get_maximum_width_of_each_column(header=header, data=data)

        self._print_horizontal_lines(maximum_width=maximum_width)

        self._print_header(maximum_width=maximum_width, header=header)

        self._print_horizontal_lines(maximum_width=maximum_width)

        self._print_data(maximum_width=maximum_width, data=data, formatter=formatter)

        self._print_horizontal_lines(maximum_width=maximum_width)

    def _print_horizontal_lines(self, maximum_width: Dict[int, int]):
        for i in range(len(maximum_width)):
            print('+', end='')
            print((maximum_width[i]+2) * '-', end='')
        print('+')

    def _print_header(self, header: List[str], maximum_width: Dict[int, int]):
        print('|', end='')
        for i, text in enumerate(header):
            text_width_adjusted = '{}'.format(text).ljust(maximum_width[i])
            print(' {} |'.format(text_width_adjusted), end='')
        print()

    def _print_data(self, maximum_width: Dict[int, int], data: List[List[str]], formatter: TableFormatter):
        for row_index, row in enumerate(data):
            print('|', end='')
            for column_index, cell_content in enumerate(row):
                formated_content = formatter.format_cell(row_index=row_index, column_index=column_index, cell_content=cell_content)
                text_width_adjusted = '{}'.format(formated_content).ljust(maximum_width[column_index])
                print(' {} |'.format(text_width_adjusted), end='')
            print()

    def _get_maximum_width_of_each_column(self, header: List[str], data: List[List[str]]) -> Dict[int, int]:
        column_widths = {i: len(header[i]) for i in range(len(header))}
        for row in data:
            for i in range(len(row)):
                column_widths[i] = max(column_widths[i], len(row[i]))
        return column_widths
