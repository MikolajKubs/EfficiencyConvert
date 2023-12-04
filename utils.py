import pandas as pd
import datetime


def convert_string_into_list_not_empty(string):
    result = []
    for i in string.split("\n"):
        for j in i.split(" "):
            if j != "":
                result.append(j)

    return result


def convert_to_date(date_string):
    try:
        return datetime.datetime.strptime(date_string, '%d-%m-%Y').date()
    except ValueError:
        try:
            return datetime.datetime.strptime(date_string, '%d.%m.%Y').date()
        except ValueError:
            try:
                return datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
            except ValueError:
                try:
                    return datetime.datetime.strptime(date_string, '%m/%d/%Y').date()
                except ValueError:
                    if date_string == "25.10.02022":
                        return datetime.date(2022, 10, 25)
                    elif date_string == "00:00:00":
                        return None
                    else:
                        print("WTF: ", date_string)
                        return None


def print_head(df, rows_count):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'expand_frame_repr', False):
        print(df.head(rows_count))


def add_to_dataframe(df, rows):
    for row in rows:
        df.loc[-1] = row
        df.index += 1

    df = df.sort_index()

    return df
