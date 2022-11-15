"""Dictionary related utility functions."""

__author__ = "730579449"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads the rows of a csv into a 'table' (list of dicts)."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table into a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(total_data: dict[str, list[str]], rows_amount: int) -> dict[str, list[str]]:
    """Making a table based off first few rows."""
    mini_table: dict[str, list[str]] = {}
    for column in total_data:
        i: int = 0
        values: list[str] = []
        if rows_amount >= len(total_data[column]):
            return total_data
        while i < rows_amount:
            values.append(total_data[column][i])
            i += 1
        mini_table[column] = values
    return mini_table


def select(data_table: dict[str, list[str]], column_title: list[str]) -> dict[str, list[str]]:
    """Selects columns and creates subset."""
    new_table: dict[str, list[str]] = {}
    for column in column_title:
        new_table[column] = data_table[column]
    return new_table


def concat(first_table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Function combines two tables."""
    combo_table: dict[str, list[str]] = {}
    for column in first_table:
        combo_table[column] = first_table[column]
    for column in second_table:
        if column in combo_table:
            combo_table[column] += second_table[column]
        else:
            combo_table[column] = second_table[column]
    return combo_table


def count(xs: list[str]) -> dict[str, int]:
    """Counts up amount of times values appear in a given list."""
    tallies: dict[str, int] = {}
    for value in xs:
        if value in tallies:
            tallies[value] = tallies[value] + 1
        else: 
            tallies[value] = 1
    return tallies