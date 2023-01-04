#!/bin/bash

# 
# Usage:
# ./run_train.sh [-g gpu] [-s stage] [-e exp_name]
# Options:
#     -g: GPU device# 
#     -s: Stage to start (0 or 1)
#     -e: Experiment name (e.g., "exp1")

# Default values
db_dir="./data/ARCTIC/train"
dataset_name="cmu_arctic"
gpu=0
start_stage=1
resume=10
exp_name="resume_epoch${resume}" 

while getopts "g:s:e:" opt; do
       case $opt in
              g ) gpu=$OPTARG;;
              s ) start_stage=$OPTARG;;
              e ) exp_name=$OPTARG;;
       esac
done

feat_dir="./dump/${dataset_name}/feat/train"
dconf_path="./dump/${dataset_name}/data_config.json"
stat_path="./dump/${dataset_name}/stat.pkl"
normfeat_dir="./dump/${dataset_name}/norm_feat/train"
model_dir="./model/${dataset_name}"
log_dir="./logs/${dataset_name}"


winpty py ./train.py -g ${gpu} \
              --data_rootdir ${normfeat_dir} \
              --model_rootdir ${model_dir} \
              --log_dir ${log_dir} \
              --experiment_name ${exp_name} \
              --resume ${resume} \
              --model_rootdir ${model_dir}
              ${cond}
