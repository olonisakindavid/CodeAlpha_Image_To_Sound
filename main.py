# OFFLINE
# from PIL import Image
# import pytesseract
# import pyttsx3

# # Load the screenshot image
# screenshot = Image.open('screenshot.png')

# # Perform OCR on the image
# text = pytesseract.image_to_string(screenshot)

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Set properties (optional)
# engine.setProperty('rate', 150)  # Speed of speech (words per minute)
# engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# # Convert the recognized text to speech and play it
# engine.say(text)
# engine.runAndWait()

# ONLINE
from gtts import gTTS
from PIL import Image
import pytesseract

try:
    # Load the screenshot image
    screenshot = Image.open('screenshot.png')

    # Perform OCR on the image
    text = pytesseract.image_to_string(screenshot)

    # Create a gTTS object with the extracted text
    tts = gTTS(text)

    # Save the generated speech to an audio file
    tts.save('output_audio.mp3')
    print("Image-To-Sound conversion successful.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
