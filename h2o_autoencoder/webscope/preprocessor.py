import h2o
import os
import h2o.frame
import h2o.model.metrics_base
import pandas as pd
from tqdm import tqdm


full_frame = pd.read_csv("/home/wso2123/My  Work/Datasets/Webscope/A1Benchmark/real_1.csv")
full_frame = full_frame.drop(['timestamps'], axis=1)

for i in tqdm(range(1,68)):
    file_name = "/home/wso2123/My  Work/Datasets/Webscope/A1Benchmark/real_"+str(i)+".csv"
    frame = pd.read_csv(file_name)
    frame = frame.drop(['timestamps'], axis=1)
    full_frame = full_frame.append(frame)

print full_frame
full_frame.to_csv("/home/wso2123/My  Work/Datasets/Webscope/A1Benchmark/A1Benchmark_full.csv",index=False)

# def main():
#
#     for i in [3,4]:
#         print (i%3+1),"---------------------------------------------------------------------"
#         # Dataset paths
#         data = "/home/wso2123/My  Work/Datasets/Webscope/A" + str(i) + "Benchmark/A" + str(i) + "Benchmark_full.csv"
#         normal_data = "/home/wso2123/My  Work/Datasets/Webscope/A" + str(i) + "Benchmark/A" + str(i) + "Benchmark_normal.csv"
#         for j in tqdm(range(1)):
#
#             full_frame = pd.read_csv(data)
#             normal_frame = pd.read_csv(normal_data)
#             print len(full_frame), len(normal_frame), "\n"
#             sample_ratio = 1 - (len(full_frame) * 0.7) / len(normal_frame)
#
#             if sample_ratio < 0.1:
#                 validate_frame = normal_frame.sample(frac=0.1, random_state=200)
#             else:
#                 validate_frame = normal_frame.sample(frac=sample_ratio, random_state=200)
#
#             train_frame = normal_frame.drop(validate_frame.index)
#
#             print sample_ratio
#
#             test_frame = get_test_frame(full_frame, 0.3)
#             uncorrected_train_frame = full_frame.drop(test_frame.index)
#             validate_frame.to_csv("/home/wso2123/My  Work/Datasets/Webscope/A" + str(i) + "Benchmark/validate.csv", index=False)
#             train_frame.to_csv("/home/wso2123/My  Work/Datasets/Webscope/A" + str(i) + "Benchmark/train.csv", index=False)
#             test_frame.to_csv("/home/wso2123/My  Work/Datasets/Webscope/A" + str(i) + "Benchmark/test.csv", index=False)
#             uncorrected_train_frame.to_csv("/home/wso2123/My  Work/Datasets/Webscope/A" + str(i) + "Benchmark/uncorrected_train.csv", index=False)
#
#             print "Task Completed"
#
#
# def get_test_frame(frame, sample_ratio):
#     return frame.sample(frac=sample_ratio, random_state=200)
#
#
# def get_normal_frame(frame, response_var, lbl):
#
#     lbl_list = frame[response_var]
#     new_frame = []
#     for i in range(len(lbl_list)):
#         if lbl_list[i, 0] == lbl:
#             if len(new_frame) == 0:
#                 new_frame = frame[i, 0:]
#             else:
#                 new_frame = new_frame.rbind(frame[i, 0:])
#     return new_frame
#
#
# def get_anomaly_frame(frame, response_var, lbl):
#
#     lbl_list = frame[response_var]
#     new_frame = []
#     for i in range(len(lbl_list)):
#         if lbl_list[i, 0] != lbl:
#             if len(new_frame) == 0:
#                 new_frame = frame[i, 0:]
#             else:
#                 new_frame = new_frame.rbind(frame[i, 0:])
#     return new_frame
#
#
# def get_pandas_frame(frame, lbl):
#     lbl_list = frame.iloc[:, -1]
#     new_frame = frame.iloc[0, :]
#     for i in tqdm(range(1, len(lbl_list))):
#         if lbl_list.iloc[i] == lbl:
#             df1 = frame.iloc[i, :]
#             new_frame = new_frame.append(df1)
#     return new_frame
#
#
# def get_train_frame(frame):
#     str_data = frame.get_frame_data()
#     lbl_list = str_data.split("\n")
#     # lbl_list = frame["C42"]
#     test_frame=pd.DataFrame(frame)
#     new_frame = pd.DataFrame()
#
#     for i in tqdm(range(len(lbl_list))):
#         if lbl_list[i].split(",")[-1] == "\"normal.\"":
#             df1 = test_frame.iloc[i, :]
#             new_frame = new_frame.append(df1)
#     return new_frame
#
# if __name__ == '__main__':
#     main()
