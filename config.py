import os

n_epochs = 2000
g_type = "gated_cnn"  # generator type : "gated_cnn" or "u_net"

sr = 16000  # sampling rate
n_features = 24  # Mceps coefficient
n_frames = 128  # fixed-length segment randomly
frame_period = 5.0  # extracted every 5 ms

DATASET_PATH = "./data/"
dataset_A = os.path.join(DATASET_PATH, "train/son")
dataset_B = os.path.join(DATASET_PATH, "train/yuinna")
test_dir = os.path.join(DATASET_PATH, "test")
direction = "A2B"

log_dir = "./log"
model_dir = "./model"
test_output_dir = './sample'
