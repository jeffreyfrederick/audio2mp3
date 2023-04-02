<h1>Audio File Converter</h1>
<p>This is a simple Python script that converts audio files to high-quality MP3 format. It processes all supported audio file types (WAV, OGG, M4A, FLAC, WMA, AAC) found in the current directory and its subdirectories.</p>

<h2>Installation</h2>

<ol>
    <li>Ensure you have Python 3.x installed.</li>
    <li>Install the required libraries using the following command:</li>
</ol>

<pre><code>pip install pydub tqdm</code></pre>

<h2>Usage</h2>

<ol>
    <li>Download or clone this repository.</li>
    <li>Place the <code>audio_converter.py</code> script in the directory containing the audio files you want to convert. The script will also search for and convert supported audio files in all subdirectories.</li>
    <li>Open a terminal and navigate to the directory containing the <code>audio_converter.py</code> script.</li>
    <li>Run the script using the following command:</li>
</ol>

<pre><code>python audio_converter.py</code></pre>

<p>The script will convert all supported audio files in the current directory and its subdirectories to high-quality 320kbps MP3 files. The converted files will be saved in the same location as the original files.</p>

<p>A progress bar will be displayed during the conversion process, indicating the number of files processed and the total number of files to be converted.</p>

<h2>License</h2>

<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
