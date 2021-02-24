import os

n_epochs = 2000
g_type = "gated_cnn"  # generator type : "gated_cnn" or "u_net"

sr = 16000  # sampling rate
n_features = 24  # Mceps coefficient
n_frames = 128  # fixed-length segment randomly
frame_period = 5.0  # extracted every 5 ms

DATASET_PATH = "/media/mint/Barracuda/Datasets/CommonVoiceMozillaIta/VoiceStyleTransfer"
dataset_A = os.path.join(DATASET_PATH, "train/A")
dataset_B = os.path.join(DATASET_PATH, "train/B")
test_dir = os.path.join(DATASET_PATH, "test")
direction = "A2B"

OUT_PATH = "/media/mint/Barracuda/Models/VoiceStyleTransfer/1"
log_dir = os.path.join(OUT_PATH, "log")
model_dir = os.path.join(OUT_PATH, "model")
test_output_dir = os.path.join(OUT_PATH, 'sample')
