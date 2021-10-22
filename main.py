from PIL import Image 
from IPython.display import display 
import random
import json

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background_color = [
    "background-1", 
    "background-2", 
    "background-3", 
    "background-4", 
    "background-5", 
    "background-6", 
    "background-7",
    "background-8",
    "background-9",
    "background-10",
    "background-11",
    "background-12",
    "background-13",
    "background-14",
    "background-15",
    "background-16",
    "background-17",
    "background-18",
    "background-19",
    "background-20",
    "background-21",
    "background-22",
    "background-23",
    "background-24"
] 
background_color_weights = [4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 4.41, 1, 2]

skin_color = ["skin-1", "skin-2", "skin-3", "skin-4", "skin-5", "skin-6", "skin-7", "skin-8", "skin-9", "skin-10", "skin-11"] 
skin_color_weights = [31.25, 10.2, 7, 11.9, 10.2, 20.5, 6.8, 1, 0.75, 0.25, 0.15]

skin_condition = ["skin_condition", "transparent"] 
skin_condition_weights = [1, 99]

tattoo = ["tattoo-1", "tattoo-2", "tattoo-3", "tattoo-4", "tattoo-5", "tattoo-6", "tattoo-7", "tattoo-8", "tattoo-9", "tattoo-10", "tattoo-11", "tattoo-12", "tattoo-13", "tattoo-14", "transparent"] 
tattoo_weights = [0, 2.7, 2.25, 3.3, 2.25, 1.5, 2.55, 3.9, 0.6, 3.3, 2.25, 0.9, 2.25, 2.25, 70]

eye = ["sheep-eye"] 
eye_weights = [100]

hair = ["hair-1", "hair-2", "hair-3", "hair-4", "hair-5", "hair-6"] 
hair_weights = [14, 21, 16, 3, 14, 32]

nose = ["nose-1", "nose-2", "nose-3", "nose-4", "nose-5", "nose-6"] 
nose_weights = [25.25, 33, 15, 25, 0.5, 1.25]

body_hair = ["body_hair-1", "body_hair-2", "body_hair-3", "body_hair-4", "body_hair-5", "body_hair-6", "body_hair-7", "body_hair-8", "body_hair-9", "body_hair-10", "body_hair-11", "body_hair-12", "transparent"] 
body_hair_weights = [0, 0, 2.8, 2.8, 1.75, 1.05, 0, 3.5, 7, 2.1, 7, 7, 65]

mouth = ["mouth-1", "mouth-2", "mouth-3", "mouth-4", "mouth-5"] 
mouth_weights = [5, 20, 5, 25, 45]

necklace = ["necklace-1", "necklace-2", "transparent"] 
necklace_weights = [12.5, 12.5, 75]

eyebrows = ["eyebrows-1", "eyebrows-2", "eyebrows-3"] 
eyebrows_weights = [20, 35, 45]

clothes = ["clothes-1", "clothes-2", "clothes-3", "clothes-4", "clothes-5", "clothes-6", "clothes-7", "clothes-8", "clothes-9"] 
clothes_weights = [15, 27, 10, 18, 7, 7, 7, 2.5, 6.5]

earings = ["earings-1", "earings-2", "earings-3","earings-4","transparent"] 
earings_weights = [12.25, 4.2, 12.25, 6.3, 65]

accessory = ["accessory-1", "accessory-2", "accessory-3", "accessory-4","transparent"] 
accessory_weights = [12.25, 8.75, 7, 7, 65]

extra = ["extra-1", "extra-2", "transparent"] 
extra_weights = [12, 18, 70]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file name

background_color_files = {
    "background-1": "01_001",
    "background-2": "01_002",
    "background-3": "01_003",
    "background-4": "01_004",
    "background-5": "01_005",
    "background-6": "01_006",
    "background-7": "01_007",
    "background-8": "01_008",
    "background-9": "01_009",
    "background-10": "01_010",
    "background-11": "01_011",
    "background-12": "01_012",
    "background-13": "01_013",
    "background-14": "01_014",
    "background-15": "01_015",
    "background-16": "01_016",
    "background-17": "01_017",
    "background-18": "01_018",
    "background-19": "01_019",
    "background-20": "01_020",
    "background-21": "01_021",
    "background-22": "01_022",
    "background-23": "01_023",
    "background-24": "01_024",
}

skin_files = {
    "skin-1": "02_b02_01_001",
    "skin-2": "02_b02_01_002",
    "skin-3": "02_b02_01_003",
    "skin-4": "02_b02_01_004",
    "skin-5": "02_b02_01_005",
    "skin-6": "02_b02_01_006",
    "skin-7": "02_b02_01_007",
    "skin-8": "02_b02_01_008",
    "skin-9": "02_b02_01_009",
    "skin-10": "02_b02_01_010",
    "skin-11": "02_b02_01_011",
}

skin_condition_flies = {
    "skin_condition": "02_b02_02_001",
    "transparent": "transparent"
}

tattoo_files = {
    "tattoo-1": "02_b02_03_001",
    "tattoo-2": "02_b02_03_002",
    "tattoo-3": "02_b02_03_003",
    "tattoo-4": "02_b02_03_004",
    "tattoo-5": "02_b02_03_005",
    "tattoo-6": "02_b02_03_006",
    "tattoo-7": "02_b02_03_007",
    "tattoo-8": "02_b02_03_008",
    "tattoo-9": "02_b02_03_009",
    "tattoo-10": "02_b02_03_010",
    "tattoo-11": "02_b02_03_011",
    "tattoo-12": "02_b02_03_012",
    "tattoo-13": "02_b02_03_013",
    "tattoo-14": "02_b02_03_014",
    "transparent": "transparent"
}

eye_flies = {
    "sheep-eye": "02_b02_04_001"
}

hair_files = {
    "hair-1": "02_b02_05_001",
    "hair-2": "02_b02_05_002",
    "hair-3": "02_b02_05_003",
    "hair-4": "02_b02_05_004",
    "hair-5": "02_b02_05_005",
    "hair-6": "02_b02_05_006"
}

nose_files = {
    "nose-1": "02_b02_06_001",
    "nose-2": "02_b02_06_002",
    "nose-3": "02_b02_06_003",
    "nose-4": "02_b02_06_004",
    "nose-5": "02_b02_06_005",
    "nose-6": "02_b02_06_006"
}

body_hair_files = {
    "body_hair-1": "02_b02_07_001",
    "body_hair-2": "02_b02_07_002",
    "body_hair-3": "02_b02_07_003",
    "body_hair-4": "02_b02_07_004",
    "body_hair-5": "02_b02_07_005",
    "body_hair-6": "02_b02_07_006",
    "body_hair-7": "02_b02_07_007",
    "body_hair-8": "02_b02_07_008",
    "body_hair-9": "02_b02_07_009",
    "body_hair-10": "02_b02_07_010",
    "body_hair-11": "02_b02_07_011",
    "body_hair-12": "02_b02_07_012",
    "transparent": "transparent"
}

mouth_files = {
    "mouth-1": "02_b02_08_001",
    "mouth-2": "02_b02_08_002",
    "mouth-3": "02_b02_08_003",
    "mouth-4": "02_b02_08_004",
    "mouth-5": "02_b02_08_005"
}

necklace_files = {
    "necklace-1": "02_b02_09_001",
    "necklace-2": "02_b02_09_002",
    "transparent": "transparent"
}

eyebrows_files = {
    "eyebrows-1": "02_b02_10_001",
    "eyebrows-2": "02_b02_10_002",
    "eyebrows-3": "02_b02_10_003"
}

clothes_files = {
    "clothes-1": "02_b02_11_001",
    "clothes-2": "02_b02_11_002",
    "clothes-3": "02_b02_11_003",
    "clothes-4": "02_b02_11_004",
    "clothes-5": "02_b02_11_005",
    "clothes-6": "02_b02_11_006",
    "clothes-7": "02_b02_11_007",
    "clothes-8": "02_b02_11_008",
    "clothes-9": "02_b02_11_009"
}

earings_files = {
    "earings-1": "02_b02_13_001",
    "earings-2": "02_b02_13_002",
    "earings-3": "02_b02_13_003",
    "earings-4": "02_b02_13_004",
    "transparent": "transparent"
}

accessory_files = {
    "accessory-1": "02_b02_15_001",
    "accessory-2": "02_b02_15_002",
    "accessory-3": "02_b02_15_003",
    "accessory-4": "02_b02_15_004",
    "transparent": "transparent"
}

extra_files = {
    "extra-1": "02_b02_16_001",
    "extra-2": "02_b02_16_002",
    "transparent": "transparent"
}

## Generate Traits
TOTAL_IMAGES = 250 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Background-Color"] = random.choices(background_color, background_color_weights)[0]
    new_image ["Skin-Color"] = random.choices(skin_color, skin_color_weights)[0]
    new_image ["Skin-Condition"] = random.choices(skin_condition, skin_condition_weights)[0]
    new_image ["Tattoo"] = random.choices(tattoo, tattoo_weights)[0]
    new_image ["Eye"] = random.choices(eye, eye_weights)[0]
    new_image ["Hair"] = random.choices(hair, hair_weights)[0]
    new_image ["Nose"] = random.choices(nose, nose_weights)[0]
    new_image ["Body-Hair"] = random.choices(body_hair, body_hair_weights)[0]
    new_image ["Mouth"] = random.choices(mouth, mouth_weights)[0]  
    new_image ["Necklace"] = random.choices(necklace, necklace_weights)[0]
    new_image ["Eyebrows"] = random.choices(eyebrows, eyebrows_weights)[0]  
    new_image ["Clothes"] = random.choices(clothes, clothes_weights)[0]
    new_image ["Earings"] = random.choices(earings, earings_weights)[0]   
    new_image ["Accessory"] = random.choices(accessory, accessory_weights)[0]
    new_image ["Extra"] = random.choices(extra, extra_weights)[0]
    if (new_image ["Body-Hair"] == "body_hair-5"):
        return create_new_image()
    if (new_image ["Background-Color"] == "background-16") and (new_image ["Hair"] == "hair-2"):
        return create_new_image()
    else:
        if (new_image ["Skin-Color"] == "skin-8" or new_image ["Skin-Color"] == "skin-9" or new_image ["Skin-Color"] == "skin-10" or new_image ["Skin-Color"] == "skin-11") and (new_image ["Skin-Condition"] == "skin_condition" or new_image ["Nose"] == "nose-5" or new_image ["Nose"] == "nose-6"):
            return create_new_image()
        elif (new_image ["Skin-Condition"] == "skin_condition") and (new_image ["Nose"] == "nose-5"):
            return create_new_image()
        # elif (new_image ["Hair"] == "hair-1" or new_image ["Hair"] == "hair-2" or new_image ["Hair"] == "hair-3" or new_image ["Hair"] == "hair-4") and (new_image ["Accessory"] == "accessory-1" or new_image ["Accessory"] == "accessory-2" or new_image ["Accessory"] == "accessory-3" or new_image ["Accessory"] == "accessory-4"):
        #     return create_new_image()
        # elif (new_image ["Hair"] == "hair-5") and (new_image ["Accessory"] == "accessory-1" or new_image ["Accessory"] == "accessory-2"):
        #     return create_new_image()
        elif (new_image ["Nose"] == "nose-5") and (new_image ["Body-Hair"] == "body_hair-3" or new_image ["Body-Hair"] == "body_hair-4" or new_image ["Body-Hair"] == "body_hair-6" or new_image ["Body-Hair"] == "body_hair-9" or new_image ["Body-Hair"] == "body_hair-11" or new_image ["Mouth"] == "mouth-3" or new_image ["Mouth"] == "mouth-4" or new_image ["Mouth"] == "mouth-5"):
            return create_new_image()
        elif (new_image ["Nose"] == "nose-6") and (new_image ["Body-Hair"] == "body_hair-3" or new_image ["Body-Hair"] == "body_hair-4" or new_image ["Body-Hair"] == "body_hair-6" or new_image ["Body-Hair"] == "body_hair-9" or new_image ["Body-Hair"] == "body_hair-11"):
            return create_new_image()
        elif (new_image ["Necklace"] == "necklace-1" or new_image ["Necklace"] == "necklace-2") and (new_image ["Clothes"] == "clothes-1" or new_image ["Clothes"] == "clothes-3" or new_image ["Clothes"] == "clothes-5"):
            return create_new_image()
        else:
            if new_image in all_images:
                return create_new_image()
            else:
                return new_image
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)
	
# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

print(all_images)

# Get Trait Counts
background_color_count = {}
for item in background_color:
    background_color_count[item] = 0
    
skin_color_count = {}
for item in skin_color:
    skin_color_count[item] = 0

skin_condition_count = {}
for item in skin_condition:
    skin_condition_count[item] = 0

tattoo_count = {}
for item in tattoo:
    tattoo_count[item] = 0

eye_count = {}
for item in eye:
    eye_count[item] = 0

hair_count = {}
for item in hair:
    hair_count[item] = 0

nose_count = {}
for item in nose:
    nose_count[item] = 0 

body_hair_count = {}
for item in body_hair:
    body_hair_count[item] = 0
    
mouth_count = {}
for item in mouth:
    mouth_count[item] = 0

necklace_count = {}
for item in necklace:
    necklace_count[item] = 0

eyebrows_count = {}
for item in eyebrows:
    eyebrows_count[item] = 0

clothes_count = {}
for item in clothes:
    clothes_count[item] = 0

earings_count = {}
for item in earings:
    earings_count[item] = 0

accessory_count = {}
for item in accessory:
    accessory_count[item] = 0

extra_count = {}
for item in extra:
    extra_count[item] = 0

for image in all_images:
    background_color_count[image["Background-Color"]] += 1
    skin_color_count[image["Skin-Color"]] += 1
    skin_condition_count[image["Skin-Condition"]] += 1
    tattoo_count[image["Tattoo"]] += 1
    eye_count[image["Eye"]] += 1
    hair_count[image["Hair"]] += 1
    nose_count[image["Nose"]] += 1
    body_hair_count[image["Body-Hair"]] += 1
    mouth_count[image["Mouth"]] += 1
    necklace_count[image["Necklace"]] += 1    
    eyebrows_count[image["Eyebrows"]] += 1
    clothes_count[image["Clothes"]] += 1
    earings_count[image["Earings"]] += 1    
    accessory_count[image["Accessory"]] += 1
    extra_count[image["Extra"]] += 1
    
print(background_color_count)
print(skin_color_count)
print(skin_condition_count)
print(tattoo_count)
print(eye_count)
print(hair_count)
print(nose_count)
print(body_hair_count)
print(mouth_count)
print(necklace_count)
print(eyebrows_count)
print(clothes_count)
print(earings_count)
print(accessory_count)
print(extra_count)

#### Generate Metadata for all Traits 
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)

#### Generate Images    
for item in all_images:

    im1 = Image.open(f'./trait-layers/01_Backgrounds/{background_color_files[item["Background-Color"]]}.png').convert('RGBA')
    im2 = Image.open(f'./trait-layers/02_b02_01_Skin Color/{skin_files[item["Skin-Color"]]}.png').convert('RGBA')
    im3 = Image.open(f'./trait-layers/02_b02_02_Skin Condition/{skin_condition_flies[item["Skin-Condition"]]}.png').convert('RGBA')
    im4 = Image.open(f'./trait-layers/02_b02_03_Tattoo/{tattoo_files[item["Tattoo"]]}.png').convert('RGBA')
    im5 = Image.open(f'./trait-layers/02_b02_04_Eyes/{eye_flies[item["Eye"]]}.png').convert('RGBA')
    im6 = Image.open(f'./trait-layers/02_b02_05_Hair/{hair_files[item["Hair"]]}.png').convert('RGBA')
    im7 = Image.open(f'./trait-layers/02_b02_06_Nose/{nose_files[item["Nose"]]}.png').convert('RGBA')
    im8 = Image.open(f'./trait-layers/02_b02_07_Body Hair/{body_hair_files[item["Body-Hair"]]}.png').convert('RGBA')
    im9 = Image.open(f'./trait-layers/02_b02_08_Mouth/{mouth_files[item["Mouth"]]}.png').convert('RGBA')
    im10 = Image.open(f'./trait-layers/02_b02_09_Necklace/{necklace_files[item["Necklace"]]}.png').convert('RGBA')
    im11 = Image.open(f'./trait-layers/02_b02_10_Eyebrows/{eyebrows_files[item["Eyebrows"]]}.png').convert('RGBA')
    im12 = Image.open(f'./trait-layers/02_b02_11_Clothes/{clothes_files[item["Clothes"]]}.png').convert('RGBA')
    im13 = Image.open(f'./trait-layers/02_b02_13_Earings/{earings_files[item["Earings"]]}.png').convert('RGBA')    
    im14 = Image.open(f'./trait-layers/02_b02_15_Head Accessory/{accessory_files[item["Accessory"]]}.png').convert('RGBA')
    im15 = Image.open(f'./trait-layers/02_b02_16_Extra/{extra_files[item["Extra"]]}.png').convert('RGBA')

    #Create each composite
    if (item ["Hair"] == "hair-1" or item ["Hair"] == "hair-2" or item ["Hair"] == "hair-3" or item ["Hair"] == "hair-4") and (item ["Accessory"] == "accessory-1" or item ["Accessory"] == "accessory-2" or item ["Accessory"] == "accessory-3" or item ["Accessory"] == "accessory-4"):
        com1 = Image.alpha_composite(im1, im2)
        com2 = Image.alpha_composite(im3, im4)
        com3 = Image.alpha_composite(im5, im6)
        com4 = Image.alpha_composite(im7, im8)
        com5 = Image.alpha_composite(im9, im10)
        com6 = Image.alpha_composite(im11, im12)     
        com7 = Image.alpha_composite(im13, im15)

        com8 = Image.alpha_composite(com1, com2)
        com9 = Image.alpha_composite(com3, com4)
        com10 = Image.alpha_composite(com5, com6)
        # com11 = Image.alpha_composite(com7, im15)
        
        com12 = Image.alpha_composite(com8, com9)
        com13 = Image.alpha_composite(com10, com7)
        com14 = Image.alpha_composite(com12, com13)


        #Convert to RGB
        rgb_im = com14.convert('RGBA')

    elif (item ["Hair"] == "hair-5") and (item ["Accessory"] == "accessory-1" or item ["Accessory"] == "accessory-2"):
        com1 = Image.alpha_composite(im1, im2)
        com2 = Image.alpha_composite(im3, im4)
        com3 = Image.alpha_composite(im5, im6)
        com4 = Image.alpha_composite(im7, im8)
        com5 = Image.alpha_composite(im9, im10)
        com6 = Image.alpha_composite(im11, im12)     
        com7 = Image.alpha_composite(im13, im15)

        com8 = Image.alpha_composite(com1, com2)
        com9 = Image.alpha_composite(com3, com4)
        com10 = Image.alpha_composite(com5, com6)
        # com11 = Image.alpha_composite(com7, im15)
        
        com12 = Image.alpha_composite(com8, com9)
        com13 = Image.alpha_composite(com10, com7)
        com14 = Image.alpha_composite(com12, com13)


        #Convert to RGB
        rgb_im = com14.convert('RGBA')
        
    else:
        com1 = Image.alpha_composite(im1, im2)
        com2 = Image.alpha_composite(im3, im4)
        com3 = Image.alpha_composite(im5, im6)
        com4 = Image.alpha_composite(im7, im8)
        com5 = Image.alpha_composite(im9, im10)
        com6 = Image.alpha_composite(im11, im12)     
        com7 = Image.alpha_composite(im13, im14)

        com8 = Image.alpha_composite(com1, com2)
        com9 = Image.alpha_composite(com3, com4)
        com10 = Image.alpha_composite(com5, com6)
        com11 = Image.alpha_composite(com7, im15)
        
        com12 = Image.alpha_composite(com8, com9)
        com13 = Image.alpha_composite(com10, com11)
        com14 = Image.alpha_composite(com12, com13)


        #Convert to RGB
        rgb_im = com14.convert('RGBA')
        

    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)
	
#### Generate Metadata for each Image    
f = open('./metadata/all-traits.json',) 
data = json.load(f)

IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE"
PROJECT_NAME = "ADD_PROJECT_NAME_HERE"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Background-Color", i["Background-Color"]))
    token["attributes"].append(getAttribute("Skin-Color", i["Skin-Color"]))
    token["attributes"].append(getAttribute("Skin-Condition", i["Skin-Condition"]))
    token["attributes"].append(getAttribute("Tattoo", i["Tattoo"]))
    token["attributes"].append(getAttribute("Eye", i["Eye"]))
    token["attributes"].append(getAttribute("Hair", i["Hair"]))
    token["attributes"].append(getAttribute("Mouth", i["Tattoo"]))
    token["attributes"].append(getAttribute("Nose", i["Nose"]))
    token["attributes"].append(getAttribute("Body-Hair", i["Body-Hair"]))
    token["attributes"].append(getAttribute("Eyebrows", i["Eyebrows"]))
    token["attributes"].append(getAttribute("Clothes", i["Clothes"]))
    token["attributes"].append(getAttribute("Earings", i["Earings"]))
    token["attributes"].append(getAttribute("Necklace", i["Necklace"]))
    token["attributes"].append(getAttribute("Accessory", i["Accessory"]))
    token["attributes"].append(getAttribute("Extra", i["Extra"]))
    

    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()