import argparse
import ffmpeg
import os
import glob

def convert_mp3(input_file, output_file, codec='libmp3lame'):
    (
        ffmpeg
        .input(input_file)
        .output(output_file, acodec=codec)
        .run()
    )

def main():
    parser = argparse.ArgumentParser(description='Convert music files to MP3.')
    parser.add_argument('--codec', default='libmp3lame', help='Codec to use for conversion (default: libmp3lame)')
    args = parser.parse_args()

    music_extensions = ['*.mp3', '*.wav', '*.aac', '*.flac', '*.m4a', '*.ogg', '*.mpeg']
    file_paths = []
    for extension in music_extensions:
        file_paths.extend(glob.glob(extension))

    os.makedirs('converted', exist_ok=True)

    for path in file_paths:
        filename = os.path.splitext(os.path.basename(path))[0]
        convert_mp3(path, f'converted/{filename}.mp3', codec=args.codec)

if __name__ == "__main__":
    main()
