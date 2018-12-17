import os, re
# from pymediainfo import MediaInfo

#from hachoir_core.cmd_line import unicodeFilename
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

from itertools import chain

script_dir = os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(script_dir):
    for file in files:
        if file.endswith((".mp4", ".mkv")) and not file.startswith('.'): # The arg can be a tuple of suffixes to look for
            print(os.path.join(root, file))
            print(file)
            filename, file_extension = os.path.splitext(file)
            print(filename)
            print(file_extension)
            print(re.sub('\s-\s\d{3,4}p|P$','',filename))
            # media_info = MediaInfo.parse(os.path.join(root, file))
            # for track in media_info.tracks:
            #   if track.track_type == 'Video':
            #     print(track.height)
            parser = createParser(os.path.join(root, file))
            metadata = extractMetadata(parser)
            for line in metadata.exportPlaintext():
                print(line)