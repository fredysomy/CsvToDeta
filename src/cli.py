import fire
import csv
from deta import Deta

def csvtodeta(id,path,db):
    deta = Deta(id)
    datafile = deta.Base(db)
    print("Reading data from {}".format(path))
    arr=[]
    with open (path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for csvRow in csvReader:
           arr.append(csvRow)
    for each in arr:
        datafile.insert(each)
        print("Uploaded {}".format(each))
    print("succesfully uploaded {} data to {} Base".format(len(arr),db))

def main():
    fire.Fire({
        "csvtodeta":csvtodeta
    })


if __name__=="__main__":
    main()
