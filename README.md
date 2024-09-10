# YoutubeDataConvert

## Overview

YoutubeDataConvert is a tool that allows you to convert data into videos and vice versa. This can be particularly useful for leveraging platforms like YouTube for free data storage, as YouTube allows you to upload as many videos as you want.

## Features

- Convert data files to series of images.
- Convert images back to data files with no data loss.
- Supports all file types and formats.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/YoutubeDataConvert.git
    cd YoutubeDataConvert
    ```

2. Install the required dependencies:
3. ```sh
    #TODO I'll need to recreate this project in a Virtual Environment then export the requirements.txt
    ```
   

4. Ensure you have `youtube-dl` and `ffmpeg` installed. You can install them using the following commands:
    ```sh
    pip install youtube-dl
    sudo apt-get install ffmpeg
    ```

## Usage

### Converting Data to Video

1. Navigate to the project directory:
    ```sh
    cd YoutubeDataConvert
    ```

2. Run the main script:
    ```sh
    python src/main.py
    ```

3. Follow the prompts to enter the file name and file type. The script will convert the data file into a series of images and then compile them into a video file.

### Converting Video to Data

1. Navigate to the project directory:
    ```sh
    cd YoutubeDataConvert
    ```

2. Run the main script:
    ```sh
    python src/main.py
    ```

3. Follow the prompts to enter the number of images and the output file type. The script will extract images from the video file and convert them back into the original data file.

## How It Works

### Data to Video

Currently, the script reads the data file and converts it into a series of images. In the future, I plan to compile them into a video file using `ffmpeg`. The video file can be uploaded to YouTube, leveraging YouTube's unlimited storage for free data storage. As of now, I have the code to implement it but Youtube's compression on videos is making it near impossible to conver the videos back into the original file.

### Video to Data

The script currently converts the series of images generated back into the original data file. This allows you to retrieve your data from the video file stored on YouTube. I also have the code in which you can convert a video into a series of images but due to Video Compression, I can't guarantee lossless data retrieval as of right now.

## Example

### Converting Data to Video

1. Place your data file in the `tests` directory.
2. Run the script and follow the prompts:
    ```sh
    python src/main.py
    ```
3. Enter `A` to convert data to video.
4. Enter the file name (e.g., `test1`) and file type (e.g., `txt`).
5. The script will generate a series of images in the `images` directory.

### Converting Video to Data

1. Run the script and follow the prompts:
    ```sh
    python src/main.py
    ```
2. Enter `B` to convert video to data.
3. Enter the number of photos and the output file type (e.g., `txt`).
4. The script will generate a data file in the `outputs` directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgements

- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [ffmpeg](https://ffmpeg.org/)
- [scikit-video](https://github.com/scikit-video/scikit-video)
