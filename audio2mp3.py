import os
from pydub import AudioSegment
from tqdm import tqdm

def convert_to_mp3(file_path):
    file_name, ext = os.path.splitext(file_path)
    output_path = f"{file_name}.mp3"

    audio = AudioSegment.from_file(file_path, format=ext[1:])
    audio.export(output_path, format="mp3", bitrate="320k")

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith((".wav", ".ogg", ".m4a", ".flac", ".wma", ".aac")):
                file_path = os.path.join(root, file)
                convert_to_mp3(file_path)

if __name__ == "__main__":
    current_folder = os.getcwd()

    audio_files = []
    for root, _, files in os.walk(current_folder):
        for file in files:
            if file.lower().endswith((".wav", ".ogg", ".m4a", ".flac", ".wma", ".aac")):
                audio_files.append(os.path.join(root, file))

    print(f"found {len(audio_files)} audio files.")
    print("converting...")

    with tqdm(total=len(audio_files)) as pbar:
        for file_path in audio_files:
            convert_to_mp3(file_path)
            pbar.update(1)

    print("conversion completed.")