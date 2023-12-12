class Item:  # Should probably make weapons and characters a subclass of this item class
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class Char(Item):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        self.name = name
        self.amount = amount


class Weap(Item):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        self.name = name
        self.amount = amount


class ItemInv:
    def __init__(self):
        self.items = {}  # the dict in which items are held with their names as keys

    def add_item(self, item, amount):
        self.items[item.name] = item
        item.amount += amount

    def print_items(self):
        print("\t".join(["Name"]))
        for item in self.items.values():
            print("\t".join([str(x) for x in [item.name, item.amount]]))


# Lists (Manual Labour)

sta_fi = ["Diluc", "Mona", "Jean", "Qiqi", "Keqing"]

limited_fi = [
    "Albedo",
    "Eula",
    "Ganyu",
    "Hu Tao",
    "Klee",
    "Tartaglia",
    "Venti",
    "Xiao",
    "Zhongli",
    "Raiden Shogun",
]

th_names = [
    "Amber Catalyst",
    "Black Tassel",
    "Bloodtainted Greatsword",
    "Cool Steel",
    "Dark Iron Sword",
    "Debate Club",
    "Ebony Bow",
    "Emerald Orb",
    "Ferrous Shadow",
    "Fillet Blade",
    "Halberd",
    "Harbinger of Dawn",
    "Magic Guide",
    "Messenger",
    "Otherworldly Story",
    "Quartz",
    "Raven Bow",
    "Recurve Bow",
    "Sharpshooter's Oath",
    "Skyrider Greatsword",
    "Skyrider Sword",
    "Slingshot",
    "Thrilling Tales of Dragon Slayers",
    "Traveler's Handy Sword",
    "Twin Nephrite",
    "White Iron Greatsword",
    "White Tassel",
]
fo_names = [
    "Amber",
    "Lisa",
    "Kaeya",
    "Barbara",
    "Razor",
    "Bennet",
    "Noelle",
    "Sayu",
    "Kujou Sara",
    "Fischl",
    "Sucrose",
    "Beidou",
    "Ningguang",
    "Xiangling",
    "Xinqiu",
    "Chongyun",
    "Diona",
    "Xinyan",
    "Rosaria",
    "Yanfei",
    "Akoumaru",
    "Alley Hunter",
    "Dragon's Bane",
    "Eye of Perception",
    "Favonius Codex",
    "Favonius Greatsword",
    "Favonius Lance",
    "Favonius Sword",
    "Favonius Warbow",
    "Lion's Roar",
    "Lithic Blade",
    "Lithic Spear",
    "Mitternachts Waltz",
    "Mouun's Moon",
    "Rainslasher",
    "Rust",
    "Sacrificial Bow",
    "Sacrificial Fragments",
    "Sacrificial Greatsword",
    "Sacrificial Sword",
    "The Alley Flash",
    "The Bell",
    "The Flute",
    "The Stringless",
    "The Widsith",
    "Wavebreaker's Fin",
    "Wine and Song",
]
sta_fo = [
    "Amber",
    "Chongyun",
    "Diona",
    "Lisa",
    "Kaeya",
    "Barbara",
    "Razor",
    "Bennet",
    "Noelle",
    "Fischl",
    "Sucrose",
    "Beidou",
    "Kujou Sara",
    "Ningguang",
    "Sayu",
    "Xiangling",
    "Xinqiu",
    "Xinyan",
    "Rosaria",
    "Yanfei",
    "Dragon's Bane",
    "Eye of Perception",
    "Favonius Codex",
    "Favonius Greatsword",
    "Favonius Lance",
    "Favonius Sword",
    "Favonius Warbow",
    "Lion's Roar",
    "Rainslasher",
    "Rust",
    "Sacrificial Bow",
    "Sacrificial Fragments",
    "Sacrificial Greatsword",
    "Sacrificial Sword",
    "The Alley Flash",
    "The Bell",
    "The Flute",
    "The Stringless",
    "The Widsith",
]
fo_chars = fo_names[0:20]
fo_items = fo_names[20:]
fi_names = [
    "Albedo",
    "Diluc",
    "Eula",
    "Ganyu",
    "Hu Tao",
    "Jean",
    "Kaedehara Kazuha",
    "Kamisato Ayaka",
    "Keqing",
    "Klee",
    "Mona",
    "Qiqi",
    "Tartaglia",
    "Venti",
    "Xiao",
    "Zhongli",
    "Amos' Bow",
    "Aquila Favonia",
    "Elegy for the End",
    "Lost Prayer to the Sacred Winds",
    "Memory of Dust",
    "Primordial Jade Cutter",
    "Primordial Jade Winged-Spear",
    "Skyward Atlas",
    "Skyward Blade",
    "Skyward Harp",
    "Skyward Pride",
    "Skyward Spine",
    "Song of Broken Pines",
    "Staff of Homa",
    "Summit Shaper",
    "The Unforged",
    "Vortex Vanquisher",
    "Wolf's Gravestone",
    "Yoimiya",
    "Raiden Shogun",
]
fi_chars = [
    "Albedo",
    "Diluc",
    "Eula",
    "Ganyu",
    "Hu Tao",
    "Jean",
    "Kaedehara Kazuha",
    "Kamisato Ayaka",
    "Keqing",
    "Klee",
    "Mona",
    "Qiqi",
    "Tartaglia",
    "Venti",
    "Xiao",
    "Zhongli",
    "Yoimiya",
    "Raiden Shogun",
]
fi_items = [
    "Amos' Bow",
    "Aquila Favonia",
    "Elegy for the End",
    "Freedom-Sworn" "Lost Prayer to the Sacred Winds",
    "Memory of Dust",
    "Primordial Jade Cutter",
    "Primordial Jade Winged-Spear",
    "Skyward Atlas",
    "Skyward Blade",
    "Skyward Harp",
    "Skyward Pride",
    "Skyward Spine",
    "Song of Broken Pines",
    "Staff of Homa",
    "Summit Shaper",
    "The Unforged",
    "Vortex Vanquisher",
    "Wolf's Gravestone",
]
sta_fi_wep = [
    "Amos' Bow",
    "Aquila Favonia",
    "Lost Prayer To The Sacred Winds",
    "Primordial Jade Winged-Spear",
    "Skyward Atlas",
    "Skyward Blade",
    "Skyward Harp",
    "Skyward Pride",
    "Skyward Spine",
    "Wolf's Gravestone",
]
# Character Instances (Manual Labour)

# five stars
albedo = Char("Albedo", 0)
diluc = Char("Diluc", 0)
eula = Char("Eula", 0)
ganyu = Char("Ganyu", 0)
hu_tao = Char("Hu Tao", 0)
jean = Char("Jean", 0)
kaedehara_kazuha = Char("Kaedehara Kazuha", 0)
kamisato_ayaka = Char("Kamisato Ayaka", 0)
keqing = Char("Keqing", 0)
klee = Char("Klee", 0)
mona = Char("Mona", 0)
qiqi = Char("Qiqi", 0)
tartaglia = Char("Tartaglia", 0)
venti = Char("Venti", 0)
xiao = Char("Xiao", 0)
zhongli = Char("Zhongli", 0)
yoimiya = Char("Yoimiya", 0)
raiden_shogun = Char("Raiden Shogun", 0)

# four stars
amber = Char("Amber", 0)
chongyun = Char("Chongyun", 0)
diona = Char("Diona", 0)
lisa = Char("Lisa", 0)
kaeya = Char("Kaeya", 0)
barbara = Char("Barbara", 0)
razor = Char("Razor", 0)
bennet = Char("Bennet", 0)
noelle = Char("Noelle", 0)
fischl = Char("Fischl", 0)
sucrose = Char("Sucrose", 0)
beidou = Char("Beidou", 0)
ningguang = Char("Ningguang", 0)
xiangling = Char("Xiangling", 0)
xinqiu = Char("Xinqiu", 0)
xinyan = Char("Xinyan", 0)
rosaria = Char("Rosaria", 0)
yanfei = Char("Yanfei", 0)
sayu = Char("Sayu", 0)
kujou_sara = Char("Kujou Sara", 0)

# Item Instances

# five stars
amos_bow = Weap("Amos' Bow", 0)
aquila_favonia = Weap("Aquila Favonia", 0)
elegy_for_the_end = Weap("Elegy for the End", 0)
engulfing_lightning = Weap("Engulfing Lightning", 0)
everlasting_moonglow = Weap("Everlasting Moonglow", 0)
freedom_sworn = Weap("Freedom-Sworn", 0)
lost_prayer_to_the_sacred_winds = Weap("Lost Prayer to the Sacred Winds", 0)
memory_of_dust = Weap("Memory of Dust", 0)
polar_star = Weap("Polar Star", 0)
primordial_jade_cutter = Weap("Primordial Jade Cutter", 0)
primordial_jade_winged_spear = Weap("Primordial Jade Winged-Spear", 0)
skyward_atlas = Weap("Skyward Atlas", 0)
skyward_blade = Weap("Skyward Blade", 0)
skyward_harp = Weap("Skyward Harp", 0)
skyward_pride = Weap("Skyward Pride", 0)
skyward_spine = Weap("Skyward Spine", 0)
song_of_broken_pines = Weap("Song of Broken Pines", 0)
staff_of_homa = Weap("Staff of Homa", 0)
summit_shaper = Weap("Summit Shaper", 0)
the_mistsplitter = Weap("The Mistsplitter", 0)
the_unforged = Weap("The Unforged", 0)
thundering_pulse = Weap("Thundering Pulse", 0)
vortex_vanquisher = Weap("Vortex Vanquisher", 0)
wolfs_gravestone = Weap("Wolf's Gravestone", 0)

# four stars
akoumaru = Weap("Akoumaru", 0)
alley_hunter = Weap("Alley Hunter", 0)
dragons_bane = Weap("Dragon's Bane", 0)
eye_of_perception = Weap("Eye of Perception", 0)
favonius_codex = Weap("Favonius Codex", 0)
favonius_greatsword = Weap("Favonious Greatsword", 0)
favonius_lance = Weap("Favonius Lance", 0)
favonius_sword = Weap("Favonius Sword", 0)
favonius_warbow = Weap("Favonius Warbow", 0)
lions_roar = Weap("Lion's Roar", 0)
lithic_blade = Weap("Lithic Blade", 0)
lithic_spear = Weap("Lithic Spear", 0)
mitternachts_waltz = Weap("Mitternachts Waltz", 0)
mouuns_moon = Weap("Mouun's Moon", 0)
rainslasher = Weap("Rainslasher", 0)
rust = Weap("Rust", 0)
sacrificial_bow = Weap("Sacrificial Bow", 0)
sacrificial_fragments = Weap("Sacrificial Fragments", 0)
sacrificial_greatsword = Weap("Sacrificial Greatsword", 0)
sacrificial_sword = Weap("Sacrificial Sword", 0)
the_alley_flash = Weap("The Alley Flash", 0)
the_bell = Weap("The Bell", 0)
the_flute = Weap("The Flute", 0)
the_stringless = Weap("The Stringless", 0)
the_widsith = Weap("The Widsith", 0)
wine_and_song = Weap("Wine and Song", 0)
wavebreakers_fin = Weap("Wavebreaker's Fin", 0)

# three stars
amber_catalyst = Weap("Amber Catalyst", 0)
black_tassel = Weap("Black Tassel", 0)
bloodtainted_greatsword = Weap("Bloodtainted Greatsword", 0)
cool_steel = Weap("Cool Steel", 0)
dark_iron_sword = Weap("Dark Iron Sword", 0)
debate_club = Weap("Debate Club", 0)
ebony_bow = Weap("Ebony Bow", 0)
emerald_orb = Weap("Emerald Orb", 0)
ferrous_shadow = Weap("Ferrous Shadow", 0)
fillet_blade = Weap("Fillet Blade", 0)
halberd = Weap("Halberd", 0)
harbinger_of_dawn = Weap("Harbinger of Dawn", 0)
magic_guide = Weap("Magic Guide", 0)
messenger = Weap("Messenger", 0)
otherworldly_story = Weap("Otherworldly Story", 0)
quartz = Weap("Quartz", 0)
raven_bow = Weap("Raven Bow", 0)
recurve_bow = Weap("Recurve Bow", 0)
sharpshooters_oath = Weap("Sharpshooter's Oath", 0)
skyrider_greatsword = Weap("Skyrider Greatsword", 0)
skyrider_sword = Weap("Skyrider Sword", 0)
slingshot = Weap("Slingshot", 0)
thrilling_tales_of_dragon_slayers = Weap("Thrilling Tales of Dragon Slayers", 0)
travelers_handy_sword = Weap("Traveler's Handy Sword", 0)
twin_nephrite = Weap("Twin Nephrite", 0)
white_iron_greatsword = Weap("White Iron Greatsword", 0)
white_tassel = Weap("White Tassel", 0)

# Dictionary for Characters/Weapons (Manual Labour)

item_dict = {
    # five star characters
    "Albedo": albedo,
    "Diluc": diluc,
    "Eula": eula,
    "Ganyu": ganyu,
    "Hu Tao": hu_tao,
    "Jean": jean,
    "Kaedehara Kazuha": kaedehara_kazuha,
    "Kamisato Ayaka": kamisato_ayaka,
    "Keqing": keqing,
    "Klee": klee,
    "Mona": mona,
    "Qiqi": qiqi,
    "Tartaglia": tartaglia,
    "Venti": venti,
    "Xiao": xiao,
    "Zhongli": zhongli,
    "Yoimiya": yoimiya,
    "Raiden Shogun": raiden_shogun,
    # four star characters
    "Amber": amber,
    "Lisa": lisa,
    "Kaeya": kaeya,
    "Barbara": barbara,
    "Razor": razor,
    "Bennet": bennet,
    "Noelle": noelle,
    "Fischl": fischl,
    "Sucrose": sucrose,
    "Beidou": beidou,
    "Ningguang": ningguang,
    "Xiangling": xiangling,
    "Xinqiu": xinqiu,
    "Chongyun": chongyun,
    "Diona": diona,
    "Xinyan": xinyan,
    "Rosaria": rosaria,
    "Yanfei": yanfei,
    "Sayu": sayu,
    "Kujou Sara": kujou_sara,
    # five star weapons
    "Amos' Bow": amos_bow,
    "Aquila Favonia": aquila_favonia,
    "Elegy for the End": elegy_for_the_end,
    "Engulfing Lightning": engulfing_lightning,
    "Everlasting Moonglow": everlasting_moonglow,
    "Freedom-Sworn": freedom_sworn,
    "Lost Prayer To The Sacred Winds": lost_prayer_to_the_sacred_winds,
    "Memory of Dust": memory_of_dust,
    "Polar Star": polar_star,
    "Primordial Jade Cutter": primordial_jade_cutter,
    "Primordial Jade Winged-Spear": primordial_jade_winged_spear,
    "Skyward Atlas": skyward_atlas,
    "Skyward Blade": skyward_blade,
    "Skyward Harp": skyward_harp,
    "Skyward Pride": skyward_pride,
    "Skyward Spine": skyward_spine,
    "Song of Broken Pines": song_of_broken_pines,
    "Staff of Homa": staff_of_homa,
    "Summit Shaper": summit_shaper,
    "The Mistsplitter": the_mistsplitter,
    "The Unforged": the_unforged,
    "Thundering Pulse": thundering_pulse,
    "Vortex Vanquisher": vortex_vanquisher,
    "Wolf's Gravestone": wolfs_gravestone,
    # four star weapons
    "Akoumaru": akoumaru,
    "Alley Hunter": alley_hunter,
    "Dragon's Bane": dragons_bane,
    "Eye of Perception": eye_of_perception,
    "Favonius Codex": favonius_codex,
    "Favonius Greatsword": favonius_greatsword,
    "Favonius Lance": favonius_lance,
    "Favonius Sword": favonius_sword,
    "Favonius Warbow": favonius_warbow,
    "Lion's Roar": lions_roar,
    "Lithic Blade": lithic_blade,
    "Lithic Spear": lithic_spear,
    "Mitternachts Waltz": mitternachts_waltz,
    "Mouun's Moon": mouuns_moon,
    "Rainslasher": rainslasher,
    "Rust": rust,
    "Sacrificial Bow": sacrificial_bow,
    "Sacrificial Fragments": sacrificial_fragments,
    "Sacrificial Greatsword": sacrificial_greatsword,
    "Sacrificial Sword": sacrificial_sword,
    "The Alley Flash": the_alley_flash,
    "The Bell": the_bell,
    "The Flute": the_flute,
    "The Stringless": the_stringless,
    "The Widsith": the_widsith,
    "Wavebreaker's Fin": wavebreakers_fin,
    "Wine and Song": wine_and_song,
    # three star weapons
    "Amber Catalyst": amber_catalyst,
    "Black Tassel": black_tassel,
    "Bloodtainted Greatsword": bloodtainted_greatsword,
    "Cool Steel": cool_steel,
    "Dark Iron Sword": dark_iron_sword,
    "Debate Club": debate_club,
    "Ebony Bow": ebony_bow,
    "Emerald Orb": emerald_orb,
    "Ferrous Shadow": ferrous_shadow,
    "Fillet Blade": fillet_blade,
    "Halberd": halberd,
    "Harbinger of Dawn": harbinger_of_dawn,
    "Magic Guide": magic_guide,
    "Messenger": messenger,
    "Otherworldly Story": otherworldly_story,
    "Quartz": quartz,
    "Raven Bow": raven_bow,
    "Recurve Bow": recurve_bow,
    "Sharpshooter's Oath": sharpshooters_oath,
    "Skyrider Greatsword": skyrider_greatsword,
    "Skyrider Sword": skyrider_sword,
    "Slingshot": slingshot,
    "Thrilling Tales of Dragon Slayers": thrilling_tales_of_dragon_slayers,
    "Traveler's Handy Sword": travelers_handy_sword,
    "Twin Nephrite": twin_nephrite,
    "White Iron Greatsword": white_iron_greatsword,
    "White Tassel": white_tassel,
}

# the inventory
item_inv = ItemInv()
