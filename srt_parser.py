# SRT Parser

This script parses SRT subtitle files and outputs the result in a readable format.

## Functionality
- Reads an SRT file.
- Parses the content into a dictionary format.
- Outputs start time, end time, and text.

## Code

```python
import re

class SRTParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.cues = []

    def parse(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            # Split the content into individual cues
            cues = re.split(r'\n\n+', content.strip())
            for cue in cues:
                self._parse_cue(cue)

    def _parse_cue(self, cue):
        lines = cue.strip().split('\n')
        if len(lines) < 3:
            return  # Not a valid cue
        index = lines[0].strip()
        time_range = lines[1].strip()
        text = '\n'.join(lines[2:]).strip()
        start_time, end_time = self._parse_time_range(time_range)
        self.cues.append({'index': index, 'start': start_time, 'end': end_time, 'text': text})

    def _parse_time_range(self, time_range):
        start, end = time_range.split(' --> ')
        return start.strip(), end.strip()

    def get_cues(self):
        return self.cues

# Example usage:
# parser = SRTParser('path_to_file.srt')
# parser.parse()
# print(parser.get_cues())
```