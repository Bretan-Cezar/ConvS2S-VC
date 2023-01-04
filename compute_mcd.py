import argparse
import os
import soundfile as sf
import pyworld as WORLD
import matplotlib.pyplot as plt
import numpy as np
from pysptk.conversion import sp2mc
from sprocket.util import melcd, estimate_twf

def main():

    parser = argparse.ArgumentParser(description='Compute MCD')
    
    parser.add_argument('-tdir', '--target_directory', type=str, default='./data/ARCTIC/test',
                        help='root data folder that contains the wav files of target speech')
    parser.add_argument('-cdir', '--converted_directory', type=str, default='./out/cmu_arctic',
                        help='root data folder that contains wav files of the converted speech.')
    parser.add_argument('-att', '--attention_type', type=str, default='raw')
    parser.add_argument('-exp', '--experiment_name', type=str, help='experiment name')
    parser.add_argument('-p', '--pair', type=str, help="pair of speakers")
    parser.add_argument('-sr', '--sample_rate', type=int, default=16000)

    args = parser.parse_args()

    sr = args.sample_rate

    conv_dir = os.path.join(args.converted_directory, args.experiment_name, args.attention_type, 'vocoder')
    pair_dir = os.path.join(conv_dir, args.pair)

    source_spk = args.pair.split('2')[0]
    target_spk = args.pair.split('2')[1]

    target_dir = os.path.join(args.target_directory, target_spk)
    
    mcds = []

    for n, trg_wav_filename in enumerate(os.listdir(target_dir)):
        
        trg_wav_path = os.path.join(target_dir, trg_wav_filename)
        conv_wav_path = os.path.join(pair_dir, trg_wav_filename)
        
        trg_wav = sf.read(trg_wav_path)[0]
        conv_wav = sf.read(conv_wav_path)[0]

        _, trg_spc, _ = WORLD.wav2world(trg_wav, sr)
        _, conv_spc, _ = WORLD.wav2world(conv_wav, sr)

        trg_mceps = sp2mc(trg_spc, 24, 0.42)
        conv_mceps = sp2mc(conv_spc, 24, 0.42)

        twf = estimate_twf(trg_mceps, conv_mceps)

        trg_mceps = trg_mceps[twf[0]]
        conv_mceps = conv_mceps[twf[1]]

        mcd = melcd(trg_mceps, conv_mceps)

        mcds.append(np.mean(mcd))

    print(f'Average MCD of {args.pair} conversion: {np.mean(mcds)}')


if __name__ == '__main__':
    main()      