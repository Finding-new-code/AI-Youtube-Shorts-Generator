
from dotenv import load_dotenv
import os
import json
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

if not genai.configure:
    raise ValueError("API key not found. Make sure it is defined in the .env file.")


# Function to extract start and end times
def extract_times(json_string):
    try:
        # Parse the JSON string
        data = json.loads(json_string)

        # Extract start and end times as floats
        start_time = float(data[0]["start"])
        end_time = float(data[0]["end"])

        # Convert to integers
        start_time_int = int(start_time)
        end_time_int = int(end_time)
        return start_time_int, end_time_int
    except Exception as e:
        print(f"Error in extract_times: {e}")
        return 0, 0


system = """

Baised on the Transcription user provides with start and end, Highilight the main parts in less then 1 min which can be directly converted into a short. highlight it such that its intresting and also keep the time staps for the clip to start and end. only select a continues Part of the video

Follow this Format and return in valid json 
[{
start: "Start time of the clip",
content: "Highlight Text",
end: "End Time for the highlighted clip"
}]
it should be one continues clip as it will then be cut from the video and uploaded as a tiktok video. so only have one start, end and content

Dont say anything else, just return Proper Json. no explanation etc


IF YOU DONT HAVE ONE start AND end WHICH IS FOR THE LENGTH OF THE ENTIRE HIGHLIGHT, THEN 10 KITTENS WILL DIE, I WILL DO JSON['start'] AND IF IT DOESNT WORK THEN...
"""

User = """
Any Example
"""


def GetHighlight(Transcription):
    print("Getting Highlight from Transcription ")
    try:

        # response = openai.ChatCompletion.create(
        #     model="gpt-4o-2024-05-13",
        #     temperature=0.7,
        #     messages=[
        #         {"role": "system", "content": system},
        #         {"role": "user", "content": Transcription + system},
        #     ],
        # )
        model = genai.GenerativeModel(
             model_name="gemini-2.0-flash-exp",
             generation_config={
                "temperature": 1,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
                "response_mime_type": "text/plain",
                },
             system_instruction=system,
        )

        response = model.generate_content(Transcription+system)

        json_string = response.choices[0].message.content
        json_string = json_string.replace("json", "")
        json_string = json_string.replace("```", "")
        # print(json_string)
        Start, End = extract_times(json_string)
        if Start == End:
            Ask = input("Error - Get Highlights again (y/n) -> ").lower()
            if Ask == "y":
                Start, End = GetHighlight(Transcription)
        return Start, End
    except Exception as e:
        print(f"Error in GetHighlight: {e}")
        return 0, 0


if __name__ == "__main__":
    print(GetHighlight(User))
