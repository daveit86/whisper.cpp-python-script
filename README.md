# Description
This script helps using the whisper-cublas-12.2.0-bin-x64 binary by ggerganov (https://github.com/ggerganov/whisper.cpp).
This release takes advantage of NVIDIA GPUs.

This script performs the following operations
- Convert the input audio file to a 16Khz Wav audio file into the temp folder
- Run the script on the converted audio file and create the transcript in the trascripts folder
- Delete the converted audio file inside the temp folder

It uses the ggml-large-v2.bin model by default, models can be downloaded from, you can change the model by editing the code
https://huggingface.co/ggerganov/whisper.cpp/tree/main

# Usage
Download the run.py script and place it inside the folder where the "main.exe" file is located

Usage: python run.py <input audio file> <language code> <output type>
<input audio file>: Path to the input audio file (e.g., /path/to/input/audio/file.mp3)
<language code>: language code (e.g., en, fr, es, de, it, ru, zh, etc...)
<output type>: Desired output type (e.g., txt, vtt, srt, lrc, wts, j, jf, csv)
