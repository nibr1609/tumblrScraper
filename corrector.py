import os
import openai

override = False
while True:
    override_yn = input("do you want to override existing files? [yn] \n")
    if override_yn == "y" or override_yn == "Y":
        override = True
        break
    if override_yn != "n" and override_yn != "N":
        print("Not a valid answer")
    else:
        break

todo = input("How should GPT correct your text? \n")

key_file = open('./key/openAIkey.txt', 'r')
key = key_file.readlines()[0]
openai.api_key = key

if not os.path.isdir("./data/"):
    os.makedirs("./data/")
if not os.path.isdir("./dataCorrected/"):
    os.makedirs("./dataCorrected/")
files = os.listdir("./data/")
for i, file in enumerate(files):
    print("Progress: Correcting " + str(i + 1) + "/" + str(len(files)))
    filename = os.fsdecode(file)
    corrected = ""
    if not override and os.path.exists("./dataCorrected/" + filename):
        continue
    with open("./data/" + filename) as f:
        lines = f.read()
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": todo + ": " + lines}])
        corrected = response.choices[0].message.content
    f = open("./dataCorrected/" + filename, "w")
    f.write(corrected)
    f.close()