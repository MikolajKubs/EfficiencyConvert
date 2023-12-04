import pandas as pd
import utils

file_name = "SourceCompare.xlsm"
sheet = "NPM"


def main():
    df = pd.read_excel(io=file_name, sheet_name=sheet, header=11, skiprows=lambda x: x in [0, 11],
                       dtype={"NPM Requested Date(s)\n[DD.MM.YYYY]": str,
                              "NPM ID": str
                              }
                       )

    df = format_data_frame(df)

    final_df = pd.DataFrame(columns=df.columns)

    for index, row in df.iterrows():
        # print_row(df, index)
        result_rows = split_row_into_multiple(row)
        utils.add_to_dataframe(final_df, result_rows)

    utils.print_head(final_df, 10000)


def split_row_into_multiple(row: pd.Series):
    requested_date_cell: str = row["Requested Date"]

    result_rows = []

    if pd.isnull(requested_date_cell):
        return result_rows

    try:
        requested_dates = utils.convert_string_into_list_not_empty(requested_date_cell)

        for unformatted_date in requested_dates:
            date = utils.convert_to_date(unformatted_date)

            if date is not None:
                new_row = row.copy()
                new_row["Requested Date"] = date
                result_rows.append(new_row)

    except AttributeError:
        print("ERROR:", requested_date_cell)

    return result_rows


def format_data_frame(df):
    df = df.rename(columns={
        "NPM Requested Date(s)\n[DD.MM.YYYY]": "Requested Date",
        "Lead BU": "Business Unit",
        "Projektmanager": "Project Manager"})
    df = df[["NPM ID",
             "Project definition of Pre-Nom",
             "Business Unit",
             "Product/ Scope",
             "Project Manager",
             "Requested Date"]]

    return df


if __name__ == '__main__':
    main()
