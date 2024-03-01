import subprocess
import os
from pathlib import Path

def convert_audio(input_file):
    output_file = Path(input_file).with_suffix(".wav")
    output_temp_folder = "temp"
    
    if not Path(output_temp_folder).exists():
        os.makedirs(output_temp_folder)
        
    output_temp_file = os.path.join(output_temp_folder, output_file.name)
    print(f"output:{output_file},input:{input_file}")
    command = f"ffmpeg -i \"{input_file}\" -ar 16000 -ac 2 -strict -2 -c:a pcm_s16le -f wav \"{output_temp_file}\""
    print(f"command:{command}")
    subprocess.run(command, shell=True)
    return output_temp_file
    
def run_external_tool(input_file, output_temp_file, language, output_type):
    input_file = Path(input_file)
    exe_path = "main.exe"
    model_path = "models\\\\ggml-large-v2.bin"
    output_folder = "transcripts"
    output_file = os.path.join(output_folder,input_file.name)

    if not Path(output_folder).exists():
        os.makedirs(output_folder)
    
    command = f"{exe_path} -f \"{output_temp_file}\" -l {language} -m {model_path} -o{output_type} -of \"{output_file}\""
    print(command)
    subprocess.run(command, shell=True)

def remove_temp_files(output_temp_file):
    command = f"del /f /q \"{output_temp_file}\""
    subprocess.run(command, shell=True)

def process_input(input_path, language, output_type):
    if os.path.isfile(input_path):
        output_temp_file = convert_audio(input_path)
        run_external_tool(input_path, output_temp_file, language, output_type)
        remove_temp_files(output_temp_file)
    elif os.path.isdir(input_path):
        for file_name in os.listdir(input_path):
            file_path = os.path.join(input_path, file_name)
            if os.path.isfile(file_path):
                output_temp_file = convert_audio(file_path)
                run_external_tool(file_path, output_temp_file, language, output_type)
                remove_temp_files(output_temp_file)
    else:
        print("Invalid input path.")

def print_usage():
    print("Usage: python run.py <input audio file/folder> <language code> <output type>")
    print("<input audio file/folder>: Path to the input audio file or folder containing audio files (e.g., /path/to/input/audio or /path/to/input/audio/file.mp3)")
    print("<language code>: language code (e.g., en, fr, es, de, it, ru, zh, etc...)")
    print("<output type>: Desired output type (e.g., txt, vtt, srt, lrc, wts, j, jf, csv)")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 4:
        print_usage()
        sys.exit(1)
    
    input_path = sys.argv[1]
    language = sys.argv[2].lower()
    output_type = sys.argv[3]
    
    process_input(input_path, language, output_type)
