from pydub import AudioSegment
from pydub.generators import Sine

def generate_note(freq, duration, amplitude=0.5):
    return Sine(freq).to_audio_segment(duration=duration).apply_gain(-amplitude)

# Define notes and their frequencies
notes = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25
}

# Create a list of note names to define two phrases
phrase1 = ['C4', 'D4', 'E4', 'C4', 'E4', 'F4', 'G4', 'F4', 'E4', 'C4']
phrase2 = ['E4', 'F4', 'G4', 'E4', 'G4', 'A4', 'B4', 'A4', 'G4', 'E4']

# Set the duration of a beat in milliseconds
beat_duration = 200

# Generate the melody by combining the notes of the phrases
tune = AudioSegment.silent(duration=0)
for note_name in phrase1 + phrase2:
    note_freq = notes[note_name]
    note = generate_note(note_freq, beat_duration, amplitude=-20)
    tune += note

# Repeat the tune to create a loop
tune_loop = tune * 4

# Export the loop as an mp3 file
tune_loop.export("background_music.mp3", format="mp3")
