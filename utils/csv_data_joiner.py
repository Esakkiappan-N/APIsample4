import pandas as pd

def read_test_data(testcase_id):
    df = pd.read_csv("testdata/web/login.csv")
    data = df[df["testcaseid"] == testcase_id].iloc[0]
    return data.to_dict()