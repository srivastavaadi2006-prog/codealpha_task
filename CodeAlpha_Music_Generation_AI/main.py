import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from music21 import stream, note, chord, midi

def generate_synthetic_midi_data():
    """Generates a structured classical-style note sequence to train on immediately."""
    # A simple repeating melodic/harmonic pattern to mimic training data structures
    base_melody = ['C4', 'E4', 'G4', 'C5', 'E5', 'G4', 'E4', 'C4', 
                   'D4', 'F4', 'A4', 'D5', 'F5', 'A4', 'F4', 'D4',
                   'G3', 'B3', 'D4', 'G4', 'B4', 'D4', 'B3', 'G3']
    return base_melody * 15  # Expand array size for model training patterns

def main():
    print("Initializing Data Preprocessing via music21 conventions...")
    raw_notes = generate_synthetic_midi_data()
    
    # Map out the unique pitches in our musical dataset
    pitches = sorted(list(set(raw_notes)))
    n_vocab = len(pitches)
    
    # Create structural mapping dictionaries converting notes to integers
    note_to_int = {note: num for num, note in enumerate(pitches)}
    int_to_note = {num: note for num, note in enumerate(pitches)}
    
    # Prepare training sequences
    sequence_length = 8
    network_input = []
    network_output = []
    
    for i in range(0, len(raw_notes) - sequence_length):
        seq_in = raw_notes[i:i + sequence_length]
        seq_out = raw_notes[i + sequence_length]
        network_input.append([note_to_int[char] for char in seq_in])
        network_output.append(note_to_int[seq_out])
        
    n_patterns = len(network_input)
    
    # Reshape input vectors to match LSTM dimensions [samples, time steps, features]
    X = np.reshape(network_input, (n_patterns, sequence_length, 1))
    X = X / float(n_vocab)  # Normalize feature inputs
    y = tf.keras.utils.to_categorical(network_output)

    # 3. Build Deep Learning Architecture (LSTM)
    print("Compiling Recurrent Neural Network (LSTM Architecture)...")
    model = Sequential([
        LSTM(128, input_shape=(X.shape[1], X.shape[2]), return_sequences=True),
        Dropout(0.2),
        LSTM(128),
        Dropout(0.2),
        Dense(n_vocab, activation='softmax')
    ])
    
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    
    # 4. Train the Model
    print("Training AI Model on note sequences...")
    model.fit(X, y, epochs=15, batch_size=32, verbose=1)
    
    # 5. Generate New Music Sequence using Seed Data
    print("Generating original musical sequences via inferred model patterns...")
    start_idx = np.random.randint(0, len(network_input) - 1)
    pattern = network_input[start_idx]
    prediction_output = []
    
    # Predict the next 24 sequential notes
    for note_index in range(24):
        prediction_input = np.reshape(pattern, (1, len(pattern), 1))
        prediction_input = prediction_input / float(n_vocab)
        
        prediction = model.predict(prediction_input, verbose=0)
        index = np.argmax(prediction)
        result = int_to_note[index]
        prediction_output.append(result)
        
        # Slide sequence window forward
        pattern.append(index)
        pattern = pattern[1:len(pattern)]

    # 6. Convert Generated Sequences to MIDI & Save
    print("Converting generated note arrays back to MIDI file format...")
    output_stream = stream.Stream()
    
    for pattern in prediction_output:
        # Check if the generated signature represents a chord or note string structure
        if ('.' in pattern) or pattern.isdigit():
            notes_in_chord = pattern.split('.')
            chord_notes = []
            for current_note in notes_in_chord:
                new_note = note.Note(int(current_note))
                # --- REMOVED THE FAULTY STOREDINSTRUMENT LINE FROM HERE ---
                chord_notes.append(new_note)
            new_chord = chord.Chord(chord_notes)
            output_stream.append(new_chord)
        else:
            new_note = note.Note(pattern)
            # --- REMOVED THE FAULTY STOREDINSTRUMENT LINE FROM HERE ---
            output_stream.append(new_note)
            
    midi_filename = "ai_generated_composition.mid"
    output_stream.write('midi', fp=midi_filename)
    print(f"Success! Output score successfully saved to current path as: '{midi_filename}'")
    

if __name__ == "__main__":
    main()