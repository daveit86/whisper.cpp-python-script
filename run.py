import subprocess
import os
from pathlib import Path

def convert_audio(input_file):
    output_file = Path(input_file).with_suffix(".wav")
    output_temp_folder = "temp"
    
    if not Path(output_temp_folder).exists():
        os.makedirs(output_temp_folder)
        
    output_temp_file = os.path.join(output_temp_folder, output_file.name)
    
    command = f"ffmpeg -i {input_file} -ar 16000 -ac 2 -strict -2 -c:a pcm_s16le -f wav {output_temp_file}"
    subprocess.run(command, shell=True)
    return output_temp_file
    
def run_external_tool(input_wav_file, language, output_type):
    exe_path = "main.exe"
    model_path = "models\\\\ggml-large-v2.bin"
    output_folder = "transcripts"

    if not Path(output_folder).exists():
        os.makedirs(output_folder)
    
    command = f"{exe_path} -f {input_wav_file} -l {language} -m {model_path} -o{output_type} -of {output_folder}"
    subprocess.run(command, shell=True)

def remove_temp_files(output_temp_file):
    command = f"del /f /q {output_temp_file}"
    subprocess.run(command, shell=True)

def print_usage():
    print("Usage: python run.py <input audio file> <language code> <output type>")
    print("<input audio file>: Path to the input audio file (e.g., /path/to/input/audio/file.mp3)")
    print("<language code>: language code (e.g., en, fr, es, de, it, ru, zh, etc...)")
    print("<output type>: Desired output type (e.g., txt, vtt, srt, lrc, wts, j, jf, csv)")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 4:
        print_usage()
        sys.exit(1)
    
    input_file = sys.argv[1]
    language = sys.argv[2].lower()
    output_type = sys.argv[3]
    
    output_temp_file=convert_audio(input_file)
    run_external_tool(output_temp_file, language, output_type)
    remove_temp_files(output_temp_file)
