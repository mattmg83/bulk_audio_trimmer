from pydub import AudioSegment
import os

def trim_audio(input_folder, output_folder, seconds_to_trim_beginning, seconds_to_trim_end):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith((".mp3", ".wav", ".ogg", ".flac")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Load the audio file
            audio = AudioSegment.from_file(input_path)

            # Calculate the duration of the audio file
            duration = len(audio) / 1000  # in seconds

            # Calculate the start and end positions for trimming
            start_trim = seconds_to_trim_beginning * 1000
            end_trim = seconds_to_trim_end * 1000

            # Trim the audio
            trimmed_audio = audio[start_trim:-end_trim]

            # Export the trimmed audio to the output folder
            trimmed_audio.export(output_path, format=filename.split(".")[-1])

            print(f"Trimmed '{filename}' and saved to '{output_path}'")

if __name__ == "__main__":
    input_folder = "path/to/input/folder"
    output_folder = "path/to/output/folder"
    seconds_to_trim_beginning = 5  # Adjust as needed
    seconds_to_trim_end = 3  # Adjust as needed

    trim_audio(input_folder, output_folder, seconds_to_trim_beginning, seconds_to_trim_end)
