from typing import List, Dict
from .table_formatter import TableFormatter
from .table_builder import TableBuilder


class TableBuilderAlternative(TableBuilder):
    def __init__(self):
        super().__init__()

    def build_table(self, header: List[str], data: List[List[str]], formatter: TableFormatter = TableFormatter()) -> None:
        maximum_width = self._get_maximum_width_of_each_column(header=header, data=data)

        self._print_header(maximum_width=maximum_width, header=header)

        self._print_horizontal_lines(maximum_width=maximum_width)

        self._print_data(maximum_width=maximum_width, data=data, formatter=formatter)

    def _print_horizontal_lines(self, maximum_width: Dict[int, int]):
        number_of_chars = sum(maximum_width.values()) + 3 * len(maximum_width) - 1
        print(number_of_chars * '-')

    def _print_header(self, header: List[str], maximum_width: Dict[int, int]):
        for i, text in enumerate(header):
            text_width_adjusted = '{}'.format(text).ljust(maximum_width[i])
            if i == len(header) - 1:
                print(' {}'.format(text_width_adjusted), end='')
            else:
                print(' {} |'.format(text_width_adjusted), end='')
        print()

    def _print_data(self, maximum_width: Dict[int, int], data: List[List[str]], formatter: TableFormatter):
        for row_index, row in enumerate(data):
            for column_index, cell_content in enumerate(row):
                formated_content = formatter.format_cell(row_index=row_index, column_index=column_index, cell_content=cell_content)
                text_width_adjusted = '{}'.format(formated_content).ljust(maximum_width[column_index])
                if column_index == len(maximum_width) - 1:
                    print(' {}'.format(text_width_adjusted), end='')
                else:
                    print(' {} |'.format(text_width_adjusted), end='')
            print()
