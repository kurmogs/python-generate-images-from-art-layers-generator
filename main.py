from PIL import Image 
from IPython.display import display 
import random
import json
import sys

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = [
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
    "background-24",
    "background-25",
    "background-26",
    "background-27",
    "background-28",
    "background-29",
    "background-30",
    "background-31",
    "background-32",
    "background-33"
] 
background_weights = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
                      2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 
                      0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 
                      0.4, 0.4, 0.2]

helm_backpieces = [
    "helm_backpieces-1",
    "helm_backpieces-2",
    "helm_backpieces-3",
    "helm_backpieces-4",
    "helm_backpieces-5",
] 

armor_back_pieces = [
    "armor_back_pieces-1",
    "armor_back_pieces-2",
    "armor_back_pieces-3",
    "armor_back_pieces-4",
    "armor_back_pieces-5",
    "armor_back_pieces-6",
    "armor_back_pieces-7",
    "armor_back_pieces-8",
    "armor_back_pieces-9",
    "armor_back_pieces-10",
    "armor_back_pieces-11",
    "armor_back_pieces-12",
    "armor_back_pieces-13",
    "armor_back_pieces-14",
    "armor_back_pieces-15",
    "armor_back_pieces-16",
    "armor_back_pieces-17",
    "armor_back_pieces-18",
    "armor_back_pieces-19",
    "armor_back_pieces-20",
    "armor_back_pieces-21",
    "armor_back_pieces-22",
    "armor_back_pieces-23",
    "armor_back_pieces-24",
    "armor_back_pieces-25",
    "armor_back_pieces-26",
    "armor_back_pieces-27",
    "armor_back_pieces-28",
    "armor_back_pieces-29",
    "armor_back_pieces-30",
    "armor_back_pieces-31",
    "armor_back_pieces-32",
    "armor_back_pieces-33",
    "armor_back_pieces-34",
    "armor_back_pieces-35",
    "armor_back_pieces-36",
    "armor_back_pieces-37",
    "armor_back_pieces-38",
    "armor_back_pieces-39",
    "armor_back_pieces-40",
    "armor_back_pieces-41", 
    "armor_back_pieces-42",
    "armor_back_pieces-43"
] 

base_body = [
    "base_body-1",
    "base_body-2",
    "base_body-3"
] 
base_body_weights = [33.3, 33.3, 33.4]

tattoos = [
    "tattoos-1",
    "tattoos-2",
    "tattoos-3",
    "tattoos-4",
    "tattoos-5",
    "tattoos-6",
    "tattoos-7",
    "tattoos-8",
    "tattoos-9",
    "tattoos-10"
] 
tattoos_weights = [0.1, 0.25, 0.1, 0.25, 0.1, 0.25, 0.2, 0.25, 0.5, 98]

battle_armors = [
    "battle_armors-1",
    "battle_armors-2",
    "battle_armors-3",
    "battle_armors-4",
    "battle_armors-5",
    "battle_armors-6",
    "battle_armors-7",
    "battle_armors-8",
    "battle_armors-9",
    "battle_armors-10",
    "battle_armors-11",
    "battle_armors-12",
    "battle_armors-13",
    "battle_armors-14",
    "battle_armors-15",
    "battle_armors-16",
    "helmetless_armors-1",
    "helmetless_armors-2",
    "helmetless_armors-3",
    "helmetless_armors-4",
    "helmetless_armors-5",
    "helmetless_armors-6",
    "helmetless_armors-7",
    "helmetless_armors-8",
    "helmetless_armors-9",
    "helmetless_armors-10",
    "helmetless_armors-11",
    "helmetless_armors-12",
    "helmetless_armors-13",
    "helmetless_armors-14",
    "helmetless_armors-15",
    "helmetless_armors-16",
    "helmetless_armors-17",
    "helmetless_armors-18",
    "helmetless_armors-19",
    "helmetless_armors-20",
    "enclosed_armors-1",
    "enclosed_armors-2",
    "enclosed_armors-3",
    "enclosed_armors-4",
    "enclosed_armors-5",
    "enclosed_armors-6",
    "enclosed_armors-7",
    "enclosed_armors-8",
    "enclosed_armors-9",
    "enclosed_armors-10",
    "enclosed_armors-11",
    "enclosed_armors-12",
    "enclosed_armors-13",
    "enclosed_armors-14",
    "enclosed_armors-15",
    "enclosed_armors-16",
    "enclosed_armors-17",
    "enclosed_armors-18",
    "enclosed_armors-19",
    "enclosed_armors-20",
    "no_battle_armors"
] 

battle_armors_weights = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2,
                        2, 2, 2, 2, 2, 2, 2.25, 2.25, 2.25, 2.25,
                        2.25, 2.25, 2.25, 2.25, 2.25, 2.25, 1.75, 1.75, 1.75, 1.75,
                        1.75, 1.75, 1.75, 1.75, 1.75, 1.75, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, 1, 15 ]

scars = [
    "scars-1",
    "scars-2",
    "scars-3",
    "scars-4"
] 
scars_weights = [40, 20, 20, 20]

facial_expressions = [
    "facial_expressions-1",
    "facial_expressions-2",
    "facial_expressions-3",
    "facial_expressions-4",
    "facial_expressions-5",
    "facial_expressions-6",
    "facial_expressions-7",
    "facial_expressions-8",
    "facial_expressions-9",
    "facial_expressions-10",
    "facial_expressions-11",
    "facial_expressions-12",
    "facial_expressions-13",
    "facial_expressions-14",
    "facial_expressions-15",
    "facial_expressions-16",
    "facial_expressions-17",
    "facial_expressions-18",
    "facial_expressions-19",
    "facial_expressions-20",
    "facial_expressions-21",
    "facial_expressions-22",
    "facial_expressions-23",
    "facial_expressions-24",
    "facial_expressions-25",
    "facial_expressions-26",
    "facial_expressions-27",
    "facial_expressions-28",
    "facial_expressions-29",
    "facial_expressions-30",
    "facial_expressions-31",
    "facial_expressions-32",
    "facial_expressions-33",
    "facial_expressions-34",
    "facial_expressions-35",
    "facial_expressions-36",
    "facial_expressions-37",
    "facial_expressions-38",
    "facial_expressions-39",
    "facial_expressions-40",
    "facial_expressions-41",
    "facial_expressions-42",
    "facial_expressions-43",
    "facial_expressions-44",
    "facial_expressions-45",
    "facial_expressions-46",
    "facial_expressions-47",
    "facial_expressions-48",
    "facial_expressions-49",
    "facial_expressions-50",
    "facial_expressions-51",
    "facial_expressions-52",
    "facial_expressions-53",
    "facial_expressions-54",
    "facial_expressions-55",
    "facial_expressions-56",
    "facial_expressions-57",
    "facial_expressions-58",
    "facial_expressions-59",
    "facial_expressions-60",
    "facial_expressions-61",
    "facial_expressions-62",
    "facial_expressions-63",
    "facial_expressions-64",
    "facial_expressions-65",
    "facial_expressions-66",
    "facial_expressions-67",
    "facial_expressions-68",
    "facial_expressions-69",
    "facial_expressions-70",
    "facial_expressions-71",
    "facial_expressions-72",
    "facial_expressions-73",
    "facial_expressions-74",
    "facial_expressions-75",
    "facial_expressions-76",
    "facial_expressions-77",
    "facial_expressions-78",
    "facial_expressions-79",
    "facial_expressions-80",
    "facial_expressions-81",
    "facial_expressions-82",
    "facial_expressions-83",
    "facial_expressions-84",
    "facial_expressions-85",
    "facial_expressions-86",
    "facial_expressions-87"
] 

war_paint = [ 
    "war_paint-1",
    "war_paint-2",
    "war_paint-3",
    "war_paint-4",
    "war_paint-5",
    "war_paint-6",
    "war_paint-7",
    "war_paint-8",
    "war_paint-9",
    "war_paint-10",
    "war_paint-11",
    "war_paint-12",
    "war_paint-13",
    "war_paint-14",
    "war_paint-15",
    "war_paint-16",
    "war_paint-17",
    "war_paint-18",
    "war_paint-19",
    "war_paint-20",
    "war_paint-21",
    "war_paint-22",
    "war_paint-23",
    "war_paint-24",
    "war_paint-25",
    "war_paint-26",
    "war_paint-27",
    "war_paint-28",
    "war_paint-29",
    "war_paint-30",
    "war_paint-31",
    "war_paint-32",
    "war_paint-33",
    "war_paint-34",
    "war_paint-35",
    "war_paint-36",
    "war_paint-37",
    "war_paint-38",
    "war_paint-39",
    "war_paint-40",
    "war_paint-41",
    "war_paint-42",
    "war_paint-43",
    "war_paint-44",
    "war_paint-45",
    "war_paint-46",
    "war_paint-47",
    "war_paint-48",
    "war_paint-49",
    "war_paint-50",
    "war_paint-51",
    "war_paint-52",
    "war_paint-53",
    "war_paint-54",
    "war_paint-55",
    "war_paint-56",
    "war_paint-57",
    "war_paint-58",
    "war_paint-59",
    "war_paint-60",
    "war_paint-61",
    "war_paint-62",
    "war_paint-63",
    "war_paint-64",
    "war_paint-65",
    "war_paint-66",
    "war_paint-67",
    "war_paint-68",
    "war_paint-69",
    "war_paint-70",
    "war_paint-71",
    "war_paint-72",
    "war_paint-73",
    "war_paint-74",
    "war_paint-75",
    "war_paint-76",
    "war_paint-77",
    "war_paint-78",
    "war_paint-79",
    "war_paint-80",
    "war_paint-81",
    "war_paint-82",
    "war_paint-83",
    "war_paint-84",
    "war_paint-85",
    "war_paint-86",
    "war_paint-87",
    "war_paint-88",
    "war_paint-89",
    "war_paint-90",
    "war_paint-91",
    "war_paint-92",
    "war_paint-93",
    "war_paint-94",
    "war_paint-95",
    "war_paint-96",
    "war_paint-97",
    "war_paint-98",
    "war_paint-99",
    "war_paint-100",
    "war_paint-101",
    "war_paint-102",
    "war_paint-103",
    "war_paint-104",
    "war_paint-105",
    "war_paint-106",
    "war_paint-107",
    "war_paint-108",
    "war_paint-109",
    "war_paint-110",
    "war_paint-111",
    "war_paint-112",
    "war_paint-113",
    "war_paint-114",
    "war_paint-115",
    "war_paint-116",
    "war_paint-117",
    "war_paint-118",
    "war_paint-119",
    "war_paint-120",
    "war_paint-121",
    "war_paint-122",
    "war_paint-123",
    "war_paint-124",
    "war_paint-125",
    "war_paint-126",
    "war_paint-127",
    "war_paint-128",
    "war_paint-129",
    "war_paint-130",
    "war_paint-131",
    "war_paint-132",
    "war_paint-133",
    "war_paint-134",
    "war_paint-135",
    "war_paint-136",
    "war_paint-137",
    "war_paint-138",
    "war_paint-139",
    "war_paint-140",
    "war_paint-141"
] 
war_paint_weights = [1, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 0.14,
                    1, 2, 0.5, 0.07, 0.5, 0.5, 0.5, 0.5, 2, 0.5,
                    1, 2, 0.5, 0.07, 0.5, 0.5, 0.5, 0.5, 2, 0.5,
                    0.5, 0.5, 0.5, 0.07, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    1, 2, 0.5, 0.07, 0.5, 0.5, 0.5, 0.5, 2, 0.5,
                    1, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 0.14,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.14,
                    1, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 0.5,
                    0.5, 0.5, 0.5, 0.07, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    1, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 0.5,
                    1, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 0.14,
                    1, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 0.14,
                    0.5, 0.5, 0.5, 0.07, 0.5, 0.5, 0.5, 0.5, 0.5, 0.14,
                    1, 2, 0.5, 0.08, 0.5, 0.5, 0.5, 0.5, 2, 0.16,
                    0.5]

eyebrows = [
    "eyebrows-1",
    "eyebrows-2",
    "eyebrows-3",
    "eyebrows-4",
    "eyebrows-5",
    "eyebrows-6",
    "eyebrows-7",
    "eyebrows-8",
    "eyebrows-9",
    "eyebrows-10",
    "eyebrows-11",
    "eyebrows-12",
    "eyebrows-13",
    "eyebrows-14",
    "eyebrows-15",
    "eyebrows-16",
    "eyebrows-17",
    "eyebrows-18",
    "eyebrows-19",
    "eyebrows-20",
    "eyebrows-21",
    "eyebrows-22",
    "eyebrows-23",
    "eyebrows-24",
    "eyebrows-25",
    "eyebrows-26",
    "eyebrows-27",
    "eyebrows-28",
    "eyebrows-29",
    "eyebrows-30",
    "eyebrows-31",
    "eyebrows-32",
    "eyebrows-33",
    "eyebrows-34",
    "eyebrows-35",
    "eyebrows-36",
    "eyebrows-37",
    "eyebrows-38",
    "eyebrows-39",
    "eyebrows-40",
    "eyebrows-41",
    "eyebrows-42",
    "eyebrows-43",
    "eyebrows-44",
    "eyebrows-45"
] 

hair = [
    "hair-1",
    "hair-2",
    "hair-3",
    "hair-4",
    "hair-5",
    "hair-6",
    "hair-7",
    "hair-8",
    "hair-9",
    "hair-10",
    "hair-11",
    "hair-12",
    "hair-13",
    "hair-14",
    "hair-15",
    "hair-16",
    "hair-17",
    "hair-18",
    "hair-19",
    "hair-20",
    "hair-21",
    "hair-22",
    "hair-23",
    "hair-24",
    "hair-25",
    "hair-26",
    "hair-27",
    "hair-28",
    "hair-29",
    "hair-30",
    "hair-31",
    "hair-32",
    "hair-33",
    "hair-34",
    "hair-35",
    "hair-36",
    "hair-37",
    "hair-38",
    "hair-39",
    "hair-40",
    "hair-41",
    "hair-42",
    "hair-43",
    "hair-44",
    "hair-45",
    "hair-46",
    "hair-47",
    "hair-48",
    "hair-49",
    "hair-50",
    "hair-51",
    "hair-52",
    "hair-53",
    "hair-54",
    "hair-55",
    "hair-56",
    "hair-57",
    "hair-58",
    "hair-59",
    "hair-60",
    "hair-61",
    "hair-62",
    "hair-63",
    "hair-64",
    "hair-65",
    "hair-66",
    "hair-67",
    "hair-68",
    "hair-69",
    "hair-70",
    "hair-71",
    "hair-72"
] 
hair_weights = [1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.2,
                0.56, 0.56, 0.56, 0.56, 0.56, 0.56, 0.56, 0.56, 0.52,
                1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.8, 1.8, 1.8,
                2.2, 2.2, 2.2, 2.2, 2.2, 2.2,  2.2, 2.3, 2.3,
                1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.8, 1.8, 1.8,
                1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.2,
                0.56, 0.56, 0.56, 0.56, 0.56,  0.56, 0.56, 0.56, 0.52,
                1.6, 1.6, 1.6, 1.6, 1.6, 1.6,  1.8, 1.8, 1.8, 
                5]

beards = [ 
    "beards-1",
    "beards-2",
    "beards-3",
    "beards-4",
    "beards-5",
    "beards-6",
    "beards-7",
    "beards-8",
    "beards-9",
    "beards-10",
    "beards-11",
    "beards-12",
    "beards-13",
    "beards-14",
    "beards-15",
    "beards-16",
    "beards-17",
    "beards-18",
    "beards-19",
    "beards-20",
    "beards-21",
    "beards-22",
    "beards-23",
    "beards-24",
    "beards-25",
    "beards-26",
    "beards-27",
    "beards-28",
    "beards-29",
    "beards-30",
    "beards-31",
    "beards-32",
    "beards-33",
    "beards-34",
    "beards-35",
    "beards-36",
    "beards-37",
    "beards-38",
    "beards-39",
    "beards-40",
    "beards-41",
    "beards-42",
    "beards-43",
    "beards-44",
    "beards-45",
    "beards-46",
    "beards-47",
    "beards-48",
    "beards-49",
    "beards-50",
    "beards-51",
    "beards-52",
    "beards-53",
    "beards-54",
    "beards-55",
    "beards-56",
    "beards-57",
    "beards-58",
    "beards-59",
    "beards-60",
    "beards-61",
    "beards-62",
    "beards-63",
    "beards-64",
    "beards-65",
    "beards-66",
    "beards-67",
    "beards-68",
    "beards-69",
    "beards-70",
    "beards-71",
    "beards-72"
]
beards_weights = [2.2, 2.2, 2.2, 2.2, 2.2, 2.2,  2.2, 2.3, 2.3,
            1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.2,
            1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.8, 1.8, 1.8,
            1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.8, 1.8, 1.8,
            0.56, 0.56, 0.56, 0.56, 0.56, 0.56, 0.56, 0.56, 0.52,
            1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.2,
            0.56, 0.56, 0.56, 0.56, 0.56, 0.56, 0.56, 0.56, 0.52,
            2.2, 2.2, 2.2, 2.2, 2.2, 2.2,  2.2, 2.3, 2.3
]   

mage_hoods = [
    "mage_hoods-1",
    "mage_hoods-2",
    "mage_hoods-3",
    "mage_hoods-4",
    "mage_hoods-5",
    "mage_hoods-6",
    "mage_hoods-7"
] 
mage_hoods_weights = [0.8, 0.8, 0.8, 0.8, 0.9, 0.9, 95]

arms = [
    "arms-1",
    "arms-2",
    "arms-3",
    "mage-1",
    "mage-2",
    "mage-3",
    "arms-7",
    "arms-8",
    "arms-9",
    "arms-10",
    "arms-11",
    "arms-12",
    "arms-13",
    "arms-14",
    "arms-15"
]
arms_weights = [7, 7, 7, 7, 7, 2, 7, 7, 7, 7, 7, 7, 7, 7, 7]

weapon = [
    "weapon_one_hand-1",
    "weapon_one_hand-2",
    "weapon_one_hand-3",
    "weapon_one_hand-4",
    "weapon_one_hand-5",
    "weapon_one_hand-6",
    "weapon_one_hand-7",
    "weapon_one_hand-8",
    "weapon_one_hand-9",
    "weapon_one_hand-10",     
    "weapon_one_hand-back-11",
    "weapon_one_hand-back-12",
    "weapon_one_hand-back-13",
    "weapon_one_hand-back-14",
    "weapon_one_hand-back-15",
    "weapon_one_hand-back-16",
    "weapon_one_hand-back-17",
    "weapon_one_hand-back-18",
    "weapon_one_hand-back-19",
    "weapon_one_hand-back-20",
    "weapon_one_hand-back-21",
    "weapon_one_hand-back-22",
    "weapon_one_hand-back-23",
    "weapon_one_hand-back-24",
    "weapon_dual_wield-1",
    "weapon_dual_wield-2",
    "weapon_dual_wield-3",
    "weapon_dual_wield-4",
    "weapon_dual_wield-5",
    "weapon_dual_wield-6",
    "weapon_dual_wield-7",
    "weapon_dual_wield-8",
    "weapon_dual_wield-9",
    "weapon_dual_wield-10",
    "weapon_double_grip-1",
    "weapon_double_grip-2",
    "weapon_double_grip-3",
    "weapon_double_grip-4",
    "weapon_double_grip-5",
    "weapon_double_grip-6",
    "weapon_double_grip-7",
    "weapon_double_grip-8",
    "weapon_double_grip-9",
    "weapon_double_grip-10",
    "weapon_double_grip-11",
    "weapon_double_grip-12",
    "weapon_double_grip-13",
    "weapon_double_grip-14",
    "weapon_double_grip-15",
    "weapon_double_grip-16",
    "weapon_double_grip-17",
    "weapon_double_grip-18",
    "weapon_double_grip-19",
    "weapon_double_grip-20",
    "weapon_double_grip-21",
    "weapon_double_grip-22",
    "weapon_double_grip-23",
    "weapon_staff-1",
    "weapon_staff-2",
    "weapon_staff-3",
    "weapon_staff-4",
    "weapon_staff-5",
    "weapon_staff-6",
    "weapon_staff-7",
    "weapon_staff-8",
    "weapon_staff-9",
    "weapon_staff-10",
    "weapon_staff-11",
    "weapon_staff-12",
    "weapon_staff-13",
    "weapon_staff-14",
    "weapon_staff-15",
    "weapon_staff-16",
    "weapon_staff-17",
    "weapon_staff-18",
    "weapon_staff-19",
    "weapon_staff-20",
    "weapon_staff-21",
    "weapon_staff-22",
    "weapon_staff-23",
    "weapon_staff-24",
    "weapon_mage_effect-1",
    "weapon_mage_effect-2",
    "weapon_mage_effect-3",
    "weapon_mage_effect-4",
    "weapon_mage_effect-5",
    "weapon_back-1",
    "weapon_back-2",
    "weapon_back-3",
    "weapon_back-4",
    "weapon_back-5",
    "weapon_back-6",
    "weapon_back-7",
    "weapon_back-8",
    "weapon_back-9",
    "weapon_back-10",
    "weapon_back-11",
    "weapon_back-12",
    "no_weapon"
]
weapon_weights = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
                    1.5, 1.5, 1.5, 1.5, 1.5, 1, 1, 1, 1, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 1, 1,
                    0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                    1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 1, 1, 1, 1, 1, 3, 4, 0, 0,
                    0, 4, 4, 0, 0, 0, 0, 0, 15
]

arm_armor = [
    "arm_armor-1",
    "arm_armor-2",
    "arm_armor-3",
    "arm_armor-4",
    "arm_armor-5",
    "arm_armor-6",
    "arm_armor-7",
    "arm_armor-8",
    "arm_armor-9",
    "arm_armor-10",
    "mage_hand-21",
    "mage_hand-22",
    "mage_hand-23",
    "mage_hand-24",
    "mage_hand-25",
    "mage_hand-26",
    "mage_hand-27",
    "mage_hand-28",
    "mage_hand-29",
    "mage_hand-20",
    "arm_armor-21",
    "arm_armor-22",
    "arm_armor-23",
    "arm_armor-24",
    "arm_armor-25",
    "arm_armor-26",
    "arm_armor-27",
    "arm_armor-28",
    "arm_armor-29",
    "arm_armor-30",
    "arm_armor-31",
    "arm_armor-32",
    "arm_armor-33",
    "arm_armor-34",
    "arm_armor-35",
    "arm_armor-36",
    "arm_armor-37",
    "arm_armor-38",
    "arm_armor-39",
    "arm_armor-40",
    "arm_armor-41",
    "arm_armor-42",
    "arm_armor-43",
    "arm_armor-44",
    "arm_armor-45",
    "arm_armor-46",
    "arm_armor-47",
    "arm_armor-48",
    "arm_armor-49",
    "arm_armor-50",
    "arm_armor-51",
    "arm_armor-52",
    "arm_armor-53",
    "arm_armor-54",
    "arm_armor-55",
    "arm_armor-56",
    "arm_armor-57",
    "arm_armor-58",
    "arm_armor-59",
    "arm_armor-60",
    "mage_armor-1",
    "mage_armor-2",
    "mage_armor-3",
    "mage_armor-4",
    "mage_armor-5",
    "mage_armor-6",
    "mage_armor-7",
    "mage_armor-8",
    "mage_armor-9",
    "mage_armor-10",
    "arm_armor-71",
    "arm_armor-72",
    "arm_armor-73",
    "arm_armor-74",
    "arm_armor-75",
    "arm_armor-76",
    "arm_armor-77",
    "arm_armor-78",
    "arm_armor-79",
    "arm_armor-80",
    "arm_armor-81",
    "arm_armor-82",
    "arm_armor-83",
    "arm_armor-84",
    "arm_armor-85",
    "arm_armor-86",
    "arm_armor-87",
    "arm_armor-88",
    "arm_armor-89",
    "arm_armor-90",
    "arm_armor-91",
    "arm_armor-92",
    "arm_armor-93",
    "arm_armor-94",
    "arm_armor-95",
    "arm_armor-96",
    "arm_armor-97",
    "arm_armor-98",
    "arm_armor-99",
    "arm_armor-100",
    "mage_armor-11",
    "arm_armor-102",
    "arm_armor-103",
    "arm_armor-104",
    "arm_armor-105",
    "arm_armor-106",
    "arm_armor-107",
    "arm_armor-108",
    "arm_armor-109",
    "arm_armor-110",
    "arm_armor-111",
    "arm_armor-112",
    "arm_armor-113",
    "arm_armor-114",
    "arm_armor-115",
    "arm_armor-116",
    "arm_armor-117",
    "arm_armor-118",
    "arm_armor-119",
    "arm_armor-120",
    "arm_armor-121",
    "arm_armor-122",
    "arm_armor-123",
    "arm_armor-124",
    "arm_armor-125",
    "arm_armor-126",
    "arm_armor-127",
    "arm_armor-128",
    "arm_armor-129",
    "arm_armor-130",
    "arm_armor-131",
    "arm_armor-132",
    "arm_armor-133",
    "arm_armor-134",
    "arm_armor-135",
    "arm_armor-136",
    "arm_armor-137",
    "arm_armor-138",
    "arm_armor-139",
    "arm_armor-140",
    "arm_armor-141",
    "arm_armor-142",
    "arm_armor-143",
    "arm_armor-144",
    "arm_armor-145",
    "arm_armor-146",
    "arm_armor-147",
    "arm_armor-148",
    "arm_armor-149",
    "arm_armor-150",
    "arm_armor-151",
    "arm_armor-152",
    "arm_armor-153",
    "arm_armor-154",
    "arm_armor-155",
    "arm_armor-156",
    "arm_armor-157",
    "arm_armor-158",
    "arm_armor-159",
    "arm_armor-160",
    "arm_armor-161",
    "arm_armor-162",
    "arm_armor-163",
    "arm_armor-164",
    "arm_armor-165",
    "arm_armor-166",
    "arm_armor-167",
    "arm_armor-168",
    "arm_armor-169",
    "arm_armor-170"   
]
arm_armor_weights = [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
                    1.5, 1, 1.5, 1.5, 1.5, 1.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1]


extras = [
    "extras-1",
    "extras-2",
    "extras-3",
    "extras-4",
    "extras-5",
    "extras-6",
    "extras-7",
    "extras-8",
    "extras-9",
    "extras-10",
    "extras-11",
    "extras-12",
    "extras-13",
    "extras-14",
    "extras-15",
    "extras-16",
    "extras-17",
    "extras-18",
    "extras-19",
    "extras-20",
    "extras-21",
    "extras-22",
    "extras-23",
    "extras-24"
]
extras_weights = [2.5, 0.5, 1, 2.5, 0.5, 1, 1, 1, 1, 5,
                  0.5, 1,   5, 2.5,  45, 5, 5, 5, 5, 1.25,
                  1.25, 1.25, 1.25, 5

]


# Dictionary variable for each trait. 
# Eech trait corresponds to its file name

background_files = {
    "background-1": "Background gradient blood#2.5",
    "background-2": "Background gradient desert#2.5",
    "background-3": "background gradient flames#2.5",
    "background-4": "background gradient fog#2.5",
    "background-5": "background gradient moss#2.5",
    "background-6": "Background gradient night#2.5",
    "background-7": "Background gradient sea#2.5",
    "background-8": "background gradient sunrise#2.5",
    "background-9": "Background gradient twilight#2.5",
    "background-10": "background gradient valentine#2.5",
    "background-11": "Background plain black#7",
    "background-12": "Background plain blue#7",
    "background-13": "Background plain green #7",
    "background-14": "Background plain mint#7",
    "background-15": "Background plain orange#7",
    "background-16": "Background plain pink#7",
    "background-17": "Background plain purple#7",
    "background-18": "Background plain teal#7",
    "background-19": "Background plain#7(1)",
    "background-20": "Background plain#7",
    "background-21": "Background unique asteroids#0.5",
    "background-22": "Background unique black hole#0.5",
    "background-23": "Background unique Blossom#0.5",
    "background-24": "Background unique crash#0.5",
    "background-25": "Background unique flare orange#0.1",
    "background-26": "background unique glaexy violet#0.1",
    "background-27": "Background unique milky way#0.1",
    "background-28": "Background unique moon#0.5",
    "background-29": "Background unique nebula pink#0.1",
    "background-30": "Background unique neutron star#0.5",
    "background-31": "Background unique sun asteroids#0.5",
    "background-32": "background unique sun#0.5",
    "background-33": "Background unique teal flare#0.1"    
}

helm_backpieces_files = {
    "helm_backpieces-1": "Head back pilot helmet",
    "helm_backpieces-2": "Head hood back black",
    "helm_backpieces-3": "Head hood back gold",
    "helm_backpieces-4": "Head Hood back silver",
    "helm_backpieces-5": "No helm_back#75"
}

armor_back_pieces_files = {
    "armor_back_pieces-1": "Armor backpiece trooper agnel",
    "armor_back_pieces-2": "Armor backpiece trooper aqua #2",
    "armor_back_pieces-3": "Armor backpiece trooper black",
    "armor_back_pieces-4": "Armor backpiece trooper gold",
    "armor_back_pieces-5": "Armor backpiece trooper lava",
    "armor_back_pieces-6": "Armor backpiece trooper moss",
    "armor_back_pieces-7": "Armor backpiece trooper rainbow",
    "armor_back_pieces-8": "Armor backpiece trooper silver",
    "armor_back_pieces-9": "Armor backpiece trooper sun",
    "armor_back_pieces-10": "Armor backpieceTrooper bubblegum #2",
    "armor_back_pieces-11": "Armor bronze commander",
    "armor_back_pieces-12": "Armor commander silver",
    "armor_back_pieces-13": "Armor dragon gold and silver",
    "armor_back_pieces-14": "Armor Gold and silver brawler",
    "armor_back_pieces-15": "Armor gold commander",
    "armor_back_pieces-16": "Armor helmetless explorer black#3",
    "armor_back_pieces-17": "Armor helmetless explorer blue#3",
    "armor_back_pieces-18": "Armor helmetless explorer brown#3",
    "armor_back_pieces-19": "Armor helmetless explorer gold",
    "armor_back_pieces-20": "Armor helmetless explorer green#3",
    "armor_back_pieces-21": "Armor helmetless explorer grey#3",
    "armor_back_pieces-22": "Armor helmetless explorer pink#3",
    "armor_back_pieces-23": "Armor helmetless explorer purple#3",
    "armor_back_pieces-24": "Armor helmetless explorer red#3",
    "armor_back_pieces-25": "Armor helmetless explorer silver",
    "armor_back_pieces-26": "Armor helmetless explorer white#3",
    "armor_back_pieces-27": "Armor helmetless explorer yellow#3",
    "armor_back_pieces-28": "Armor helmetless observer black#3",
    "armor_back_pieces-29": "Armor helmetless observer blue#3",
    "armor_back_pieces-30": "Armor helmetless observer brown#3",
    "armor_back_pieces-31": "Armor helmetless observer gold",
    "armor_back_pieces-32": "Armor helmetless observer green#3",
    "armor_back_pieces-33": "Armor helmetless observer Grey#3",
    "armor_back_pieces-34": "Armor helmetless observer pink#3",
    "armor_back_pieces-35": "Armor helmetless observer purple#3",
    "armor_back_pieces-36": "Armor helmetless observer red#3",
    "armor_back_pieces-37": "Armor helmetless observer silver",
    "armor_back_pieces-38": "Armor helmetless observer white#3",
    "armor_back_pieces-39": "Armor helmetless observer yellow#3",
    "armor_back_pieces-40": "Backpiece explorer",
    "armor_back_pieces-41": "Backpiece observer",
    "armor_back_pieces-42": "Gold and silver protector",
    "armor_back_pieces-43": "Trooper bubblegum #2",
    
}

base_body_files = {
    "base_body-1": "Position none skin black #1",
    "base_body-2": "Position none skin tan #1",
    "base_body-3": "Position none skin white #1"
}

tattoos_files = {
    "tattoos-1": "Tattoo beast gold",
    "tattoos-2": "Tattoo beast silver",
    "tattoos-3": "Tattoo nordic gold",
    "tattoos-4": "Tattoo nordic silver",
    "tattoos-5": "Tattoo runic gold",
    "tattoos-6": "Tattoo runic silver",
    "tattoos-7": "Tattoo tribal gold",
    "tattoos-8": "Tattoo tribal silver",
    "tattoos-9": "Tattoo thunder struck",
    "tattoos-10": "no_tattoos"
}

battle_armors_files = {
    "battle_armors-1": "Armor brawler gold and silver",
    "battle_armors-2": "Armor commander bronze",
    "battle_armors-3": "Armor commander silver",
    "battle_armors-4": "Armor dragon gold and silver",
    "battle_armors-5": "Armor gold commander",
    "battle_armors-6": "Armor protector gold and silver",
    "battle_armors-7": "Armor trooper angel#2",
    "battle_armors-8": "Armor trooper aqua #2",
    "battle_armors-9": "Armor trooper black",
    "battle_armors-10": "Armor trooper gold",
    "battle_armors-11": "Armor trooper lava#2",
    "battle_armors-12": "Armor trooper moss#2",
    "battle_armors-13": "Armor trooper rainbow#2",
    "battle_armors-14": "Armor trooper sun#2",
    "battle_armors-15": "Trooper armor silver",
    "battle_armors-16": "Trooper bubblegum #2",
    "helmetless_armors-1":"Armor helmetless explorer black#3",
    "helmetless_armors-2":"Armor helmetless explorer blue#3",
    "helmetless_armors-3":"Armor helmetless explorer brown#3",
    "helmetless_armors-4":"Armor helmetless explorer gold",
    "helmetless_armors-5":"Armor helmetless explorer green#3",
    "helmetless_armors-6":"Armor helmetless explorer grey#3",
    "helmetless_armors-7":"Armor helmetless explorer pink#3",
    "helmetless_armors-8":"Armor helmetless explorer purple#3",
    "helmetless_armors-9":"Armor helmetless explorer red#3",
    "helmetless_armors-10":"Armor helmetless explorer silver",
    "helmetless_armors-11":"Armor helmetless observer black",
    "helmetless_armors-12":"Armor helmetless observer blue",
    "helmetless_armors-13":"Armor helmetless observer brown",
    "helmetless_armors-14":"Armor helmetless observer gold",
    "helmetless_armors-15":"Armor helmetless observer green",
    "helmetless_armors-16": "Armor helmetless observer grey",
    "helmetless_armors-17": "Armor helmetless observer pink",
    "helmetless_armors-18": "Armor helmetless observer purple",
    "helmetless_armors-19": "Armor helmetless observer red",
    "helmetless_armors-20": "Armor helmetless observer silver",
    "enclosed_armors-1": "Armor observer black",
    "enclosed_armors-2": "Armor observer blue",
    "enclosed_armors-3": "Armor observer brown",
    "enclosed_armors-4": "Armor observer gold",
    "enclosed_armors-5": "Armor observer green",
    "enclosed_armors-6": "Armor observer grey",
    "enclosed_armors-7": "Armor observer pink",
    "enclosed_armors-8": "Armor observer purple",
    "enclosed_armors-9": "Armor observer red",
    "enclosed_armors-10": "Armor observer silver",
    "enclosed_armors-11": "Explorer suit black#1",
    "enclosed_armors-12": "Explorer suit blue#1",
    "enclosed_armors-13": "Suit explorer brown#1",
    "enclosed_armors-14": "Armor explorer gold",
    "enclosed_armors-15": "Explorer suit green#1",
    "enclosed_armors-16": "Explorer suit#1",
    "enclosed_armors-17": "Explorer suit pink#1",
    "enclosed_armors-18": "Explorer suit purple#1",
    "enclosed_armors-19": "Explorer suit red#1",
    "enclosed_armors-20": "Armor explorer silver",
    "no_battle_armors": "no_battle_armors"
}

scars_files = {
    "scars-1": "None #40",
    "scars-2": "Scar across #20",
    "scars-3": "Scar bleeding #20",
    "scars-4": "Scar claw"
}

facial_expressions_files = {
    "facial_expressions-1": "Face bored eye blue skin black#1",
    "facial_expressions-2": "Face bored eye blue skin tan#1",
    "facial_expressions-3": "Face bored eye blue skin white#1",
    "facial_expressions-4": "Face bored eye green skin black#1",
    "facial_expressions-5": "Face bored eye green skin tan#1",
    "facial_expressions-6": "Face bored eye green skin white#1",
    "facial_expressions-7": "Face bored eye purple skin black#1",
    "facial_expressions-8": "Face bored eye purple skin tan#1",
    "facial_expressions-9": "Face bored eye purple skin white#1",  
    "facial_expressions-10": "Face disdain eye green skin black#1", 
    "facial_expressions-11": "Face disdain eye green skin tan#1",
    "facial_expressions-12": "Face disdain eye green skin white#1",   
    "facial_expressions-13": "Face disdain eye purple skin black#1",   
    "facial_expressions-14": "Face disdain eye purple skin tan#1",   
    "facial_expressions-15": "Face disdain eye purple skin white#1",    
    "facial_expressions-16": "Face evil eye blue skin black#1",   
    "facial_expressions-17": "Face evil eye blue skin tan#1",   
    "facial_expressions-18": "Face evil eye blue skin white#1",   
    "facial_expressions-19": "Face evil eye green skin black#1",   
    "facial_expressions-20": "Face evil eye green skin tan#1",   
    "facial_expressions-21": "Face evil eye green skin white#1",   
    "facial_expressions-22": "Face evil eye purple skin black#1",   
    "facial_expressions-23": "Face evil eye purple skin tan#1",   
    "facial_expressions-24": "Face evil eye purple skin white#1",   
    "facial_expressions-25": "Face growl eye blue skin black#1",   
    "facial_expressions-26": "Face growl eye blue skin tan#1",   
    "facial_expressions-27": "Face growl eye blue skin white#1",   
    "facial_expressions-28": "Face growl eye green skin black#1",   
    "facial_expressions-29": "Face growl eye green skin tan#1",   
    "facial_expressions-30": "Face growl eye green skin white#1",   
    "facial_expressions-31": "Face growl eye purple skin black#1",   
    "facial_expressions-32": "Face growl eye purple skin tan#1",   
    "facial_expressions-33": "Face growl eye purple skin white#1",   
    "facial_expressions-34": "Face grumpy eye blue skin black#1",   
    "facial_expressions-35": "Face grumpy eye blue skin tan#1",   
    "facial_expressions-36": "Face grumpy eye blue skin white#1",   
    "facial_expressions-37": "Face grumpy eye green skin black#1",   
    "facial_expressions-38": "Face grumpy eye green skin tan#1",   
    "facial_expressions-39": "Face grumpy eye green skin white#1",   
    "facial_expressions-40": "Face grumpy eye purple skin black#1",   
    "facial_expressions-41": "Face grumpy eye purple skin tan#1",   
    "facial_expressions-42": "Face grumpy eye purple skin white#1",   
    "facial_expressions-43": "Face happy eye blue skin black#1",   
    "facial_expressions-44": "Face happy eye blue skin tan#1",   
    "facial_expressions-45": "Face happy eye blue skin white#1",   
    "facial_expressions-46": "Face happy eye green skin black#1",   
    "facial_expressions-47": "Face happy eye green skin tan#1",   
    "facial_expressions-48": "Face happy eye green skin white#1",   
    "facial_expressions-49": "Face happy eye purple skin black#1",   
    "facial_expressions-50": "Face happy eye purple skin tan#1",   
    "facial_expressions-51": "Face happy eye purple skin white#1",   
    "facial_expressions-52": "Face nervous eye blue skin black#1",   
    "facial_expressions-53": "Face nervous eye blue skin tan#1",   
    "facial_expressions-54": "Face nervous eye blue skin white#1",   
    "facial_expressions-55": "Face nervous eye green skin black#1",   
    "facial_expressions-56": "Face nervous eye green skin tan#1",   
    "facial_expressions-57": "Face nervous eye green skin white#1",   
    "facial_expressions-58": "Face nervous eye purple skin black#1",   
    "facial_expressions-59": "Face nervous eye purple skin tan#1",   
    "facial_expressions-60": "Face nervous eye purple skin white#1",   
    "facial_expressions-61": "Face rage eye blue skin black#1",   
    "facial_expressions-62": "Face rage eye blue skin tan#1",   
    "facial_expressions-63": "Face rage eye blue skin white#1",   
    "facial_expressions-64": "Face rage eye green skin black#1",   
    "facial_expressions-65": "Face rage eye green skin tan#1",   
    "facial_expressions-66": "Face rage eye green skin white#1",  
    "facial_expressions-67": "Face rage eye purple skin black#1",   
    "facial_expressions-68": "Face rage eye purple skin tan#1",   
    "facial_expressions-69": "Face rage eye purple skin white#1",   
    "facial_expressions-70": "Face stoned eye blue skin black#1",   
    "facial_expressions-71": "Face stoned eye blue skin tan#1",   
    "facial_expressions-72": "Face stoned eye blue skin white#1",   
    "facial_expressions-73": "Face stoned eye green skin black#1",   
    "facial_expressions-74": "Face stoned eye green skin tan#1",   
    "facial_expressions-75": "Face stoned eye green skin white#1",   
    "facial_expressions-76": "Face stoned eye purple skin black#1",   
    "facial_expressions-77": "Face stoned eye purple skin tan#1",   
    "facial_expressions-78": "Face stoned eye purple skin white#1",   
    "facial_expressions-79": "Face yawn eye blue skin black#1",   
    "facial_expressions-80": "Face yawn eye blue skin tan#1",   
    "facial_expressions-81": "Face yawn eye blue skin white#1",   
    "facial_expressions-82": "Face yawn eye green skin black#1",   
    "facial_expressions-83": "Face yawn eye green skin tan#1",   
    "facial_expressions-84": "Face yawn eye green skin white#1",   
    "facial_expressions-85": "Face yawn eye purple skin black#1",   
    "facial_expressions-86": "Face yawn eye purple skin tan#1",   
    "facial_expressions-87": "Face yawn eye purple skin white#1"
}

war_paint_files = {    
    "war_paint-1": "Warpaint braveheart black",
    "war_paint-2": "Warpaint braveheart blue",
    "war_paint-3": "zNo warpaint#65",
    "war_paint-4": "zNo warpaint#65",
    "war_paint-5": "zNo warpaint#65",
    "war_paint-6": "zNo warpaint#65",
    "war_paint-7": "zNo warpaint#65",
    "war_paint-8": "zNo warpaint#65",
    "war_paint-9": "Warpaint braveheart red",
    "war_paint-10": "Warpaint braveheart silver",
    "war_paint-11": "Warpaint construct black",
    "war_paint-12": "Warpaint construct blue",
    "war_paint-13": "zNo warpaint#65",
    "war_paint-14": "Warpaint construct gold",
    "war_paint-15": "zNo warpaint#65",
    "war_paint-16": "zNo warpaint#65",
    "war_paint-17": "zNo warpaint#65",
    "war_paint-18": "zNo warpaint#65",
    "war_paint-19": "Warpaint construct red",
    "war_paint-20": "zNo warpaint#65",
    "war_paint-21": "Warpaint crossworks black",
    "war_paint-22": "Warpaint crossworks blue",
    "war_paint-23": "zNo warpaint#65",
    "war_paint-24": "Warpaint crossworks gold",
    "war_paint-25": "zNo warpaint#65",
    "war_paint-26": "zNo warpaint#65",
    "war_paint-27": "zNo warpaint#65",
    "war_paint-28": "zNo warpaint#65",
    "war_paint-29": "Warpaint crossworks red",
    "war_paint-30": "zNo warpaint#65",
    "war_paint-31": "zNo warpaint#65",
    "war_paint-32": "zNo warpaint#65",
    "war_paint-33": "zNo warpaint#65",
    "war_paint-34": "warpaint drips gold",
    "war_paint-35": "zNo warpaint#65",
    "war_paint-36": "zNo warpaint#65",
    "war_paint-37": "zNo warpaint#65",
    "war_paint-38": "zNo warpaint#65",
    "war_paint-39": "zNo warpaint#65",
    "war_paint-40": "zNo warpaint#65",
    "war_paint-41": "Warpaint handprint black",
    "war_paint-42": "Warpaint handprint blue",
    "war_paint-43": "zNo warpaint#65",
    "war_paint-44": "Warpaint handprint gold",
    "war_paint-45": "zNo warpaint#65",
    "war_paint-46": "zNo warpaint#65",
    "war_paint-47": "zNo warpaint#65",
    "war_paint-48": "zNo warpaint#65",
    "war_paint-49": "Warpaint handprint red",
    "war_paint-50": "zNo warpaint#65",
    "war_paint-51": "Warpaint moth black",
    "war_paint-52": "Warpaint moth blue",
    "war_paint-53": "zNo warpaint#65",
    "war_paint-54": "zNo warpaint#65",
    "war_paint-55": "zNo warpaint#65",
    "war_paint-56": "zNo warpaint#65",
    "war_paint-57": "zNo warpaint#65",
    "war_paint-58": "zNo warpaint#65",
    "war_paint-59": "Warpaint moth red",
    "war_paint-60": "Warpaint moth silver",
    "war_paint-61": "zNo warpaint#65",
    "war_paint-62": "zNo warpaint#65",
    "war_paint-63": "zNo warpaint#65",
    "war_paint-64": "zNo warpaint#65",
    "war_paint-65": "zNo warpaint#65",
    "war_paint-66": "zNo warpaint#65",
    "war_paint-67": "zNo warpaint#65",
    "war_paint-68": "zNo warpaint#65",
    "war_paint-69": "zNo warpaint#65",
    "war_paint-70": "Warpaint ribs silver",
    "war_paint-71": "Warpaint spiked black",
    "war_paint-72": "Warpaint spiked blue",
    "war_paint-73": "Warpaint spiked silver",
    "war_paint-74": "zNo warpaint#65",
    "war_paint-75": "zNo warpaint#65",
    "war_paint-76": "zNo warpaint#65",
    "war_paint-77": "zNo warpaint#65",
    "war_paint-78": "zNo warpaint#65",
    "war_paint-79": "Warpaint spikes red",
    "war_paint-80": "zNo warpaint#65",
    "war_paint-81": "zNo warpaint#65",
    "war_paint-82": "zNo warpaint#65",
    "war_paint-83": "zNo warpaint#65",
    "war_paint-84": "Warpaint stalactites gold",
    "war_paint-85": "zNo warpaint#65",
    "war_paint-86": "zNo warpaint#65",
    "war_paint-87": "zNo warpaint#65",
    "war_paint-88": "zNo warpaint#65",
    "war_paint-89": "zNo warpaint#65",
    "war_paint-90": "zNo warpaint#65",
    "war_paint-91": "Warpaint tears black",
    "war_paint-92": "Warpaint tears blue",
    "war_paint-93": "zNo warpaint#65",
    "war_paint-94": "zNo warpaint#65",
    "war_paint-95": "zNo warpaint#65",
    "war_paint-96": "zNo warpaint#65",
    "war_paint-97": "zNo warpaint#65",
    "war_paint-98": "zNo warpaint#65",
    "war_paint-99": "Warpaint tears red",
    "war_paint-100": "Warpaint tears silver",
    "war_paint-101": "Warpaint tendrils black",
    "war_paint-102": "Warpaint tendrils blue",
    "war_paint-103": "zNo warpaint#65",
    "war_paint-104": "zNo warpaint#65",
    "war_paint-105": "zNo warpaint#65",
    "war_paint-106": "zNo warpaint#65",
    "war_paint-107": "zNo warpaint#65",
    "war_paint-108": "zNo warpaint#65",
    "war_paint-109": "Warpaint tendrils red",
    "war_paint-110": "Warpaint tendrils silver",
    "war_paint-111": "Warpaint trident black",
    "war_paint-112": "Warpaint trident blue",
    "war_paint-113": "zNo warpaint#65",
    "war_paint-114": "zNo warpaint#65",
    "war_paint-115": "zNo warpaint#65",
    "war_paint-116": "zNo warpaint#65",
    "war_paint-117": "zNo warpaint#65",
    "war_paint-118": "zNo warpaint#65",
    "war_paint-119": "Warpaint trident red",
    "war_paint-120": "Warpaint trident silver",    
    "war_paint-121": "zNo warpaint#65",
    "war_paint-122": "zNo warpaint#65",
    "war_paint-123": "zNo warpaint#65",
    "war_paint-124": "Warpaint veins gold",
    "war_paint-125": "zNo warpaint#65",
    "war_paint-126": "zNo warpaint#65",  
    "war_paint-127": "zNo warpaint#65",
    "war_paint-128": "zNo warpaint#65",
    "war_paint-129": "zNo warpaint#65",
    "war_paint-130": "zNo warpaint#65",
    "war_paint-131": "Warpaint wings black",
    "war_paint-132": "Warpaint wings blue",
    "war_paint-133": "zNo warpaint#65",
    "war_paint-134": "Warpaint wings gold",
    "war_paint-135": "zNo warpaint#65",
    "war_paint-136": "zNo warpaint#65",
    "war_paint-137": "zNo warpaint#65",
    "war_paint-138": "zNo warpaint#65",
    "war_paint-139": "Warpaint wings red",
    "war_paint-140": "Warpaint thunder struck #1",
    "war_paint-141": "zNo warpaint#65"
}

eyebrows_files = {
    "eyebrows-1": "Eyebrow angry black",
    "eyebrows-2": "Eyebrow angry blonde",
    "eyebrows-3": "Eyebrow angry blue",
    "eyebrows-4": "Eyebrow angry brown",
    "eyebrows-5": "Eyebrow angry green",
    "eyebrows-6": "Eyebrow angry grey",
    "eyebrows-7": "Eyebrow angry pink",
    "eyebrows-8": "Eyebrow angry purple",
    "eyebrows-9": "Eyebrow angry red",
    "eyebrows-10": "Eyebrow bored black",
    "eyebrows-11": "Eyebrow bored blonde",
    "eyebrows-12": "Eyebrow bored blue",
    "eyebrows-13": "Eyebrow bored brown",
    "eyebrows-14": "Eyebrow bored green",
    "eyebrows-15": "Eyebrow bored grey",
    "eyebrows-16": "Eyebrow bored pink",
    "eyebrows-17": "Eyebrow bored purple",
    "eyebrows-18": "Eyebrow bored red",
    "eyebrows-19": "Eyebrow happy black",
    "eyebrows-20": "Eyebrow happy blonde",
    "eyebrows-21": "Eyebrow happy blue",
    "eyebrows-22": "Eyebrow happy brown",
    "eyebrows-23": "Eyebrow happy green",
    "eyebrows-24": "Eyebrow happy grey",
    "eyebrows-25": "Eyebrow happy pink",
    "eyebrows-26": "Eyebrow happy purple",
    "eyebrows-27": "Eyebrow happy red",
    "eyebrows-28": "Eyebrow helmet black",
    "eyebrows-29": "Eyebrow helmet blonde",
    "eyebrows-30": "Eyebrow helmet blue",
    "eyebrows-31": "Eyebrow helmet brown",
    "eyebrows-32": "Eyebrow helmet green",
    "eyebrows-33": "Eyebrow helmet grey",
    "eyebrows-34": "Eyebrow helmet pink",
    "eyebrows-35": "Eyebrow helmet purple",
    "eyebrows-36": "Eyebrow helmet red",
    "eyebrows-37": "Eyebrow serious black",
    "eyebrows-38": "Eyebrow serious blonde",
    "eyebrows-39": "Eyebrow serious blue",
    "eyebrows-40": "Eyebrow serious brown",
    "eyebrows-41": "Eyebrow serious green",
    "eyebrows-42": "Eyebrow serious grey",
    "eyebrows-43": "Eyebrow serious pink",
    "eyebrows-44": "Eyebrow serious purple",
    "eyebrows-45": "Eyebrow serious red"
}

hair_files = {
    "hair-1": "Hair grass mohawk black#1",
    "hair-2": "Hair grass mohawk blonde",
    "hair-3": "Hair grass mohawk blue#1",
    "hair-4": "Hair grass mohawk brown#1",
    "hair-5": "Hair grass mohawk green#1",
    "hair-6": "Hair grass mohawk grey#1",
    "hair-7": "Hair grass mohawk pink#1",
    "hair-8": "Hair grass mohawk purple#1",
    "hair-9": "Hair grass mohawk red#1",
    "hair-10": "Hair lizard black#0.5",
    "hair-11": "Hair lizard blonde#0.5",
    "hair-12": "Hair lizard blue#0.5",
    "hair-13": "Hair lizard brown#0.5",
    "hair-14": "hair lizard green#0.5",
    "hair-15": "Hair lizard grey#0.5",
    "hair-16": "Hair lizard pink#0.5",
    "hair-17": "Hair lizard purple#0.5",
    "hair-18": "Hair lizard red#0.5",
    "hair-19": "Hair long braids black#1.5",
    "hair-20": "Hair long braids blonde#1.5",
    "hair-21": "Hair long braids blue#1.5",
    "hair-22": "Hair long braids brown#1.5",
    "hair-23": "Hair long braids green#1.5",
    "hair-24": "Hair long braids grey#1.5",
    "hair-25": "Hair long braids pink#1.5",
    "hair-26": "Hair long braids purple#1.5",
    "hair-27": "hair long braids red#1.5",
    "hair-28": "Hair short bun black#2",
    "hair-29": "hair short bun blonde#2",
    "hair-30": "Hair short bun blue#2",
    "hair-31": "Hair short bun brown#2",
    "hair-32": "Hair short bun green#2",
    "hair-33": "Hair short bun grey#2",
    "hair-34": "Hair short bun pink#2",
    "hair-35": "Hair short bun purple#2",
    "hair-36": "hair short bun red#2",
    "hair-37": "Hair short unkept black#1.5",
    "hair-38": "Hair short unkept blonde#1.5",
    "hair-39": "Hair short unkept blue#1.5",
    "hair-40": "Hair short unkept brown#1.5",
    "hair-41": "Hair short unkept green#1.5",
    "hair-42": "Hair short unkept grey#1.5",
    "hair-43": "Hair short unkept pink#1.5",
    "hair-44": "Hair short unkept purple#1.5",
    "hair-45": "Hair short unkept red#1.5",
    "hair-46": "Hair spike mohawk black#1",
    "hair-47": "hair spike mohawk blodne#1",
    "hair-48": "Hair spike mohawk blue#1",
    "hair-49": "Hair spike mohawk brown#1",
    "hair-50": "Hair spike mohawk green#1",
    "hair-51": "Hair spike mohawk grey#1",
    "hair-52": "Hair spike mohawk pink#1",
    "hair-53": "Hair spike mohawk purple#1",
    "hair-54": "Hair spike mohawk red#1",
    "hair-55": "Hair star black#0.5",
    "hair-56": "Hair star blonde#0.5",
    "hair-57": "Hair star blue#0.5",
    "hair-58": "Hair star brown#0.5",
    "hair-59": "hair star green#0.5",
    "hair-60": "Hair star grey#0.5",
    "hair-61": "hair star pink#0.5",
    "hair-62": "Hair star purple#0.5",
    "hair-63": "Hair star red#0.5",
    "hair-64": "Hair topknot black#2",
    "hair-65": "hair topknot blonde#2",
    "hair-66": "Hair topknot blue#2",
    "hair-67": "Hair topknot brown#2",
    "hair-68": "Hair topknot green#2",
    "hair-69": "Hair topknot grey#2",
    "hair-70": "Hair topknot pink#2",
    "hair-71": "hair topknot purple#2",
    "hair-72": "Hair topknot red#2"
}

mage_hoods_files = {
    "mage_hoods-1": "Hood mage hood blue#5",
    "mage_hoods-2": "Hood mage hood gold#1",
    "mage_hoods-3": "Hood mage hood green#5",
    "mage_hoods-4": "Hood mage hood purple#5",
    "mage_hoods-5": "Hood mage hood red#5",
    "mage_hoods-6": "Hood mage hood silver#1",
    "mage_hoods-7": "No hood#78"
}

beards_files = {
    "beards-1": "Beard fluffy black#2",
    "beards-2": "Beard fluffy blonde#2",
    "beards-3": "Beard fluffy blue#2",
    "beards-4": "Beard fluffy brown#2",
    "beards-5": "Beard fluffy green#2",
    "beards-6": "Beard fluffy grey#2",
    "beards-7": "Beard fluffy pink#2",
    "beards-8": "Beard fluffy purple#2",
    "beards-9": "Beard fluffy red#2",
    "beards-10": "Beard goatee mustache black#1",
    "beards-11": "Beard goatee mustache blonde#1",
    "beards-12": "Beard goatee mustache blue#1",
    "beards-13": "Beard goatee mustache brown#1",
    "beards-14": "Beard goatee mustache green#1",
    "beards-15": "Beard goatee mustache grey#1",
    "beards-16": "Beard goatee mustache pink#1",
    "beards-17": "Beard goatee mustache purple#1",
    "beards-18": "Beard goatee mustache red#1",
    "beards-19": "Beard handlebars black#1.5",
    "beards-20": "Beard handlebars blonde#1.5",
    "beards-21": "Beard handlebars blue#1.5",
    "beards-22": "Beard handlebars brown#1.5",
    "beards-23": "Beard handlebars green#1.5",
    "beards-24": "Beard handlebars grey#1.5",
    "beards-25": "Beard handlebars pink#1.5",
    "beards-26": "Beard handlebars purple#1.5",
    "beards-27": "Beard handlebars red#1.5",
    "beards-28": "Beard mustache sideburns black#1.5",
    "beards-29": "Beard mustache sideburns blonde#1.5",
    "beards-30": "Beard mustache sideburns blue#1.5",
    "beards-31": "Beard mustache sideburns brown#1.5",
    "beards-32": "Beard mustache sideburns green#1.5",
    "beards-33": "Beard mustache sideburns grey#1.5",
    "beards-34": "Beard mustache sideburns pink#1.5",
    "beards-35": "Beard mustache sideburns purple#1.5",
    "beards-36": "Beard mustache sideburns red#1.5",
    "beards-37": "Beard scruffy braid black#0.5",
    "beards-38": "Beard scruffy braid blonde#0.5",
    "beards-39": "Beard scruffy braid blue#0.5",
    "beards-40": "Beard scruffy braid brown#0.5",
    "beards-41": "Beard scruffy braid green#0.5",
    "beards-42": "Beard scruffy braid grey#0.5",
    "beards-43": "Beard scruffy braid pink#0.5",
    "beards-44": "Beard scruffy braid purple#0.5",
    "beards-45": "Beard scruffy braid red#0.5",
    "beards-46": "Beard short braids black#1",
    "beards-47": "Beard short braids blonde#1",
    "beards-48": "Beard short braids blue#1",
    "beards-49": "Beard short braids brown#1",
    "beards-50": "Beard short braids green#1",
    "beards-51": "Beard short braids grey#1",
    "beards-52": "Beard short braids pink#1",
    "beards-53": "Beard short braids purple#1",
    "beards-54": "Beard short braids red#1",
    "beards-55": "Beard star black#5",
    "beards-56": "Beard star blonde#5",
    "beards-57": "Beard star blue#5",
    "beards-58": "Beard star brown#5",
    "beards-59": "Beard star green#5",
    "beards-60": "Beard star grey#5",
    "beards-61": "Beard star pink#5",
    "beards-62": "Beard star purple",
    "beards-63": "Beard star red#5",
    "beards-64": "Beard twin fluffy black#2",
    "beards-65": "Beard twin fluffy Blonde#2",
    "beards-66": "Beard twin fluffy blue#2",
    "beards-67": "Beard twin fluffy brown#2",
    "beards-68": "Beard twin fluffy green#2",
    "beards-69": "Beard twin fluffy grey#2",
    "beards-70": "Beard twin fluffy pink#2",
    "beards-71": "Beard twin fluffy purple#2",
    "beards-72": "Beard twin fluffy red#2"
}

arms_files = {
    "arms-1": "Arm double grip black",
    "arms-2": "Arm double grip tan",
    "arms-3": "Arm double grip white",
    "mage-1": "Arm mage hand black",
    "mage-2": "Arm mage hand tan",
    "mage-3": "Arm mage hand white",
    "arms-7": "Arm single arm black",
    "arms-8": "Arm single arm tan",
    "arms-9": "Arm single arm white",
    "arms-10": "Arm staff hand black",
    "arms-11": "Arm staff hand tan",
    "arms-12": "Arm staff hand white",
    "arms-13": "Arm two arms black",
    "arms-14": "Arm two arms tan",
    "arms-15": "Arm two arms white"
}

weapon_files = {    
    "weapon_one_hand-1": "Weapon laser gun blue#10",
    "weapon_one_hand-2": "Weapon laser gun green#10",
    "weapon_one_hand-3": "Weapon laser gun purple#10",
    "weapon_one_hand-4": "Weapon laser gun red#10",
    "weapon_one_hand-5": "Weapon space gun blue",
    "weapon_one_hand-6": "Weapon space gun gold",
    "weapon_one_hand-7": "Weapon space gun green",
    "weapon_one_hand-8": "Weapon space gun purple",
    "weapon_one_hand-9": "Weapon space gun red",
    "weapon_one_hand-10": "Weapon space gun silver",
    "weapon_one_hand-back-11": "Weapon flametongue blue",
    "weapon_one_hand-back-12": "Weapon flametongue green",
    "weapon_one_hand-back-13": "Weapon flametongue purple",
    "weapon_one_hand-back-14": "Weapon flametongue red",
    "weapon_one_hand-back-15": "Weapon plasma blade blue#5",
    "weapon_one_hand-back-16": "Weapon plasma blade green#5",
    "weapon_one_hand-back-17": "Weapon plasma blade purple#5",
    "weapon_one_hand-back-18": "Weapon plasma blade red#5",
    "weapon_one_hand-back-19": "Weapon warhammer blue#5",
    "weapon_one_hand-back-20": "Weapon warhammer gold",
    "weapon_one_hand-back-21": "Weapon warhammer green#5",
    "weapon_one_hand-back-22": "Weapon warhammer purple#5",
    "weapon_one_hand-back-23": "Weapon warhammer red#5",
    "weapon_one_hand-back-24": "Weapon warhammer silver",
    "weapon_dual_wield-1": "Weapon assasin daggers blue",
    "weapon_dual_wield-2": "Weapon assassin daggers green",
    "weapon_dual_wield-3": "Weapon assassin daggers purple",
    "weapon_dual_wield-4": "Weapon assasin daggers red",
    "weapon_dual_wield-5": "Weapon assassin daggers silver",
    "weapon_dual_wield-6": "Weapon glass daggers blue",
    "weapon_dual_wield-7": "Weapon glass daggers gold",
    "weapon_dual_wield-8": "Weapon glass dagger green",
    "weapon_dual_wield-9": "Weapon glass daggers purple",
    "weapon_dual_wield-10": "Weapon glass daggers red", 
    "weapon_double_grip-1": "Weapon flamethrower blue",
    "weapon_double_grip-2": "Weapon flamethrower gold",
    "weapon_double_grip-3": "Weapon flamethrower green",
    "weapon_double_grip-4": "Weapon flamethrower purple",
    "weapon_double_grip-5": "Weapon flamethrower red",
    "weapon_double_grip-6": "Weapon flamethrower silver",
    "weapon_double_grip-7": "Weapon genesis pickaxe#0.1",
    "weapon_double_grip-8": "Weapon Gold pickaxe#0.5",
    "weapon_double_grip-9": "Weapon plasma axe blue#5",
    "weapon_double_grip-10": "Weapon plasma axe green#5",
    "weapon_double_grip-11": "Weapon plasma axe purple#5",
    "weapon_double_grip-12": "Weapon plasma axe red#5",
    "weapon_double_grip-13": "Weapon rifle blue#5",
    "weapon_double_grip-14": "Weapon rifle gold",
    "weapon_double_grip-15": "Weapon rifle green#5",
    "weapon_double_grip-16": "Weapon rifle purple#5",
    "weapon_double_grip-17": "Weapon rifle red#5",
    "weapon_double_grip-18": "Weapon rifle silver",
    "weapon_double_grip-19": "Weapon shotgun blue#5",
    "weapon_double_grip-20": "Weapon shotgun blue#5",
    "weapon_double_grip-21": "Weapon shotgun purple#5",
    "weapon_double_grip-22": "Weapon silver pickaxe#1",
    "weapon_double_grip-23": "Weapon shotgun red#5",
    "weapon_staff-1": "Weapon battleaxe blue",
    "weapon_staff-2": "Weapon battleaxe green",
    "weapon_staff-3": "Weapon battleaxe purple",
    "weapon_staff-4": "Weapon battleaxe red",
    "weapon_staff-5": "Weapon crystal staff blue#5",
    "weapon_staff-6": "Weapon crystal staff green#5",
    "weapon_staff-7": "Weapon crystal staff purple#5",
    "weapon_staff-8": "Weapon crystal staff red#5",
    "weapon_staff-9": "Weapon crystal staff gold",
    "weapon_staff-10": "Weapon crystal staff silver",
    "weapon_staff-11": "Weapon lightsaber blue#5",
    "weapon_staff-12": "Weapon lightsaber gold#0.5",
    "weapon_staff-13": "Weapon lightsaber green#5",
    "weapon_staff-14": "Weapon lightsaber purple#5",
    "weapon_staff-15": "Weapon lightsaber red#5",
    "weapon_staff-16": "Weapon lightsaber silver#1",
    "weapon_staff-17": "Weapon oracle staff blue#5",
    "weapon_staff-18": "Weapon oracle staff green#5",
    "weapon_staff-19": "Weapon oracle staff purple#5",
    "weapon_staff-20": "Weapon oracle staff red#5",
    "weapon_staff-21": "Weapon starsword blue#5",
    "weapon_staff-22": "Weapon starsword green#5",
    "weapon_staff-23": "Weapon starsword purple#5",
    "weapon_staff-24": "Weapon starsword red#5",
    "weapon_mage_effect-1": "Fire ball#25",
    "weapon_mage_effect-2": "Gold orb#5",
    "weapon_mage_effect-3": "Lava orb#25",
    "weapon_mage_effect-4": "Lightning orb#25",
    "weapon_mage_effect-5": "Silver orb#10",
    "weapon_back-1": "Weapon back axes gold#0.5",
    "weapon_back-2": "Weapon back axes silver#1",
    "weapon_back-3": "Weapon back daggers blue#5",
    "weapon_back-4": "Weapon back daggers red#5",
    "weapon_back-5": "Weapon back daggers green#5",
    "weapon_back-6": "Weapon back daggers purple#5",
    "weapon_back-7": "Weapon back swords silver",
    "weapon_back-8": "Weapon back swords gold",
    "weapon_back-9": "Weapon katanas blue#5",
    "weapon_back-10": "Weapon katanas green#5",
    "weapon_back-11": "Weapon katanas purple#5",
    "weapon_back-12": "Weapon katanas red#5",
    "no_weapon" : "zNO_weapon"
}
  

arm_armor_files = {
    "arm_armor-1": "Hand double grip explorer black",
    "arm_armor-2": "Hand double grip explorer blue",
    "arm_armor-3": "Hand double grip explorer brown",
    "arm_armor-4": "Hand double grip explorer gold",
    "arm_armor-5": "Hand double grip explorer green",
    "arm_armor-6": "Hand double grip explorer grey",
    "arm_armor-7": "Hand double grip explorer pink",
    "arm_armor-8": "Hand double grip explorer purple",
    "arm_armor-9": "Hand double grip explorer red",
    "arm_armor-10": "Hand double grip explorer silver",
    "mage_hand-21": "Hand mage hand explorer black#1",
    "mage_hand-22": "Hand mage hand blue#1",
    "mage_hand-23": "Hand mage hand brown#1",
    "mage_hand-24": "Hand mage hand explorer gold#1",
    "mage_hand-25": "Hand mage hand explorer  green#1",
    "mage_hand-26": "Hand mage hand explorer grey#1",
    "mage_hand-27": "Hand mage hand explorer pink#1",
    "mage_hand-28": "Hand mage hand explorer purple#1",
    "mage_hand-29": "Hand mage hand explorer red",
    "mage_hand-20": "Hand mage hand explorer silver#1",
    "arm_armor-21": "Hand single arm explorer black#1",
    "arm_armor-22": "Hand Single arm explorer blue#1",
    "arm_armor-23": "Hand Single arm explorer brown#1",
    "arm_armor-24": "Hand single arm explorer gold#1",
    "arm_armor-25": "Hand Single arm explorer green#1",
    "arm_armor-26": "Hand Single arm explorer grey#1",
    "arm_armor-27": "Hand Single arm explorer pink#1",
    "arm_armor-28": "Hand Single arm purple explorer#1",
    "arm_armor-29": "Hand Single arm explorer red#1",
    "arm_armor-30": "Hand single arm explorer silver#1",
    "arm_armor-31": "Hand staff hand explorer black#1",
    "arm_armor-32": "Hand staff hand explorer blue#1",
    "arm_armor-33": "Hand staff hand explorer brown#1",
    "arm_armor-34": "Hand staff hand explorer gold#1",
    "arm_armor-35": "Hand staff hand explorer green#1",
    "arm_armor-36": "Hand staff hand explorer grey#1",
    "arm_armor-37": "Hand staff hand explorer pink#1",
    "arm_armor-38": "Hand staff hand explorer purple#1",
    "arm_armor-39": "Hand staff hand explorer red#1",
    "arm_armor-40": "Hand staff hand explorer silver#1",
    "arm_armor-41": "Hand two arms explorer black#1",
    "arm_armor-42": "Hand two arms explorer blue#1",
    "arm_armor-43": "Hand two arms explorer brown#1",
    "arm_armor-44": "Hand two arms explorer gold#1",
    "arm_armor-45": "Hand two arms explorer green#1",
    "arm_armor-46": "Hand two arms Explorer grey#1",
    "arm_armor-47": "Hand two arms explorer pink#1",
    "arm_armor-48": "Hand two arms explorer purple#1",
    "arm_armor-49": "Hand two arms explorer red#1",
    "arm_armor-50": "Hand two arms explorer silver#1",
    "arm_armor-51": "Hand double grip observer black",
    "arm_armor-52": "Hand double grip observer blue",
    "arm_armor-53": "Hand double grip observer brown",
    "arm_armor-54": "Hand double grip observer gold",
    "arm_armor-55": "Hand double grip observer green",
    "arm_armor-56": "Hand double grip observer grey",
    "arm_armor-57": "Hand double grip observer pink",
    "arm_armor-58": "Hand double grip observer purple",
    "arm_armor-59": "Hand double grip observer red",
    "arm_armor-60": "Hand double grip observer silver",
    "mage_armor-1": "Hand mage hand observer black#1",
    "mage_armor-2": "Hand mage hand observer blue#1",
    "mage_armor-3": "Hand mage hand observer brown#1",
    "mage_armor-4": "Hand mage hand observer gold#1",
    "mage_armor-5": "Hand mage hand observer green#1",
    "mage_armor-6": "Hand mage hand observer grey#1",
    "mage_armor-7": "Hand mage hand observer pink#1",
    "mage_armor-8": "Hand mage hand observer purple#1",
    "mage_armor-9": "Hand mage hand observer red#1",
    "mage_armor-10": "Hand mage hand observer silver#1",
    "arm_armor-71": "Hand single arm observer black#1",
    "arm_armor-72": "Hand single arm observer blue#1",
    "arm_armor-73": "Hand single  arm observer brown#1",
    "arm_armor-74": "Hand single arm observer gold#1",
    "arm_armor-75": "Hand single  arm observer green#1",
    "arm_armor-76": "hand single arm observer grey#1",
    "arm_armor-77": "Hand single arm observer pink#1",
    "arm_armor-78": "Hand single arm observer purple#1",
    "arm_armor-79": "Hand single arm observer red#1",
    "arm_armor-80": "Hand single arm observer silver#1",
    "arm_armor-81": "Hand staff hand observer black#1",
    "arm_armor-82": "Hand staff hand observer blue#1",
    "arm_armor-83": "Hand staff hand observer brown#1",
    "arm_armor-84": "Hand staff hand observer gold#1",
    "arm_armor-85": "Hand staff hand observer green#1",
    "arm_armor-86": "Hand staff hand observer grey#1",
    "arm_armor-87": "Hand staff hand observer pink#1",
    "arm_armor-88": "Hand staff hand observer purple#1",
    "arm_armor-89": "Hand staff hand observer red#1",
    "arm_armor-90": "Hand staff hand silver observer#1",
    "arm_armor-91": "Hand two arms observer black#1",
    "arm_armor-92": "Hand two arms observer blue#1",
    "arm_armor-93": "Hand two arms observer brown#1",
    "arm_armor-94": "Hand two arms observer gold#1",
    "arm_armor-95": "Hand two arms observer green#1",
    "arm_armor-96": "Hand two arms observer grey#1",
    "arm_armor-97": "Hand two arms observer pink#1",
    "arm_armor-98": "Hand two arms observer purple#1",
    "arm_armor-99": "Hand two arms observer red#1",
    "arm_armor-100": "Hand two arms observer silver#1",
    "mage_armor-11": "Arms mage hand commander silver",
    "arm_armor-102": "Hand double grip aqua#1",
    "arm_armor-103": "Hand double grip black#1",
    "arm_armor-104": "Hand double grip brawler gold and silver",
    "arm_armor-105": "Hand double grip bronze#1",
    "arm_armor-106": "Hand double grip bubblegum#1",
    "arm_armor-107": "Hand double grip commander gold",
    "arm_armor-108": "Hand double grip commander silver",
    "arm_armor-109": "hand double grip lava#1",
    "arm_armor-110": "Hand double grip moss#1",
    "arm_armor-111": "Hand double grip protector gold and silver",
    "arm_armor-112": "Hand double grip rainbow#1",
    "arm_armor-113": "Hand double grip sun#1",
    "arm_armor-114": "Hand double grip trooper gold",
    "arm_armor-115": "Hand double grip trooper silver",
    "arm_armor-116": "Hand mage hand aqua#1",
    "arm_armor-117": "Hand mage hand black#1",
    "arm_armor-118": "Hand mage hand brawler#1",
    "arm_armor-119": "Hand mage hand bubblegum#1",
    "arm_armor-120": "hand mage hand commander bronze",
    "arm_armor-121": "Hand mage hand commander gold",
    "arm_armor-122": "Hand mage hand lava#1",
    "arm_armor-123": "Hand mage hand moss#1",
    "arm_armor-124": "Hand mage hand protector",
    "arm_armor-125": "Hand mage hand rainbow#1",
    "arm_armor-126": "Hand mage hand sun#1",
    "arm_armor-127": "Hand mage hand trooper gold",
    "arm_armor-128": "Hand mage hand trooper silver",
    "arm_armor-129": "Hand one arm rainbow#1",
    "arm_armor-130": "Hand single arm aqua#1",
    "arm_armor-131": "Hand single arm black#1",
    "arm_armor-132": "hand single arm bubblegum#1",
    "arm_armor-133": "Hand single arm commander bronze",
    "arm_armor-134": "Hand single arm commander gold",
    "arm_armor-135": "Hand single arm commander silver",
    "arm_armor-136": "Hand single arm gold and silver brawler#1",
    "arm_armor-137": "Hand single arm lava#1",
    "arm_armor-138": "hand single arm moss#1",
    "arm_armor-139": "Hand single arm protector",
    "arm_armor-140": "Hand single arm sun#1",
    "arm_armor-141": "Hand single arm trooper gold",
    "arm_armor-142": "Hand single arm trooper silver",
    "arm_armor-143": "Hand staff hand aqua#1",
    "arm_armor-144": "Hand staff hand black#1",
    "arm_armor-145": "Hand staff hand brawler#1",
    "arm_armor-146": "Hand staff hand bubblegum#1",
    "arm_armor-147": "Hand staff hand commander bronze",
    "arm_armor-148": "Hand staff hand commander gold",
    "arm_armor-149": "Hand staff hand lava#1",
    "arm_armor-150": "hand staff hand moss#1",
    "arm_armor-151": "Hand staff hand protector",
    "arm_armor-152": "Hand staff hand rainbow#1",
    "arm_armor-153": "Hand staff hand silver",
    "arm_armor-154": "Hand staff hand sun#1",
    "arm_armor-155": "Hand staff hand trooper gold",
    "arm_armor-156": "Hand staff hand trooper silver",
    "arm_armor-157": "Hand two arms aqua#1",
    "arm_armor-158": "Hand two arms black#1",
    "arm_armor-159": "Hand two arms brawler#1",
    "arm_armor-160": "Hand two arms comamnder silver",
    "arm_armor-161": "Hand two arms commander bronze",
    "arm_armor-162": "Hand two arms commander gold",
    "arm_armor-163": "Hand two arms lava#1",
    "arm_armor-164": "hand two arms moss#1",
    "arm_armor-165": "Hand two arms protector",
    "arm_armor-166": "Hand two arms rainbow#1",
    "arm_armor-167": "Hand two arms sun#1",
    "arm_armor-168": "Hand two arms trooper gold",
    "arm_armor-169": "Hand two arms trooper silver",
    "arm_armor-170": "Trooper two arms bubblegum#1"
}


extras_files = {
    "extras-1": "Extra burnt cigar#2",
    "extras-2": "Extra cigar gold",
    "extras-3": "Extra cigar silver",
    "extras-4": "Extra Cigar#2",
    "extras-5": "Extra earings gold",
    "extras-6": "Extra earings silver#1",
    "extras-7": "Extra Eyepatch black#2",
    "extras-8": "Extra eyepatch gold",
    "extras-9": "Extra eyepatch silver",
    "extras-10": "Extra goggle bronze",
    "extras-11": "Extra goggle gold",
    "extras-12": "Extra goggle silver",
    "extras-13": "Extra goggle simple",
    "extras-14": "Extra long cigar#2",
    "extras-15": "No extra#85",
    "extras-16": "visor glasses blue",
    "extras-17": "visor glasses green",
    "extras-18": "visor glasses purple",
    "extras-19": "visor glasses red",
    "extras-20": "visor laser blue",
    "extras-21": "visor laser green",
    "extras-22": "visor laser green",
    "extras-23": "visor laser red",
    "extras-24": "visor target"
}

constraint_helmet_hair = [
    'crown',
    'trooper',
    'halo',
    'horn'
]

## Generate Traits
TOTAL_IMAGES = 500   # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():

    sys.setrecursionlimit(3000)

    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["Helm_backpieces"] = 'helm_backpieces-5'
    # new_image ["Armor_back_pieces"] = random.choices(armor_back_pieces, armor_back_pieces_weights)[0]
    # new_image ["Base_body"] = random.choices(base_body, base_body_weights)[0]
    new_image ["Tattoos"] = random.choices(tattoos, tattoos_weights)[0]
    new_image ["Battle_armors"] = random.choices(battle_armors, battle_armors_weights)[0]
    new_image ["Scars"] = random.choices(scars, scars_weights)[0]  
    
    new_image ["War_paint"] = random.choices(war_paint, war_paint_weights)[0]  
    # new_image ["Eyebrows"] = random.choices(eyebrows, eyebrows_weights)[0]
    # new_image ["Hair"] = random.choices(hair, hair_weights)[0]   
    new_image ["Mage_hoods"] = random.choices(mage_hoods, mage_hoods_weights)[0]
    # new_image ["Beards"] = random.choices(beards, beards_weights)[0]
    new_image ["Weapon"] = random.choices(weapon, weapon_weights)[0]
    new_image ["Arm_armor"] = random.choices(arm_armor, arm_armor_weights)[0]
    new_image ["Extras"] = random.choices(extras, extras_weights)[0]


    # Constraint first

    #  Color of beard must match color of hair and eyebrows
    random_color_index = random.randint(0, 8)
    random_type_eyebrow = random.randint(0, 4)
    random_type_hair = random.randint(0, 7)
    random_type_beard = random.randint(0, 4)
    
    new_image['Eyebrows'] = eyebrows[random_type_eyebrow * 9 + random_color_index]
    new_image['Hair'] = hair[random_type_hair * 9 + random_color_index]
    new_image['Beards'] = beards[random_type_beard * 9 + random_color_index]

    # Color for Base Body, Arm Position and Facial Expression must be the same color = eg: Black or Tan or White Skin colors
    random_color_index_two = random.randint(0, 2)
    random_type_arms = random.randint(0, 4)
    random_type_expressions = random.randint(0, 28)

    new_image['Arms'] = arms[random_type_arms * 3 + random_color_index_two]
    new_image['Base_body'] = base_body[random_color_index_two]
    new_image['Facial_expressions'] = facial_expressions[random_type_expressions * 3 + random_color_index_two]

    # Colors of ARMOR, ARM ARMOR and HELMET must all be the same
    # enclosed armors and helmetless armors
    random_color_index_three = random.randint(0, 9)
    if 'explorer' in battle_armors_files[new_image['Battle_armors']] or 'observer' in battle_armors_files[new_image['Battle_armors']] or 'Explorer' in battle_armors_files[new_image['Battle_armors']]:
        
        random_type_arm_armor = random.randint(0, 9)
        random_type_helmetless_armor = random.randint(0, 3)
        random_type_warpaint = random.randint(0, 1)

        new_image['Arm_armor'] = arm_armor[random_type_arm_armor * 10 + random_color_index_three]
        new_image['Battle_armors'] = battle_armors[random_type_helmetless_armor * 10 + 16 + random_color_index_three]
        new_image["War_paint"] = war_paint[random_type_warpaint * 10 + random_color_index_three]

    # battle armors
    else:
        random_type_warpaint_special = random.randint(0, 13)

        if 'commander silver' in battle_armors_files[new_image['Battle_armors']]:
            if not 'commander silver' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            else: 
                new_image["War_paint"] = war_paint[random_type_warpaint_special * 10]
            # if not 'silver' in head_pieces_files[new_image['Head_pieces']] and 'and silver' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()
        if 'aqua' in battle_armors_files[new_image['Battle_armors']] or 'trooper angel' in battle_armors_files[new_image['Battle_armors']]:
            if not 'aqua' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            
            # if not 'aqua' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()

        if 'trooper black' in battle_armors_files[new_image['Battle_armors']]:
            if not 'black' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            else: 
                new_image["War_paint"] = war_paint[random_type_warpaint_special * 10 + 1]
            # if not 'black' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()

        if 'brawler' in battle_armors_files[new_image['Battle_armors']]:
            if not 'brawler' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            # if not 'aqua' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()

        if 'bubblegum' in battle_armors_files[new_image['Battle_armors']]:
            if not 'bubblegum' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            # if not 'Bubblegum' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()

        if 'commander bronze' in battle_armors_files[new_image['Battle_armors']]:
            if not 'commander bronze' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            # if not 'gold' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()

        if 'gold commander' in battle_armors_files[new_image['Battle_armors']]:
            if not 'commander gold' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            else: 
                new_image["War_paint"] = war_paint[random_type_warpaint_special * 10 + 4]
            # if not 'gold' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()

        if 'gold and silver' in battle_armors_files[new_image['Battle_armors']] or 'trooper gold' in battle_armors_files[new_image['Battle_armors']]:
            print('trooper gold')
            if not 'trooper gold' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            else: 
                new_image["War_paint"] = war_paint[random_type_warpaint_special * 10]
            # if not 'gold and silver' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()

        if 'trooper lava' in battle_armors_files[new_image['Battle_armors']]:
            if not 'lava' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            # if not 'lava' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()

        if 'moss' in battle_armors_files[new_image['Battle_armors']]:
            if not 'moss' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            # if not 'moss' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()

        if 'protector' in battle_armors_files[new_image['Battle_armors']]:
            if not 'protector' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            # if not 'angel' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()

        if 'rainbow' in battle_armors_files[new_image['Battle_armors']]:
            if not 'rainbow' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            # if not 'rainbow' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()

        if 'armor silver' in battle_armors_files[new_image['Battle_armors']]:
            if not 'trooper silver' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            else: 
                new_image["War_paint"] = war_paint[random_type_warpaint_special * 10]
            # if not 'silver' in head_pieces_files[new_image['Head_pieces']] and 'and silver' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()

        if 'trooper sun' in battle_armors_files[new_image['Battle_armors']]:
            if not 'sun' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            # if not 'sun' in head_pieces_files[new_image['Head_pieces']]:
            #     return create_new_image()

    # enclosed armors and mage hood can only have short hair
    if 'enclosed_armors' in new_image['Battle_armors'] or 'mage hood' in mage_hoods_files[new_image['Mage_hoods']]:
        if not ('short' in hair_files[new_image['Hair']] or 'lizard' in hair_files[new_image['Hair']]):
            return create_new_image()
        if not('handlebars' in beards_files[new_image['Beards']] or 'goatee mustache' in beards_files[new_image['Beards']] or 'scruffy braid' in beards_files[new_image['Beards']]  or 'short braids' in beards_files[new_image['Beards']]):
            return create_new_image()
        

    #  Only BEARDS = Handlebars, Goatee mustache, Scruffy Braid beards can go with enclosed armors or Pilot Helmets
    if 'handlebars' in beards_files[new_image['Beards']] or 'goatee mustache' in beards_files[new_image['Beards']] or 'scruffy braid' in beards_files[new_image['Beards']]:
        if not 'enclosed_armors' in new_image['Battle_armors']:
            return create_new_image()

    #  Helmet Eyebrows are for Helmets and Enclose Suits/Armors
    if 'helmet' in eyebrows_files[new_image['Eyebrows']]:
        # if new_image['Head_pieces'] == 'head_pieces-5' or not 'enclosed_armors' in new_image['Battle_armors']:
        if not 'enclosed_armors' in new_image['Battle_armors']:
            return create_new_image()
            
    #  When a suit is picked it's corresponding suit back must be added  
    if ('explorer' in battle_armors_files[new_image['Battle_armors']] or 'Explorer' in battle_armors_files[new_image['Battle_armors']]) and not 'helmetless' in battle_armors_files[new_image['Battle_armors']]:
        new_image['Armor_back_pieces'] = 'armor_back_pieces-40'
    elif 'observer' in battle_armors_files[new_image['Battle_armors']] and not 'helmetless' in battle_armors_files[new_image['Battle_armors']]:
        new_image['Armor_back_pieces'] = 'armor_back_pieces-41' 
    else: 

        if 'helmetless explorer' in battle_armors_files[new_image['Battle_armors']]:

            arr_helmetless_explorer = [
                "armor_back_pieces-16",
                "armor_back_pieces-17",
                "armor_back_pieces-18",
                "armor_back_pieces-19",
                "armor_back_pieces-20",
                "armor_back_pieces-21",
                "armor_back_pieces-22",
                "armor_back_pieces-23",
                "armor_back_pieces-24",
                "armor_back_pieces-25",
                "armor_back_pieces-26",
                "armor_back_pieces-27",
            ]
            new_image['Armor_back_pieces'] = random.choice(arr_helmetless_explorer)
        else:
            arr_helmetless_observer = [
                "armor_back_pieces-28",
                "armor_back_pieces-29",
                "armor_back_pieces-30",
                "armor_back_pieces-31",
                "armor_back_pieces-32",
                "armor_back_pieces-33",
                "armor_back_pieces-34",
                "armor_back_pieces-35",
                "armor_back_pieces-36",
                "armor_back_pieces-37",
                "armor_back_pieces-38",
                "armor_back_pieces-39",
            ]
            new_image['Armor_back_pieces'] = random.choice(arr_helmetless_observer)

    #  position Mage Hand, Mage Hand with Mage Effect Weapons
    if 'mage' in arms_files[new_image['Arms']]:
        if  not 'mage' in arm_armor_files[new_image['Arm_armor']]:           
            return create_new_image()
        # if new_image['Weapon_mage_effect'] == "weapon_mage_effect-6":   
        #     return create_new_image()

    else:
        # Double Grip position, with Double Grip arms with Double Grip weapon
        if 'double' in arms_files[new_image['Arms']]:
            if not 'double' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()

            if not 'weapon_double_grip' in new_image['Weapon']:            
                return create_new_image()   

        
        # position One Hand with, One Arm, with Single Weapon
        if 'single' in arms_files[new_image['Arms']]:
            if not 'single' in arm_armor_files[new_image['Arm_armor']]:
                return create_new_image()
            if not 'weapon_one_hand' in new_image['Weapon']:          
                return create_new_image()
        else:
            # position Staff, with Staff Hand, with Staff Weapons
            if 'staff' in arms_files[new_image['Arms']]:  
                if not 'staff' in arm_armor_files[new_image['Arm_armor']]:
                    return create_new_image()
                if not 'weapon_staff' in new_image['Weapon']: 
                    return create_new_image()  
            else:
                # position Two Arms, with Two Arms, with Dual Wield Weapons
                if 'two' in arms_files[new_image['Arms']]:                     
                    if not 'two' in arm_armor_files[new_image['Arm_armor']]:
                        return create_new_image()
                    if not 'weapon_dual_wield' in new_image['Weapon']:
                        return create_new_image()
 
    # HELMETS can only be put on BATTLE ARMORS (not enclosed armors or helmetless explorer/observer)
    # if 'Helmet' in head_pieces_files[new_image['Head_pieces']]:
    #     if 'enclosed_armors' in new_image['Battle_armors']:
    #         return create_new_image()
    #     if not ('short' in hair_files[new_image['Hair']] or 'lizard' in hair_files[new_image['Hair']]):
    #         return create_new_image()

    # Mage hood is added onto HELMETLESS Explorer or Observer suits, and must have NO HELM 
    if not 'No hood#78' in mage_hoods_files[new_image['Mage_hoods']] and 'mage' in mage_hoods_files[new_image['Mage_hoods']]:
        if 'blue' in mage_hoods_files[new_image['Mage_hoods']] or 'green' in mage_hoods_files[new_image ["Mage_hoods"]]:
            new_image ['Helm_backpieces'] = 'helm_backpieces-2'
        if 'gold' in mage_hoods_files[new_image['Mage_hoods']] or 'purple' in mage_hoods_files[new_image['Mage_hoods']]:
            new_image['Helm_backpieces'] = 'helm_backpieces-3'
        if 'red' in mage_hoods_files[new_image['Mage_hoods']] or 'silver' in mage_hoods_files[new_image['Mage_hoods']]:
            new_image['Helm_backpieces'] = 'helm_backpieces-4'
        if not 'helmetless' in battle_armors_files[new_image['Battle_armors']]:
            return create_new_image()

    # Mage hoods CAN ONLY have short unkept or short bun hairs
    if new_image["Mage_hoods"] != "mage_hoods-7":       
        if not 'short' in hair_files[new_image['Hair']]:
           return create_new_image()

    # Mage hand CAN ONLY be with mage hood 
    
    if 'mage hand' in arms_files[new_image['Arms']]:
        new_image['Weapon'] = 'no_weapon'
        if 'enclosed_armors' in new_image['Battle_armors'] or not 'helmetless explorer' in battle_armors_files[new_image['Battle_armors']]:
            return create_new_image()
        # if  new_image ["Weapon_mage_effect"] == 'weapon_mage_effect-6':
        #     return create_new_image()
        if  new_image ["Mage_hoods"] == 'mage_hoods-7':
            return create_new_image()
        
    # else:
    #     new_image ["Weapon_mage_effect"] = 'weapon_mage_effect-6'



    # other exception
    if 'enclosed_armors' in new_image['Battle_armors']:
        if not 'short' in hair_files[new_image['Hair']] or 'fluffy' in beards_files[new_image['Beards']]:
            return create_new_image() 

    # mage staff with only mage hood
    if 'staff' in weapon_files[new_image['Weapon']]:
        if 'No hood#78' in mage_hoods_files[new_image['Mage_hoods']]:
            return create_new_image() 

    # no armours ALWAYS has a tattoo
    if 'no_battle_armors' in battle_armors_files[new_image['Battle_armors']]:
        if 'no_tattoos' in tattoos_files[new_image['Tattoos']]:
            return create_new_image()

    # thunder tattoo always have thunder warpaint
    if 'thunder' in war_paint_files[new_image['War_paint']]:
        if not 'thunder' in tattoos_files[new_image['Tattoos']]:
            return create_new_image()

    if  new_image in all_images:
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

# print(all_images)

# # Get Trait Counts
# background_count = {}
# for item in background:
#     background_count[item] = 0
    
# weapon_back_count = {}
# for item in weapon_back:
#     weapon_back_count[item] = 0

# helm_backpieces_count = {}
# for item in helm_backpieces:
#     helm_backpieces_count[item] = 0

# armor_back_pieces_count = {}
# for item in armor_back_pieces:
#     armor_back_pieces_count[item] = 0

# base_body_count = {}
# for item in base_body:
#     base_body_count[item] = 0

# tattoos_count = {}
# for item in tattoos:
#     tattoos_count[item] = 0

# battle_armors_count = {}
# for item in battle_armors:
#     battle_armors_count[item] = 0 

# scars_count = {}
# for item in scars:
#     scars_count[item] = 0

# facial_expressions_count = {}
# for item in facial_expressions:
#     facial_expressions_count[item] = 0

# war_paint_count = {}
# for item in war_paint:
#     war_paint_count[item] = 0

# eyebrows_count = {}
# for item in eyebrows:
#     eyebrows_count[item] = 0

# hair_count = {}
# for item in hair:
#     hair_count[item] = 0

# mage_hoods_count = {}
# for item in mage_hoods:
#     mage_hoods_count[item] = 0

# beards_count = {}
# for item in beards:
#     beards_count[item] = 0

# arms_count = {}
# for item in arms:
#     arms_count[item] = 0

# weapon_count = {}
# for item in weapon:
#     weapon_count[item] = 0

# arm_armor_count = {}
# for item in arm_armor:
#     arm_armor_count[item] = 0

# weapon_mage_effect_count = {}
# for item in weapon_mage_effect:
#     weapon_mage_effect_count[item] = 0

# extras_count = {}
# for item in extras:
#     extras_count[item] = 0

# head_pieces_count = {}
# for item in head_pieces:
#     head_pieces_count[item] = 0

# for image in all_images:
#     background_count[image["Background"]] += 1
#     weapon_back_count[image["Weapon_back"]] += 1
#     helm_backpieces_count[image["Helm_backpieces"]] += 1
#     armor_back_pieces_count[image["Armor_back_pieces"]] += 1
#     base_body_count[image["Base_body"]] += 1
#     tattoos_count[image["Tattoos"]] += 1
#     battle_armors_count[image["Battle_armors"]] += 1
#     scars_count[image["Scars"]] += 1    
#     facial_expressions_count[image["Facial_expressions"]] += 1
#     war_paint_count[image["War_paint"]] += 1    
#     eyebrows_count[image["Eyebrows"]] += 1
#     hair_count[image["Hair"]] += 1
#     mage_hoods_count[image["Mage_hoods"]] += 1
#     beards_count[image["Beards"]] += 1
#     arms_count[image["Arms"]] += 1
#     weapon_count[image["Weapon"]] += 1
#     arm_armor_count[image["Arm_armor"]] += 1
#     weapon_mage_effect_count[image["Weapon_mage_effect"]] += 1
#     extras_count[image["Extras"]] += 1
#     head_pieces_count[image["Head_pieces"]] += 1


    
# print(background_count)
# print(weapon_back_count)
# print(helm_backpieces_count)
# print(armor_back_pieces_count)
# print(base_body_count)
# print(tattoos_count)
# print(battle_armors_count)
# print(scars_count)
# print(facial_expressions_count)
# print(war_paint_count)
# print(eyebrows_count)
# print(hair_count)
# print(mage_hoods_count)
# print(beards_count)
# print(arms_count)
# print(weapon_count)
# print(arm_armor_count)
# print(weapon_mage_effect_count)
# print(extras_count)
# print(head_pieces_count)

#### Generate Metadata for all Traits 
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)

#### Generate Images    
for item in all_images:
    im1 = Image.open(f'./trait-layers/1. BACKGROUNDS/{background_files[item["Background"]]}.png').convert('RGBA')
    im3 = Image.open(f'./trait-layers/3. HELM BACKPIECES/{helm_backpieces_files[item["Helm_backpieces"]]}.png').convert('RGBA')
    im4 = Image.open(f'./trait-layers/4. ARMOR BACK PIECES/{armor_back_pieces_files[item["Armor_back_pieces"]]}.png').convert('RGBA')
    im5 = Image.open(f'./trait-layers/5. BASE BODY/{base_body_files[item["Base_body"]]}.png').convert('RGBA')
    im6 = Image.open(f'./trait-layers/6. TATTOOS/{tattoos_files[item["Tattoos"]]}.png').convert('RGBA')
    im7 = Image.open(f'./trait-layers/9. FACIAL EXPRESSIONS/{facial_expressions_files[item["Facial_expressions"]]}.png').convert('RGBA')
    im8 = Image.open(f'./trait-layers/10. WAR PAINT/{war_paint_files[item["War_paint"]]}.png').convert('RGBA')
    im9 = Image.open(f'./trait-layers/12. HAIR/{hair_files[item["Hair"]]}.png').convert('RGBA')    
    im10 = Image.open(f'./trait-layers/8. SCARS/{scars_files[item["Scars"]]}.png').convert('RGBA')
    im11 = Image.open(f'./trait-layers/11. EYEBROWS/{eyebrows_files[item["Eyebrows"]]}.png').convert('RGBA')
    im12 = Image.open(f'./trait-layers/14. BEARDS/{beards_files[item["Beards"]]}.png').convert('RGBA')
    im13 = Image.open(f'./trait-layers/7. BATTLE ARMORS/{battle_armors_files[item["Battle_armors"]]}.png').convert('RGBA')  
    im14 = Image.open(f'./trait-layers/13. MAGE HOODS/{mage_hoods_files[item["Mage_hoods"]]}.png').convert('RGBA')
    im15 = Image.open(f'./trait-layers/15. ARMS/{arms_files[item["Arms"]]}.png').convert('RGBA')
    im16 = Image.open(f'./trait-layers/16. EXTRAS/{extras_files[item["Extras"]]}.png').convert('RGBA')
    im17 = Image.open(f'./trait-layers/18. WEAPON/{weapon_files[item["Weapon"]]}.png').convert('RGBA')
    im18 = Image.open(f'./trait-layers/19. ARM ARMOR/{arm_armor_files[item["Arm_armor"]]}.png').convert('RGBA')
    # im19 = Image.open(f'./trait-layers/20. WEAPON MAGE EFFECT/{weapon_mage_effect_files[item["Weapon_mage_effect"]]}.png').convert('RGBA')
    # im20 = Image.open(f'./trait-layers/21. HEAD PIECES/{head_pieces_files[item["Head_pieces"]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im3)
       

    if  'weapon_one_hand-back' in item['Weapon']:
        print('weapon_back')
        com1 = Image.alpha_composite(im1, im17)
        com2 = Image.alpha_composite(im4, im5)   
        com3 = Image.alpha_composite(im6, im7)
        com4 = Image.alpha_composite(im8, im9) 
        com5 = Image.alpha_composite(im10, im11)
    

        if 'enclosed_armors' in item['Battle_armors']:
            com6 = Image.alpha_composite(im12, im13)
        else:
            com6 = Image.alpha_composite(im13, im12) 

        
       # Mage hand CAN ONLY be with mage hood 
        if 'mage' in item['Arms'] and  'helmetless' in item['Battle_armors']:
            com7 = Image.alpha_composite(im13, im14)
        else:
            com7 = Image.alpha_composite(im15, im15) 

        com8 = Image.alpha_composite(im15, im15)
        
        # in case enclosed armos except laster
        if 'laser' in item['Extras'] and 'enclosed armors' in item['Battle_armors']:
            com9 = Image.alpha_composite(im16, im16)
        else:
            com9 = Image.alpha_composite(im15, im15)  


        if not 'no_battle_armors' in item['Battle_armors']:
            com10 = Image.alpha_composite(im18, im18)
        else:
            com10 = Image.alpha_composite(im15, im15)
    

        com11 = Image.alpha_composite(com1, com2)
        com12 = Image.alpha_composite(com3, com4)
        com13 = Image.alpha_composite(com5, com6)
        com14 = Image.alpha_composite(com7, com8)
        com15 = Image.alpha_composite(com9, com10)      
        com16 = Image.alpha_composite(com11, com12)    
        com17 = Image.alpha_composite(com13, com14)
        com18 = Image.alpha_composite(com14, com15)
        com19 = Image.alpha_composite(com16, com16)
        com20 = Image.alpha_composite(com17, com18)
        com21 = Image.alpha_composite(com19, com20)

        #Convert to RGB
        rgb_im = com21.convert('RGBA')

    else:
        com2 = Image.alpha_composite(im4, im5)   
        com3 = Image.alpha_composite(im6, im7)
        com4 = Image.alpha_composite(im8, im9) 
        com5 = Image.alpha_composite(im10, im11)
    

        if 'enclosed_armors' in item['Battle_armors']:
            com6 = Image.alpha_composite(im12, im13)
        else:
            com6 = Image.alpha_composite(im13, im12) 

        
        # Mage hand CAN ONLY be with mage hood 
        if 'mage' in item['Arms'] and  'helmetless' in item['Battle_armors']:
            print('mage hood')
            com7 = Image.alpha_composite(im13, im14)
        else:
            com7 = Image.alpha_composite(im17, im17) 

        com8 = Image.alpha_composite(im17, im17)
        
        # in case enclosed armos except laster
        if 'laser' in item['Extras'] and 'enclosed armors' in item['Battle_armors']:
            com9 = Image.alpha_composite(im16, im15)
        else:
            com9 = Image.alpha_composite(im15, im15)  

        if not 'no_battle_armors' in item['Battle_armors']:
            com10 = Image.alpha_composite(im18, im18)
        else:
            com10 = Image.alpha_composite(im15, im15)
    

        com11 = Image.alpha_composite(com1, com2)
        com12 = Image.alpha_composite(com3, com4)
        com13 = Image.alpha_composite(com5, com6)
        com14 = Image.alpha_composite(com7, com8)
        com15 = Image.alpha_composite(com9, com10)
        com16 = Image.alpha_composite(com11, com12)    
        com17 = Image.alpha_composite(com13, com14)
        com18 = Image.alpha_composite(com14, com15)
        com19 = Image.alpha_composite(com16, com17)
        com20 = Image.alpha_composite(com17, com18)
        com21 = Image.alpha_composite(com19, com20)

        #Convert to RGB
        rgb_im = com21.convert('RGBA')
    
        

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
    token["attributes"].append(getAttribute("Background", i["Background"]))
    # token["attributes"].append(getAttribute("Weapon_back", i["Weapon_back"]))
    token["attributes"].append(getAttribute("Helm_backpieces", i["Helm_backpieces"]))
    token["attributes"].append(getAttribute("Armor_back_pieces", i["Armor_back_pieces"]))
    token["attributes"].append(getAttribute("Base_body", i["Base_body"]))
    token["attributes"].append(getAttribute("Tattoos", i["Tattoos"]))
    token["attributes"].append(getAttribute("Battle_armors", i["Battle_armors"]))
    token["attributes"].append(getAttribute("Scars", i["Scars"]))
    token["attributes"].append(getAttribute("Facial_expressions", i["Facial_expressions"]))
    token["attributes"].append(getAttribute("War_paint", i["War_paint"]))
    token["attributes"].append(getAttribute("Hair", i["Hair"]))
    token["attributes"].append(getAttribute("Mage_hoods", i["Mage_hoods"]))
    token["attributes"].append(getAttribute("Beards", i["Beards"]))
    token["attributes"].append(getAttribute("Arms", i["Arms"]))
    token["attributes"].append(getAttribute("Weapon", i["Weapon"]))
    token["attributes"].append(getAttribute("Arm_armor", i["Arm_armor"]))
    # token["attributes"].append(getAttribute("Weapon_mage_effect", i["Weapon_mage_effect"]))
    token["attributes"].append(getAttribute("Extras", i["Extras"]))
    # token["attributes"].append(getAttribute("Head_pieces", i["Head_pieces"]))
                            
    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()