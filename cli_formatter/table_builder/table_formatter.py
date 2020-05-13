
class TableFormatter:
    def __init__(self):
        pass

    def format_cell(self, row_index: int, column_index: int, cell_content: str) -> str:
        """ length should stay the same, the formatting is meant for e.g. coloring single cells """
        return cell_content
