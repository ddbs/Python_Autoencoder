import h2o
import os
import h2o.frame
import h2o.model.metrics_base
import pandas as pd
from tqdm import tqdm


def main():
    # Dataset paths
    cancer_data = "/home/wso2123/My Work/Datasets/Breast cancer wisconsin/data.csv"
    cancer_data_normal = "/home/wso2123/My Work/Datasets/Breast cancer wisconsin/Breast cancer wisconsin_normal.csv"
    musk_clean1 = "/home/wso2123/My Work/Datasets/Musk/clean1.data"
    musk_clean2 = "/home/wso2123/My Work/Datasets/Musk/clean2.data"
    ionosphere_data = "/home/wso2123/My Work/Datasets/Ionosphere/ionosphere.csv"
    kddcup_data_set1 = "/home/wso2123/My Work/Datasets/KDD Cup/kddcup.data.corrected"
    kddcup_data_set1_normal = "/home/wso2123/My Work/Datasets/KDD Cup/kddcup.data.corrected_normal.csv"
    kddcup_data_set2 = "/home/wso2123/My Work/Datasets/KDD Cup/kddcup.data.corrected"

    os.environ['NO_PROXY'] = 'localhost'
    #
    # # Start H2O on your local machine
    h2o.init()

    full_frame = h2o.import_file(kddcup_data_set1)
    normal_frame = h2o.import_file(kddcup_data_set1_normal)
    print len(full_frame), len(normal_frame), "\n"
    sample_ratio = 1 - (len(full_frame)*0.7)/len(normal_frame)

    if sample_ratio < 0.1:
        validate_frame, train_frame = normal_frame.split_frame([0.1])
    else:
        validate_frame, train_frame = normal_frame.split_frame([sample_ratio])

    print sample_ratio

    uncorrected_train_frame,test_frame = full_frame.split_frame([0.7])
    h2o.export_file(validate_frame, "/home/wso2123/My Work/Datasets/KDD Cup/f_validate.csv")
    h2o.export_file(train_frame, "/home/wso2123/My Work/Datasets/KDD Cup/f_train.csv")
    h2o.export_file(test_frame, "/home/wso2123/My Work/Datasets/KDD Cup/f_test.csv")
    h2o.export_file(uncorrected_train_frame, "/home/wso2123/My Work/Datasets/KDD Cup/f_uncorrected_train.csv")
    #full_frame.to_csv("/home/wso2123/My Work/Datasets/KDD Cup/kddcup.data_10_percent_corrected_alpha.csv", index=False)
    # normal_frame = get_pandas_frame(full_frame, "normal.")
    # normal_frame.to_csv("/home/wso2123/My Work/Datasets/KDD Cup/kddcup.data_10_percent_corrected_normal.csv")
    print "Task Completed"
    #print normal_frame
    # anomaly_frame = get_anomaly_frame(full_frame,"C35","g")

    #h2o.export_file(normal_frame, "/home/wso2123/My Work/Datasets/KDD Cup/kddcup.data_10_percent_corrected_normal.csv")
    # h2o.export_file(anomaly_frame, "/home/wso2123/My Work/Datasets/Ionosphere/Ionosphere_anomaly.csv")
    # test_frame = np.random.choice(full_frame., int(len(full_frame)*0.7))
    # print test_frame


def get_test_frame(frame, sample_ratio):
    return frame.sample(frac=sample_ratio, random_state=200)


def get_normal_frame(frame, response_var, lbl):

    lbl_list = frame[response_var]
    new_frame = []
    for i in range(len(lbl_list)):
        if lbl_list[i, 0] == lbl:
            if len(new_frame) == 0:
                new_frame = frame[i, 0:]
            else:
                new_frame = new_frame.rbind(frame[i, 0:])
    return new_frame


def get_anomaly_frame(frame, response_var, lbl):

    lbl_list = frame[response_var]
    new_frame = []
    for i in range(len(lbl_list)):
        if lbl_list[i, 0] != lbl:
            if len(new_frame) == 0:
                new_frame = frame[i, 0:]
            else:
                new_frame = new_frame.rbind(frame[i, 0:])
    return new_frame


def get_pandas_frame(frame, lbl):
    lbl_list = frame.iloc[:, -1]
    new_frame = frame.iloc[0, :]
    for i in tqdm(range(1, len(lbl_list))):
        if lbl_list.iloc[i] == lbl:
            df1 = frame.iloc[i, :]
            new_frame = new_frame.append(df1)
    return new_frame


def get_train_frame(frame):
    str_data = frame.get_frame_data()
    lbl_list = str_data.split("\n")
    # lbl_list = frame["C42"]
    test_frame=pd.DataFrame(frame)
    new_frame = pd.DataFrame()

    for i in tqdm(range(len(lbl_list))):
        if lbl_list[i].split(",")[-1] == "\"normal.\"":
            df1 = test_frame.iloc[i, :]
            new_frame = new_frame.append(df1)
    return new_frame

if __name__ == '__main__':
    main()