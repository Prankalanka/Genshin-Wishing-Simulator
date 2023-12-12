import random
import numpy as np
from my_functions import clear
from inventory import (
    fo_names,
    item_dict,
    item_inv,
    fo_chars,
    fi_chars,
    th_names,
    sta_fi,
    sta_fo,
    sta_fi_wep,
)

# Next Steps: Update to latest version, Make more user friendly

# variables
banner_no = 38
soft_pity_char = 75
soft_pity_weap = 65
base = 497 / 75  # how much a five star's chance increases by each pull after soft pity
# colours
gold = "\033[38;5;11m"
purple = "\033[38;5;164m"
white = "\033[38;5;231m"
blue = "\033[0;34m"


class Banner:
    def __init__(self, lim_fi, lim_fo, soft_pity):
        self.lim_fi = lim_fi
        self.lim_fo = list(lim_fo[0])
        self.soft_pity = soft_pity
        self.pity = [
            0,
            0,
        ]  # stores how many pulls it has been since a five and four star
        self.fi_weight = [0.6, 99.4]  # first no. is percent chance of five star
        self.fo_weight = [5, 95]  # first no. is percent chance of four star
        self.fi_fifty = "lost"
        self.fo_fifty = "lost"
        self.fi_roll_res = 0  # the result of the five star roll
        self.fo_roll_res = 0  # the result of the four star roll

    # Gives a fifty percent chance of the limited character (lost) and standard (won)
    def fiftyfifty(self):
        fifty = ["won", "lost"]
        if self.fi_roll_res == self.fi_weight[0]:
            self.fi_fifty = random.choice(fifty)
        if self.fo_roll_res == self.fo_weight[0]:
            self.fo_fifty = random.choice(fifty)

    # changes weight depending on how many pulls it has been since a five/four star
    def weight_changer(self, pity):
        if pity[0] > self.soft_pity:
            self.fi_weight[0] += base
            self.fi_weight[1] = 100 - self.fi_weight[0]
        if pity[0] < self.soft_pity:
            self.fi_weight[0] = 0.6
            self.fi_weight[1] = 99.4
        if pity[1] == 8:
            self.fo_weight[0] = 50
            self.fo_weight[1] = 50
        if pity[1] < 8:
            self.fo_weight[0] = 5
            self.fo_weight[1] = 95
        if pity[1] >= 9:
            self.fo_weight[0] = 100
            self.fo_weight[1] = 0
        #print(self.fi_weight, self.fo_weight)

    # Main thing that processes the ability to pull
    def process(self):
        # rolls for a five and four star and stores it in fi_roll_res and fo_roll_res
        fo_roll = random.choices(
            self.fo_weight, weights=(self.fo_weight[0], self.fo_weight[1])
        )
        fi_roll = random.choices(
            self.fi_weight, weights=(self.fi_weight[0], self.fi_weight[1])
        )
        self.fo_roll_res = fo_roll[0]
        self.fi_roll_res = fi_roll[0]

            
        # displays and adds to inventory the pull giving prio to five stars
        if self.fi_roll_res == self.fi_weight[0] and self.fi_fifty == "lost":
            # we add it to the inventory now using dicts
                
            if type(self.lim_fi) != list:  # if item is character
                fi_item = self.lim_fi
            else:  # if item is an item
                fi_item = random.choice(self.lim_fi)
                    
            item_inv.add_item(item_dict[fi_item], 1)
            print(gold, fi_item, "It took", self.pity[0] + 1, "pulls", white)
            self.fi_fifty = "won"
            self.pity[0] = -1
            self.fiftyfifty()

                    
        elif self.fi_roll_res == self.fi_weight[0] and self.fi_fifty == "won":
            if self.lim_fi in fi_chars:
                fi_item = random.choice(sta_fi)
            if type(self.lim_fi) == list:
                fi_item = random.choice(sta_fi_wep)
                
            item_inv.add_item(item_dict[fi_item], 1)
            print(gold, fi_item, "It took", self.pity[0] + 1, "pulls", white)
            self.pity[0] = -1
            self.fi_fifty = "lost"

                    
        elif self.fo_roll_res == self.fo_weight[0] and self.fo_fifty == "lost":
            fo_item = fo_names[random.choice(self.lim_fo)]
            item_inv.add_item(item_dict[fo_item], 1)
            print(purple, fo_item, white)
            self.pity[1] = -1
            self.fo_fifty = "won"
            self.fiftyfifty()

                
        elif self.fo_roll_res == self.fo_weight[0] and self.fo_fifty == "won":
            fo_item = random.choice(sta_fo)
            item_inv.add_item(item_dict[fo_item], 1)
            print(purple, fo_item, white)
            self.pity[1] = -1
            self.fo_fifty = "lost"

                
        elif self.fi_roll_res != 5 and self.fo_roll_res != 4:
            th_item = random.choice(th_names)
            item_inv.add_item(item_dict[th_item], 1)
            print(blue, th_item, white)

    # the entire process of a pull ordered and in one function
    def pull(self):
        self.pity[0] += 1
        self.pity[1] += 1
        self.weight_changer(self.pity)
        self.process()


# Character Banner Instances (Manual Labour)
BiG_banner = Banner(
    "Venti",
    np.where(np.isin(fo_names, ["Xiangling", "Barbara", "Fischl"])),
    soft_pity_char,
)
SpSt_banner = Banner(
    "Klee", np.where(np.isin(fo_names, ["Xinqiu", "Sucrose", "Noelle"])), soft_pity_char
)
FoS_banner = Banner(
    "Tartaglia",
    np.where(np.isin(fo_names, ["Beidou", "Diona", "Ningguang"])),
    soft_pity_char,
)
GoH_banner = Banner(
    "Zhongli",
    np.where(np.isin(fo_names, ["Xinyan", "Chongyun", "Razor"])),
    soft_pity_char,
)
SeSe_banner = Banner(
    "Albedo",
    np.where(np.isin(fo_names, ["Fischl", "Bennet", "Sucrose"])),
    soft_pity_char,
)
AitH_banner = Banner(
    "Ganyu",
    np.where(np.isin(fo_names, ["Xiangling", "Xinqiu", "Noelle"])),
    soft_pity_char,
)
ItML_banner = Banner(
    "Xiao", np.where(np.isin(fo_names, ["Xinyan", "Diona", "Beidou"])), soft_pity_char
)
DoL_banner = Banner(
    "Keqing",
    np.where(np.isin(fo_names, ["Ningguang", "Barbara", "Bennet"])),
    soft_pity_char,
)
MoB_banner = Banner(
    "Hu Tao",
    np.where(np.isin(fo_names, ["Xiangling", "Xinqiu", "Chongyun"])),
    soft_pity_char,
)
BiG2_banner = Banner(
    "Venti", np.where(np.isin(fo_names, ["Sucrose", "Razor", "Noelle"])), soft_pity_char
)
FoS2_banner = Banner(
    "Tartaglia",
    np.where(np.isin(fo_names, ["Rosaria", "Barbara", "Fischl"])),
    soft_pity_char,
)
GoH2_banner = Banner(
    "Zhongli",
    np.where(np.isin(fo_names, ["Noelle", "Yanfei", "Diona"])),
    soft_pity_char,
)
BoOS_banner = Banner(
    "Eula", np.where(np.isin(fo_names, ["Beidou", "Xinyan", "Xinqiu"])), soft_pity_char
)
SpSt2_banner = Banner(
    "Klee",
    np.where(np.isin(fo_names, ["Sucrose", "Barbara", "Fischl"])),
    soft_pity_char,
)
LitW_banner = Banner(
    "Kaedehara Kazuha",
    np.where(np.isin(fo_names, ["Rosaria", "Razor", "Bennet"])),
    soft_pity_char,
)
THC_banner = Banner(
    "Kamisato Ayaka",
    np.where(np.isin(fo_names, ["Chongyun", "Ningguang", "Yanfei"])),
    soft_pity_char,
)
ToGF_banner = Banner(
    "Yoimiya", np.where(np.isin(fo_names, ["Diona", "Sayu", "Xinyan"])), soft_pity_char
)
RoS_banner = Banner(
    "Raiden Shogun",
    np.where(np.isin(fo_names, ["Xiangling", "Kujou Sara", "Sucrose"])),
    soft_pity_char,
)

# Weapon Banner Instances (Manual Labour)

EI10a_banner = Banner(
    ["Amos' Bow", "Aquila Favonia"],
    np.where(
        np.isin(
            fo_names,
            [
                "The Bell",
                "The Flute",
                "Favonius Lance",
                "The Stringless",
                "The Widsith",
            ],
        )
    ),
    soft_pity_weap,
)

EI10b_banner = Banner(
    ["Lost Prayer To The Sacred Winds", "Wolf's Gravestone"],
    np.where(
        np.isin(
            fo_names,
            [
                "Dragon's Bane",
                "Sacrificial Bow",
                "Sacrificial Fragments",
                "Sacrificial Sword",
                "Sacrificial Greatsword",
            ],
        )
    ),
    soft_pity_weap,
)

EI11a_banner = Banner(
    ["Skyward Harp", "Memory of Dust"],
    np.where(
        np.isin(
            fo_names,
            ["Rust", "The Flute", "Favonius Lance", "Rainslasher", "Eye of Perception"],
        )
    ),
    soft_pity_weap,
)

EI11b_banner = Banner(
    ["Vortex Vanquisher", "The Unforged"],
    np.where(
        np.isin(
            fo_names,
            [
                "The Bell",
                "Favonius Warbow",
                "Favonius Codex",
                "Lion's Roar",
                "Dragon's Bane",
            ],
        )
    ),
    soft_pity_weap,
)

EI12a_banner = Banner(
    ["Summit Shaper", "Skyward Atlas"],
    np.where(
        np.isin(
            fo_names,
            [
                "Favonius Sword",
                "Favonius Greatsword",
                "Favonius Lance",
                "The Stringless",
                "Sacrificial Fragments",
            ],
        )
    ),
    soft_pity_weap,
)

EI12b_banner = Banner(
    ["Amos' Bow", "Skyward Pride"],
    np.where(
        np.isin(
            fo_names,
            [
                "The Bell",
                "Dragon's Bane",
                "Eye of Perception",
                "Favonius Warbow",
                "Sacrificial Sword",
            ],
        )
    ),
    soft_pity_weap,
)

EI13a_banner = Banner(
    ["Primordial Jade Winged-Spear", "Primordial Jade Cutter"],
    np.where(
        np.isin(
            fo_names,
            [
                "Sacrificial Greatsword",
                "The Flute",
                "Favonius Lance",
                "Rust",
                "Eye of Perception",
            ],
        )
    ),
    soft_pity_weap,
)

EI13b_banner = Banner(
    ["Staff of Homa", "Wolf's Gravestone"],
    np.where(
        np.isin(
            fo_names,
            [
                "Lithic Blade",
                "Lion's Roar",
                "Lithic Spear",
                "Sacrificial Bow",
                "The Widsith",
            ],
        )
    ),
    soft_pity_weap,
)

EI14a_banner = Banner(
    ["Elegy for the End", "Skyward Blade"],
    np.where(
        np.isin(
            fo_names,
            [
                "Favonius Greatsword",
                "The Alley Flash",
                "Dragon's Bane",
                "Favonius Warbow",
                "Wine and Song",
            ],
        )
    ),
    soft_pity_weap,
)

EI14b_banner = Banner(
    ["Skyward Harp", "Lost Prayer To The Sacred Winds"],
    np.where(
        np.isin(
            fo_names,
            [
                "Sacrificial Greatsword",
                "Favonius Sword",
                "Favonius Lance",
                "Alley Hunter",
                "Favonius Codex",
            ],
        )
    ),
    soft_pity_weap,
)

EI15a_banner = Banner(
    ["Summit Shaper", "Memory of Dust"],
    np.where(
        np.isin(
            fo_names,
            [
                "Lithic Blade",
                "The Flute",
                "Lithic Spear",
                "Sacrificial Bow",
                "Eye of Perception",
            ],
        )
    ),
    soft_pity_weap,
)

EI15b_banner = Banner(
    ["Song of Broken Pines", "Aquila Favonia"],
    np.where(
        np.isin(
            fo_names,
            [
                "Rainslasher",
                "Sacrificial Sword",
                "Dragon's Bane",
                "Rust",
                "Sacrificial Fragments",
            ],
        )
    ),
    soft_pity_weap,
)

EI16a_banner = Banner(
    ["Lost Prayer To The Sacred Winds", "Skyward Pride"],
    np.where(
        np.isin(
            fo_names,
            [
                "The Bell",
                "Lion's Roar",
                "Favonius Lance",
                "Mitternachts Waltz",
                "The Widsith",
            ],
        )
    ),
    soft_pity_weap,
)

EI16b_banner = Banner(
    ["Freedom-Sworn", "Skyward Atlas"],
    np.where(
        np.isin(
            fo_names,
            [
                "Favonius Greatsword",
                "The Alley Flash",
                "Dragon's Bane",
                "Alley Hunter",
                "Wine and Song",
            ],
        )
    ),
    soft_pity_weap,
)

EI20a_banner = Banner(
    ["The Mistsplitter", "Skyward Spine"],
    np.where(
        np.isin(
            fo_names,
            [
                "Sacrificial Greatsword",
                "Favonius Sword",
                "Favonius Lance",
                "The Stringless",
                "Favonius Codex",
            ],
        )
    ),
    soft_pity_weap,
)

EI20b_banner = Banner(
    ["Thundering Pulse", "Skyward Blade"],
    np.where(
        np.isin(
            fo_names,
            [
                "Rainslasher",
                "Sacrificial Sword",
                "Dragon's Bane",
                "Favonius Warbow",
                "Sacrificial Fragments",
            ],
        )
    ),
    soft_pity_weap,
)

EI21a_banner = Banner(
    ["Engulfing Lightning", "The Unforged"],
    np.where(
        np.isin(
            fo_names,
            [
                "The Bell",
                "Lion's Roar",
                "Favonius Lance",
                "Sacrificial Bow",
                "The Widsith",
            ],
        )
    ),
    soft_pity_weap,
)

EI21b_banner = Banner(
    ["Everlasting Moonglow", "Primordial Jade Cutter"],
    np.where(
        np.isin(
            fo_names,
            [
                "Favonius Greatsword",
                "The Flute",
                "Dragon's Bane",
                "The Stringless",
                "Favonius Codex",
            ],
        )
    ),
    soft_pity_weap,
)

EI22a_banner = Banner(
    ["Polar Star", "Memory of Dust"],
    np.where(
        np.isin(
            fo_names,
            [
                "Akoumaru",
                "Favonius Sword",
                "Favonius Lance",
                "Rust",
                "Eye of Perception",
            ],
        )
    ),
    soft_pity_weap,
)

EI22b_banner = Banner(
    ["Staff of Homa", "Elegy for the End"],
    np.where(
        np.isin(
            fo_names,
            [
                "Rainslasher",
                "Sacrificial Sword",
                "Wavebreaker's Fin",
                "Mouun's Moon",
                "The Widsith",
            ],
        )
    ),
    soft_pity_weap,
)

# banner dictionary
ban_dict = {
    1: BiG_banner,
    2: SpSt_banner,
    3: FoS_banner,
    4: GoH_banner,
    5: SeSe_banner,
    6: AitH_banner,
    7: ItML_banner,
    8: DoL_banner,
    9: MoB_banner,
    10: BiG2_banner,
    11: FoS2_banner,
    12: GoH2_banner,
    13: BoOS_banner,
    14: SpSt2_banner,
    15: LitW_banner,
    16: THC_banner,
    17: ToGF_banner,
    18: RoS_banner,
    19: EI10a_banner,
    20: EI10b_banner,
    21: EI11a_banner,
    22: EI11b_banner,
    23: EI12a_banner,
    24: EI12b_banner,
    25: EI13a_banner,
    26: EI13b_banner,
    27: EI14a_banner,
    28: EI14b_banner,
    29: EI15a_banner,
    30: EI15b_banner,
    31: EI16a_banner,
    32: EI16b_banner,
    33: EI20a_banner,
    34: EI20b_banner,
    35: EI21a_banner,
    36: EI21b_banner,
    37: EI22a_banner,
    38: EI22b_banner,
}

# Functions


# asks the user how many pulls they want and calls for pull to do that many
def input_pull(banner):
    number = input(
        "Input 0 to switch. \nHow many pulls?"
    )
    try:
        if int(number) == 0:
            clear()
            ban_select()
        elif int(number) > 0:
            number = int(number)
            for i in range(int(number)):
                banner.pull()
            input_pull(banner)
        elif int(number) < 0:
            print("Input valid number.")
            input_pull(banner)
    except ValueError:
        print("Input valid number.")
        input_pull(banner)


# selects banners (Manual Labour)
def ban_select():

    print(
        "1.Ballad in Goblets:",
        gold,
        "\n",
        BiG_banner.lim_fi,
        purple,
        "\n",
        fo_names[BiG_banner.lim_fo[0]],
        "\n",
        fo_names[BiG_banner.lim_fo[1]],
        "\n",
        fo_names[BiG_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "2.Sparkling Steps:",
        gold,
        "\n",
        SpSt_banner.lim_fi,
        purple,
        "\n",
        fo_names[SpSt_banner.lim_fo[0]],
        "\n",
        fo_names[SpSt_banner.lim_fo[1]],
        "\n",
        fo_names[SpSt_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "3.Farewell of Snezhnaya:",
        gold,
        "\n",
        FoS_banner.lim_fi,
        purple,
        "\n",
        fo_names[FoS_banner.lim_fo[0]],
        "\n",
        fo_names[FoS_banner.lim_fo[1]],
        "\n",
        fo_names[FoS_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "4.Gentry of Hermitage:",
        gold,
        "\n",
        GoH_banner.lim_fi,
        purple,
        "\n",
        fo_names[GoH_banner.lim_fo[0]],
        "\n",
        fo_names[GoH_banner.lim_fo[1]],
        "\n",
        fo_names[GoH_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "5.Secret Secretorum",
        gold,
        "\n",
        SeSe_banner.lim_fi,
        purple,
        "\n",
        fo_names[SeSe_banner.lim_fo[0]],
        "\n",
        fo_names[SeSe_banner.lim_fo[1]],
        "\n",
        fo_names[SeSe_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "6.Adrift in the Harbor:",
        gold,
        "\n",
        AitH_banner.lim_fi,
        purple,
        "\n",
        fo_names[AitH_banner.lim_fo[0]],
        "\n",
        fo_names[AitH_banner.lim_fo[1]],
        "\n",
        fo_names[AitH_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "7.Invitation to Mundane Life:",
        gold,
        "\n",
        ItML_banner.lim_fi,
        purple,
        "\n",
        fo_names[ItML_banner.lim_fo[0]],
        "\n",
        fo_names[ItML_banner.lim_fo[1]],
        "\n",
        fo_names[ItML_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "8.Dance of Lanterns:",
        gold,
        "\n",
        DoL_banner.lim_fi,
        purple,
        "\n",
        fo_names[DoL_banner.lim_fo[0]],
        "\n",
        fo_names[DoL_banner.lim_fo[1]],
        "\n",
        fo_names[DoL_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "9.Moment of Bloon:",
        gold,
        "\n",
        MoB_banner.lim_fi,
        purple,
        "\n",
        fo_names[MoB_banner.lim_fo[0]],
        "\n",
        fo_names[MoB_banner.lim_fo[1]],
        "\n",
        fo_names[MoB_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "10.Ballad in Goblets (Rerun):",
        gold,
        "\n",
        BiG2_banner.lim_fi,
        purple,
        "\n",
        fo_names[BiG2_banner.lim_fo[0]],
        "\n",
        fo_names[BiG2_banner.lim_fo[1]],
        "\n",
        fo_names[BiG2_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "11.Farewell of Snezhnaya (Rerun):",
        gold,
        "\n",
        FoS2_banner.lim_fi,
        purple,
        "\n",
        fo_names[FoS2_banner.lim_fo[0]],
        "\n",
        fo_names[FoS2_banner.lim_fo[1]],
        "\n",
        fo_names[FoS2_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "12.Gentry of Hermitage (Rerun):",
        gold,
        "\n",
        GoH2_banner.lim_fi,
        purple,
        "\n",
        fo_names[GoH2_banner.lim_fo[0]],
        "\n",
        fo_names[GoH2_banner.lim_fo[1]],
        "\n",
        fo_names[GoH2_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "13.Born of Ocean Swell:",
        gold,
        "\n",
        BoOS_banner.lim_fi,
        purple,
        "\n",
        fo_names[BoOS_banner.lim_fo[0]],
        "\n",
        fo_names[BoOS_banner.lim_fo[1]],
        "\n",
        fo_names[BoOS_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "14.Sparkling Steps (Rerun):",
        gold,
        "\n",
        SpSt2_banner.lim_fi,
        purple,
        "\n",
        fo_names[SpSt2_banner.lim_fo[0]],
        "\n",
        fo_names[SpSt2_banner.lim_fo[1]],
        "\n",
        fo_names[SpSt2_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "15.Leaves in the Wind:",
        gold,
        "\n",
        LitW_banner.lim_fi,
        purple,
        "\n",
        fo_names[LitW_banner.lim_fo[0]],
        "\n",
        fo_names[LitW_banner.lim_fo[1]],
        "\n",
        fo_names[LitW_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "16.The Heron's Court:",
        gold,
        "\n",
        THC_banner.lim_fi,
        purple,
        "\n",
        fo_names[THC_banner.lim_fo[0]],
        "\n",
        fo_names[THC_banner.lim_fo[1]],
        "\n",
        fo_names[THC_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "17.Tapestry of Golden Flames:",
        gold,
        "\n",
        ToGF_banner.lim_fi,
        purple,
        "\n",
        fo_names[ToGF_banner.lim_fo[0]],
        "\n",
        fo_names[ToGF_banner.lim_fo[1]],
        "\n",
        fo_names[ToGF_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "18.Reign of Serenity:",
        gold,
        "\n",
        RoS_banner.lim_fi,
        purple,
        "\n",
        fo_names[RoS_banner.lim_fo[0]],
        "\n",
        fo_names[RoS_banner.lim_fo[1]],
        "\n",
        fo_names[RoS_banner.lim_fo[2]],
        "\n",
        "\n",
        white,
    )

    print(
        "19.Epitome Invocation 1.0 A:",
        gold,
        "\n",
        EI10a_banner.lim_fi[0],
        "\n",
        EI10a_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI10a_banner.lim_fo[0]],
        "\n",
        fo_names[EI10a_banner.lim_fo[1]],
        "\n",
        fo_names[EI10a_banner.lim_fo[2]],
        "\n",
        fo_names[EI10a_banner.lim_fo[3]],
        "\n",
        fo_names[EI10a_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "20.Epitome Invocation 1.0 B:",
        gold,
        "\n",
        EI10b_banner.lim_fi[0],
        "\n",
        EI10b_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI10b_banner.lim_fo[0]],
        "\n",
        fo_names[EI10b_banner.lim_fo[1]],
        "\n",
        fo_names[EI10b_banner.lim_fo[2]],
        "\n",
        fo_names[EI10b_banner.lim_fo[3]],
        "\n",
        fo_names[EI10b_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "21.Epitome Invocation 1.1 A:",
        gold,
        "\n",
        EI11a_banner.lim_fi[0],
        "\n",
        EI11a_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI11a_banner.lim_fo[0]],
        "\n",
        fo_names[EI11a_banner.lim_fo[1]],
        "\n",
        fo_names[EI11a_banner.lim_fo[2]],
        "\n",
        fo_names[EI11a_banner.lim_fo[3]],
        "\n",
        fo_names[EI11a_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "22.Epitome Invocation 1.1 B:",
        gold,
        "\n",
        EI11b_banner.lim_fi[0],
        "\n",
        EI11b_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI11b_banner.lim_fo[0]],
        "\n",
        fo_names[EI11b_banner.lim_fo[1]],
        "\n",
        fo_names[EI11b_banner.lim_fo[2]],
        "\n",
        fo_names[EI11b_banner.lim_fo[3]],
        "\n",
        fo_names[EI11b_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "23.Epitome Invocation 1.2 A:",
        gold,
        "\n",
        EI12a_banner.lim_fi[0],
        "\n",
        EI12a_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI12a_banner.lim_fo[0]],
        "\n",
        fo_names[EI12a_banner.lim_fo[1]],
        "\n",
        fo_names[EI12a_banner.lim_fo[2]],
        "\n",
        fo_names[EI12a_banner.lim_fo[3]],
        "\n",
        fo_names[EI12a_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "24.Epitome Invocation 1.2 B:",
        gold,
        "\n",
        EI12b_banner.lim_fi[0],
        "\n",
        EI12b_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI12b_banner.lim_fo[1]],
        "\n",
        fo_names[EI12b_banner.lim_fo[2]],
        "\n",
        fo_names[EI12b_banner.lim_fo[3]],
        "\n",
        fo_names[EI12b_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "25.Epitome Invocation 1.3 A:",
        gold,
        "\n",
        EI13a_banner.lim_fi[0],
        "\n",
        EI13a_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI13a_banner.lim_fo[0]],
        "\n",
        fo_names[EI13a_banner.lim_fo[1]],
        "\n",
        fo_names[EI13a_banner.lim_fo[2]],
        "\n",
        fo_names[EI13a_banner.lim_fo[3]],
        "\n",
        fo_names[EI13a_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "26.Epitome Invocation 1.3 B:",
        gold,
        "\n",
        EI13b_banner.lim_fi[0],
        "\n",
        EI13b_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI13b_banner.lim_fo[0]],
        "\n",
        fo_names[EI13b_banner.lim_fo[1]],
        "\n",
        fo_names[EI13b_banner.lim_fo[2]],
        "\n",
        fo_names[EI13b_banner.lim_fo[3]],
        "\n",
        fo_names[EI13b_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "27.Epitome Invocation 1.4 A:",
        gold,
        "\n",
        EI14a_banner.lim_fi[0],
        "\n",
        EI14a_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI14a_banner.lim_fo[0]],
        "\n",
        fo_names[EI14a_banner.lim_fo[1]],
        "\n",
        fo_names[EI14a_banner.lim_fo[2]],
        "\n",
        fo_names[EI14a_banner.lim_fo[3]],
        "\n",
        fo_names[EI14a_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "28.Epitome Invocation 1.4 B:",
        gold,
        "\n",
        EI14b_banner.lim_fi[0],
        "\n",
        EI14b_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI14b_banner.lim_fo[0]],
        "\n",
        fo_names[EI14b_banner.lim_fo[1]],
        "\n",
        fo_names[EI14b_banner.lim_fo[2]],
        "\n",
        fo_names[EI14b_banner.lim_fo[3]],
        "\n",
        fo_names[EI14b_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "29.Epitome Invocation 1.5 A:",
        gold,
        "\n",
        EI15a_banner.lim_fi[0],
        "\n",
        EI15a_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI15a_banner.lim_fo[0]],
        "\n",
        fo_names[EI15a_banner.lim_fo[1]],
        "\n",
        fo_names[EI15a_banner.lim_fo[2]],
        "\n",
        fo_names[EI15a_banner.lim_fo[3]],
        "\n",
        fo_names[EI15a_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "30.Epitome Invocation 1.5 B:",
        gold,
        "\n",
        EI15b_banner.lim_fi[0],
        "\n",
        EI15b_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI15b_banner.lim_fo[0]],
        "\n",
        fo_names[EI15b_banner.lim_fo[1]],
        "\n",
        fo_names[EI15b_banner.lim_fo[2]],
        "\n",
        fo_names[EI15b_banner.lim_fo[3]],
        "\n",
        fo_names[EI15b_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "31.Epitome Invocation 1.6 A:",
        gold,
        "\n",
        EI16a_banner.lim_fi[0],
        "\n",
        EI16a_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI16a_banner.lim_fo[0]],
        "\n",
        fo_names[EI16a_banner.lim_fo[1]],
        "\n",
        fo_names[EI16a_banner.lim_fo[2]],
        "\n",
        fo_names[EI16a_banner.lim_fo[3]],
        "\n",
        fo_names[EI16a_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "32.Epitome Invocation 1.6 B:",
        gold,
        "\n",
        EI16b_banner.lim_fi[0],
        "\n",
        EI16b_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI16b_banner.lim_fo[0]],
        "\n",
        fo_names[EI16b_banner.lim_fo[1]],
        "\n",
        fo_names[EI16b_banner.lim_fo[2]],
        "\n",
        fo_names[EI16b_banner.lim_fo[3]],
        "\n",
        fo_names[EI16b_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "33.Epitome Invocation 2.0 A:",
        gold,
        "\n",
        EI20a_banner.lim_fi[0],
        "\n",
        EI20a_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI20a_banner.lim_fo[0]],
        "\n",
        fo_names[EI20a_banner.lim_fo[1]],
        "\n",
        fo_names[EI20a_banner.lim_fo[2]],
        "\n",
        fo_names[EI20a_banner.lim_fo[3]],
        "\n",
        fo_names[EI20a_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "34.Epitome Invocation 2.0 B:",
        gold,
        "\n",
        EI20b_banner.lim_fi[0],
        "\n",
        EI20b_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI20b_banner.lim_fo[0]],
        "\n",
        fo_names[EI20b_banner.lim_fo[1]],
        "\n",
        fo_names[EI20b_banner.lim_fo[2]],
        "\n",
        fo_names[EI20b_banner.lim_fo[3]],
        "\n",
        fo_names[EI20b_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "35.Epitome Invocation 2.1 A:",
        gold,
        "\n",
        EI21a_banner.lim_fi[0],
        "\n",
        EI21a_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI21a_banner.lim_fo[0]],
        "\n",
        fo_names[EI21a_banner.lim_fo[1]],
        "\n",
        fo_names[EI21a_banner.lim_fo[2]],
        "\n",
        fo_names[EI21a_banner.lim_fo[3]],
        "\n",
        fo_names[EI21a_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "36.Epitome Invocation 2.1 B:",
        gold,
        "\n",
        EI21b_banner.lim_fi[0],
        "\n",
        EI21b_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI21b_banner.lim_fo[0]],
        "\n",
        fo_names[EI21b_banner.lim_fo[1]],
        "\n",
        fo_names[EI21b_banner.lim_fo[2]],
        "\n",
        fo_names[EI21b_banner.lim_fo[3]],
        "\n",
        fo_names[EI21b_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "37.Epitome Invocation 2.2 A:",
        gold,
        "\n",
        EI22a_banner.lim_fi[0],
        "\n",
        EI22a_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI22a_banner.lim_fo[0]],
        "\n",
        fo_names[EI22a_banner.lim_fo[1]],
        "\n",
        fo_names[EI22a_banner.lim_fo[2]],
        "\n",
        fo_names[EI22a_banner.lim_fo[3]],
        "\n",
        fo_names[EI22a_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )

    print(
        "38.Epitome Invocation 2.2 B:",
        gold,
        "\n",
        EI22b_banner.lim_fi[0],
        "\n",
        EI22b_banner.lim_fi[1],
        purple,
        "\n",
        fo_names[EI22b_banner.lim_fo[0]],
        "\n",
        fo_names[EI22b_banner.lim_fo[1]],
        "\n",
        fo_names[EI22b_banner.lim_fo[2]],
        "\n",
        fo_names[EI22b_banner.lim_fo[3]],
        "\n",
        fo_names[EI22b_banner.lim_fo[4]],
        "\n",
        "\n",
        white,
    )
    print("Input 0 to go back.")

    selected_banner = input("Enter the number of your banner of choice.")
    try:
        if int(selected_banner) == 0:
            clear()
            menu()
        if 0 > int(selected_banner) or int(selected_banner) > banner_no:
            clear()
            print("Input valid number.")
            print("\n")
            ban_select()
        else:
            clear()
            input_pull(ban_dict[int(selected_banner)])
    except ValueError:
        clear()
        print("Input valid number")
        print("\n")
        ban_select()


# the general interface (maybe add an options option later)
def menu():
    print(
        """                              
 _____             _   _        _ _ _ _     _           
|   __|___ ___ ___| |_|_|___   | | | |_|___| |_ ___ ___ 
|  |  | -_|   |_ -|   | |   |  | | | | |_ -|   | -_|  _|
|_____|___|_|_|___|_|_|_|_|_|  |_____|_|___|_|_|___|_| 
             """
    )
    print("\n1. Select Banner")
    print("2. Print Items")
    option = input("Option:")
    if option == "1":
        clear()
        ban_select()
    if option == "2":
        clear()
        item_inv.print_items()
        back = input("Input any key to go back.")
        if back == "b":
            clear()
            menu()
        else:
            clear()
            menu()
    else:
        clear()
        menu()


# Run Code
menu()
