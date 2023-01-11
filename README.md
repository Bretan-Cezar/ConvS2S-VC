# ConvS2S-VC

ConvS2S-VC is a parallel many-to-many voice conversion (VC) method using a fully convolutional sequence-to-sequence (ConvS2S) model. The current version performs VC by first modifying the mel-spectrogram of input speech in accordance with a target speaker or style index, and then generating a waveform using a speaker-independent neural vocoder (Parallel WaveGAN or HiFi-GAN) from the converted mel-spectrogram.

My additions to the original code are:

-   python code to compute Mel-cepstral Distortion between a series of target and converted speeches
-   changes to the model architecture and training loop as stated by the 2nd paper listed below to support any-to-many conversion

## Papers

-   [Hirokazu Kameoka](http://www.kecl.ntt.co.jp/people/kameoka.hirokazu/index-e.html), [Kou Tanaka](http://www.kecl.ntt.co.jp/people/tanaka.ko/index.html), [Takuhiro Kaneko](http://www.kecl.ntt.co.jp/people/kaneko.takuhiro/index.html), "**FastS2S-VC: Streaming Non-Autoregressive Sequence-to-Sequence Voice Conversion**," arXiv:2104.06900 [cs.SD], 2021. [**[Paper]**](https://arxiv.org/abs/2104.06900)

-   [Hirokazu Kameoka](http://www.kecl.ntt.co.jp/people/kameoka.hirokazu/index-e.html), [Kou Tanaka](http://www.kecl.ntt.co.jp/people/tanaka.ko/index.html), Damian Kwasny, [Takuhiro Kaneko](http://www.kecl.ntt.co.jp/people/kaneko.takuhiro/index.html), Nobukatsu Hojo, "**ConvS2S-VC: Fully Convolutional Sequence-to-Sequence Voice Conversion**," _IEEE/ACM Transactions on Audio, Speech, and Language Processing_, vol. 28, pp. 1849-1863, Jun. 2020. [**[Paper]**](https://ieeexplore.ieee.org/document/9113442)

## Original Author

Hirokazu Kameoka ([@kamepong](https://github.com/kamepong))

E-mail: kame.hirokazu@gmail.com
