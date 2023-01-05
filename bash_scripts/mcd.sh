trg_dir="./data/ARCTIC/test"
conv_dir="./out/cmu_arctic"
att_type="raw"
exp_name="resume_epoch50"
spk_pair="aew2bdl"
sr=16000

winpty py ./compute_mcd.py --target_directory ${trg_dir} \
            --converted_directory ${conv_dir} \
            --attention_type ${att_type} \
            --experiment_name ${exp_name} \
            --pair ${spk_pair} \
            --sample_rate ${sr}