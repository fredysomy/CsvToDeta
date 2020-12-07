import csv

import deta
import fire


def csv_to_deta(deta_id: str, path: str, db: str):
    """
    Reads in a CSV file and uploads its contents to a Deta Base
    :param str deta_id: The ID of your target Deta Base instance
    :param str path: The absolute path to the target CSV file
    :param str db: The name of your Deta Base
    :return: None
    """
    deta = deta.Deta(deta_id)
    datafile = deta.Base(db)
    print(f"Reading CSV from {path}")
    with open(path) as csv_file:
        count = 0
        csv_reader = csv.DictReader(csv_file)
        for csv_row in csv_reader:
            datafile.insert(csv_row)
            print(f"Uploaded {csv_row}")
            count += 1
        print(f"Succesfully uploaded {count} rows to {db} Deta Base")


def main():
    fire.Fire({
        "csvtodeta":csv_to_deta
    })


if __name__ == "__main__":
    main()
