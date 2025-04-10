import sys

sys.path.append("/home/hoangminhthai/Documents/KHTN_CS115/machine-translation-transformer/src")

import torch
import torch.nn as nn

from modules.transformer import Transformer
from utils.tokenizer import tokenizer
from utils.field import create_field
from utils.translator import translate

from argparse import ArgumentParser
import json
import os

model_data_folder_vn_to_en = "/home/hoangminhthai/Documents/KHTN_CS115/machine-translation-transformer/models/vn_to_en"
model_data_folder_en_to_vn = "/home/hoangminhthai/Documents/KHTN_CS115/machine-translation-transformer/models/en_to_vn"
model_config_file = "/home/hoangminhthai/Documents/KHTN_CS115/machine-translation-transformer/models/config.json"
model_ckp_vn_to_en = "/home/hoangminhthai/Documents/KHTN_CS115/machine-translation-transformer/models/vn_to_en/model_best.pt"
model_ckp_en_to_vn = "/home/hoangminhthai/Documents/KHTN_CS115/machine-translation-transformer/models/en_to_vn/model_best.pt"

def model_initialize_vn_to_en():
    print("Waiting set up model from vn_to_en")

    print("Load config")
    with open(model_config_file, 'r') as file:
        cfg = json.load(file)

    max_strlen = cfg['max_strlen']
    k = cfg['k']
    print(json.dumps(cfg, indent=3))

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print(f"Use {device}")

    print("Creating tokenizer")
    en_tokenizer = tokenizer('en_core_web_sm')  # Initialize with the English model
    vi_tokenizer = tokenizer('xx_sent_ud_sm')

    src_field, trg_field = create_field(vi_tokenizer, en_tokenizer)
    print("Loading vocabulary")
    src_vocab = torch.load(os.path.join(model_data_folder_vn_to_en , 'src_vocab.pth'))
    trg_vocab = torch.load(os.path.join(model_data_folder_vn_to_en , 'trg_vocab.pth'))
    src_field.vocab = src_vocab
    trg_field.vocab = trg_vocab

    print("Loading model")
    model = Transformer(
        len(src_field.vocab),
        len(trg_field.vocab),
        d_model = cfg['d_model'],
        n = cfg['n_layers'],
        heads = cfg['heads'],
        dropout = cfg['dropout']
    )

    model_ckpt = torch.load(model_ckp_vn_to_en, map_location=torch.device(device))
    model.load_state_dict(model_ckpt)
    model = model.to(device)    

    print("Successfully set up the model from vn_to_en")
    return model, src_field, trg_field, max_strlen, device, k

def model_initialize_en_to_vn():
    print("Waiting set up model from en_to_vn")

    print("Load config")
    with open(model_config_file, 'r') as file:
        cfg = json.load(file)

    max_strlen = cfg['max_strlen']
    k = cfg['k']
    print(json.dumps(cfg, indent=3))

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print(f"Use {device}")

    print("Creating tokenizer")
    en_tokenizer = tokenizer('en_core_web_sm')  # Initialize with the English model
    vi_tokenizer = tokenizer('xx_sent_ud_sm')

    src_field, trg_field = create_field(vi_tokenizer, en_tokenizer)
    print("Loading vocabulary")
    src_vocab = torch.load(os.path.join(model_data_folder_en_to_vn , 'src_vocab.pth'))
    trg_vocab = torch.load(os.path.join(model_data_folder_en_to_vn , 'trg_vocab.pth'))
    src_field.vocab = src_vocab
    trg_field.vocab = trg_vocab

    print("Loading model")
    model = Transformer(
        len(src_field.vocab),
        len(trg_field.vocab),
        d_model = cfg['d_model'],
        n = cfg['n_layers'],
        heads = cfg['heads'],
        dropout = cfg['dropout']
    )

    model_ckpt = torch.load(model_ckp_en_to_vn, map_location=torch.device(device))
    model.load_state_dict(model_ckpt)
    model = model.to(device)    

    print("Successfully set up the model from en_to_vn")
    return model, src_field, trg_field, max_strlen, device, k
