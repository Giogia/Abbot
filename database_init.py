from modules import database

database.create_table()
database.conn.commit()

words = [
    "abalone",
    "acorn",
    "acorn squash",
    "admiral butterfly",
    "African elephant",
    "African gray parrot",
    "African penguin",
    "African rock python",
    "African wild cat",
    "agate",
    "agouti",
    "agriculture",
    "airedale terrier",
    "Alaskan malamute",
    "albatross",
    "alexandrite",
    "alfalfa",
    "algae",
    "alligator",
    "allspice",
    "almond",
    "alpaca",
    "alternate leaves",
    "amber",
    "ambush bug",
    "American bison",
    "American cocker spaniel",
    "American crocodile",
    "American flamingo",
    "American golden plover",
    "American Robin",
    "American tree sparrow",
    "amethyst",
    "amoeba",
    "amphibian",
    "anaconda",
    "anemone",
    "angelfish",
    "angelica",
    "angelshark",
    "angiosperm",
    "angonoka",
    "animal",
    "anise",
    "annato",
    "annual",
    "anole",
    "ant",
    "anteater",
    "antelope",
    "anther",
    "Apatosaurus",
    "ape",
    "aphid",
    "apical meristem",
    "apple",
    "apple blossom",
    "apricot",
    "aquamarine",
    "arachnid",
    "archaeopteryx",
    "arctic fox",
    "Arctic tern",
    "arctic wolf",
    "armadillo",
    "armyworm",
    "Arsinoitherium",
    "arthropod",
    "artichoke",
    "artiodactyls",
    "arugula",
    "ash",
    "asp",
    "asparagus",
    "aspen",
    "assassin bug",
    "aster",
    "atlas moth",
    "autotroph",
    "aventurine",
    "avocado",
    "awning",
    "axil",
    "axilary bud",
    "aye-aye",
    "azalea",
    "azurite",
    "baboon",
    "baby's breath",
    "bachelor button",
    "back porch",
    "back stoop",
    "backswimmer",
    "backyard",
    "bactrian camel",
    "badger",
    "bald eagle",
    "bamboo",
    "bamboo shoots",
    "banana",
    "bandicoot",
    "banyan",
    "baobob",
    "bark",
    "barnacle",
    "barracuda",
    "basalt",
    "basil",
    "basilisk",
    "basketball hoop",
    "basking shark",
    "bass",
    "basset hound",
    "bat",
    "bay",
    "beagle",
    "bean",
    "beans",
    "bear",
    "bearded dragon",
    "beaver",
    "bed bug",
    "bedbug",
    "bee",
    "beech",
    "beetle",
    "beets",
    "begonia",
    "bell pepper",
    "bellflower",
    "bells of Ireland",
    "beluga whale",
    "bench",
    "berbere",
    "berry",
    "beryl",
    "bichon frise",
    "biennial",
    "bighorn sheep",
    "bigtooth aspen",
    "bilby",
    "binturong",
    "birch",
    "bird",
    "birdbath",
    "bison",
    "bitterroot",
    "bivalve",
    "black ash",
    "black bear",
    "black bear hamster",
    "black caiman",
    "black racer",
    "black swan",
    "black willow",
    "black-eyed peas",
    "black-eyed Susan",
    "blackberry",
    "blackbird",
    "blade",
    "blood orange",
    "bloodhound",
    "blossom",
    "blowfish",
    "blue jay",
    "blue morpho butterfly",
    "blue ring octopus",
    "blue shark",
    "blue whale",
    "blue-tongued skink",
    "bluebells",
    "blueberry",
    "bluebird",
    "bluebonnet",
    "bluefin tuna",
    "bluet",
    "boa constrictor",
    "bobcat",
    "bodhi",
    "bongo",
    "bonobo",
    "bony fish",
    "borage",
    "border collie",
    "borer",
    "Boston terrier",
    "botany",
    "bougainvillea",
    "bouquet",
    "bowhead whale",
    "box turtle",
    "boxer",
    "boysenberry",
    "bract",
    "branch",
    "breadfruit",
    "bristlecone pine",
    "brittle star",
    "broccoli",
    "bromeliad",
    "brown bear",
    "brown butterfly",
    "brown pelican",
    "brush",
    "Brussels sprouts",
    "buckeye",
    "buckeye butterfly",
    "bud",
    "buffalo",
    "bug",
    "bulb",
    "bulbel",
    "bulbs",
    "bull",
    "bull shark",
    "bull snake",
    "bulldog",
    "bullfrog",
    "bumblebee",
    "bush",
    "bushbaby",
    "buttercup",
    "butterfly",
    "butterfly bush",
    "butternut",
    "cabbage palmetto",
    "cactus",
    "caiman",
    "calcite",
    "calendula",
    "California poppy",
    "California sea lion",
    "calla lily",
    "calyx",
    "camel",
    "camellia",
    "Canada goose",
    "canary",
    "candytuft",
    "canna",
    "canopy",
    "cantaloupe",
    "cape buffalo",
    "Cape hunting dog",
    "capers",
    "capybera",
    "caracal",
    "carat",
    "caraway",
    "cardamon",
    "cardinal",
    "caribou",
    "carnation",
    "carnelian",
    "carnivora",
    "carob",
    "carpel",
    "carpenter ant",
    "carport",
    "carrion flower",
    "carrot",
    "cassowary",
    "cat",
    "catalpa",
    "catamount",
    "caterpillar",
    "cattle",
    "cauliflower",
    "cavy",
    "cayenne pepper",
    "cedar",
    "celeriac",
    "celery",
    "celery seed",
    "centipede",
    "cephalpod",
    "chalcedony",
    "chameleon",
    "chard",
    "cheetah",
    "cherry",
    "chervil",
    "chestnut",
    "chick peas",
    "chickadee",
    "chicken",
    "chicory",
    "chihuahua",
    "chili pepper",
    "chimipanzee",
    "chinchilla",
    "Chinese cabbage",
    "chipmunk",
    "chiton",
    "chives",
    "choke cherry",
    "chrysalis",
    "chrysanthemum",
    "cicada",
    "cicely",
    "cilantro",
    "cinnamon",
    "citrine",
    "citron",
    "citrus",
    "clam",
    "cleft leaf",
    "cloud",
    "clove",
    "clover",
    "clownfish",
    "coal",
    "coati",
    "cobra",
    "cockatoo",
    "cockroach",
    "coconut",
    "coconut palm",
    "cod",
    "coelacanth",
    "collard greens",
    "collared lizard",
    "collared peccary",
    "collie",
    "colugo",
    "columbine",
    "comma butterfly",
    "common rhea",
    "companion dog",
    "composite flower",
    "compost bin",
    "compound leaf",
    "conch",
    "cone",
    "cookiecutter shark",
    "copepod",
    "copper butterfly",
    "copperhead snake",
    "coral",
    "coral snake",
    "coriander",
    "cork",
    "corm",
    "corn snake",
    "cornflower",
    "corolla",
    "corpse flower",
    "cosmo",
    "cottonmouth",
    "cottonwood",
    "cougar",
    "cow",
    "coyote",
    "coypu",
    "crab",
    "crabapple",
    "cranberry",
    "crane",
    "crane fly",
    "crape myrtle",
    "crayfish",
    "crenate leaf",
    "cress",
    "cricket",
    "crocodile",
    "crocus",
    "crow",
    "crustacean",
    "Cryptoclidus",
    "crystal",
    "cucumber",
    "current",
    "curry leaf",
    "cuttlefish",
    "cutworm",
    "cypress",
    "Dachshund",
    "daffodil",
    "dahlia",
    "daikon",
    "daisy",
    "dall sheep",
    "Dall's porpoise",
    "Dalmatian",
    "damselfly",
    "dandelion",
    "dandelion greens",
    "dark-eyed junco",
    "darkling beetle",
    "date",
    "deciduous",
    "deer",
    "Deinonychus",
    "delphinium",
    "density",
    "dentate leaf",
    "desert tortoise",
    "Desmatosuchus",
    "dhole",
    "diamond",
    "dianthus",
    "diatom",
    "dicot",
    "dill",
    "Dilophosaurus",
    "Dimetrodon",
    "dingo",
    "Dinichthys",
    "Dinornis",
    "dinosaur",
    "Diplodocus",
    "Doberman pinscher",
    "dodo",
    "Doedicurus",
    "dog",
    "dogfish",
    "doghouse",
    "dogwood",
    "dolomite",
    "dolphin",
    "dolphin, bottlenose",
    "dolphin, spotted",
    "donkey",
    "dory",
    "Douglas fir",
    "dove",
    "downspout",
    "downy woodpecker",
    "dragonfly",
    "dragonfruit",
    "driveway",
    "dromedary",
    "druze",
    "duck",
    "duck-billed platypus",
    "dugong",
    "dung beetle",
    "Dunkleosteus",
    "durian",
    "eagle",
    "earthworm",
    "earwig",
    "eastern bluebird",
    "eastern quoll",
    "echidna",
    "echinoderms",
    "edelweiss",
    "Edenta",
    "edger",
    "Edmontonia",
    "Edmontosaurus",
    "eel",
    "egg",
    "eggplant",
    "egret",
    "ekaltadelta",
    "eland",
    "Elasmosaurus",
    "Elasmotherium",
    "elderberry",
    "electric eel",
    "elephant",
    "elephant seal",
    "elk",
    "elm",
    "embryo",
    "emerald",
    "emerald tree boa",
    "emergents",
    "emperor angelfish",
    "emperor penguin",
    "emu",
    "endangered species",
    "endive",
    "endosperm",
    "entire",
    "Eohippus",
    "Eoraptor",
    "epazote",
    "epicotyl",
    "ermine",
    "Estemmenosuchus",
    "eucalyptus",
    "evergreen",
    "extinct animals",
    "Fabrosaurus",
    "facet",
    "falcon",
    "farm animals",
    "fava bean",
    "feldspar",
    "fence",
    "fennec fox",
    "fennel",
    "fenugreek",
    "fern",
    "ferret",
    "fertilizer",
    "fiddler crab",
    "fig",
    "filament",
    "filbert",
    "fin whale",
    "finch",
    "fir",
    "fire ant",
    "fire opal",
    "fireant",
    "firefly",
    "fish",
    "flame tree",
    "flamingo",
    "flatworm",
    "flea",
    "flightless birds",
    "flora",
    "floret",
    "florist",
    "flounder",
    "flower",
    "flower garden",
    "flowerbed",
    "fluorite",
    "fly",
    "flying fish",
    "flying squirrel",
    "fog",
    "foliage",
    "fool's gold",
    "forest",
    "forest antelope",
    "forest giraffe",
    "forget-me-not",
    "fossa",
    "fossil",
    "fowl",
    "fox",
    "foxglove",
    "freesia",
    "frilled lizard",
    "fritillary butterfly",
    "frog",
    "frond",
    "front porch",
    "front stoop",
    "frost",
    "fruit",
    "fruit bat",
    "fruit fly",
    "fruit tree",
    "fruitfly",
    "fugu",
    "galagos",
    "galangal",
    "Galapagos shark",
    "gar",
    "garage",
    "garam masala",
    "garbage can",
    "garden",
    "garden path",
    "gardenia",
    "garlic",
    "garlic chives",
    "garnet",
    "gastropod",
    "gate",
    "gavial",
    "gazelle",
    "gecko",
    "gem",
    "gemstone",
    "geode",
    "geology",
    "gerbera daisy",
    "gerbil",
    "German shepherd",
    "germinate",
    "giant squid",
    "gibbon",
    "gila monster",
    "gillyflower",
    "ginger",
    "ginkgo",
    "giraffe",
    "gladiolus",
    "Glyptodon",
    "gnat",
    "gneiss",
    "gnu",
    "goat",
    "gold",
    "golden eagle",
    "golden lion tamarin",
    "golden retriever",
    "goldenlarch",
    "goldenrod",
    "goldfinch",
    "goldfish",
    "goose",
    "gopher",
    "gorilla",
    "gossamer-winged butterfly",
    "gourd",
    "grain",
    "granite",
    "grape",
    "grapefruit",
    "grass",
    "grasshopper",
    "gravel",
    "gray whale",
    "great apes",
    "great Dane",
    "great egret",
    "great horned owl",
    "great white shark",
    "green darner dragonfly",
    "green iguana",
    "green onion",
    "greenbean",
    "Greenland shark",
    "greens",
    "greyhound",
    "grizzly bear",
    "ground beetle",
    "groundhog",
    "grouper",
    "grouse",
    "grove",
    "grow",
    "grub",
    "guard cell",
    "guava",
    "guinea pig",
    "gull",
    "gulper eel",
    "gum",
    "gutter",
    "gypsum",
    "gypsy moth",
    "hackberry",
    "hail",
    "hairstreak butterfly",
    "hammerhead shark",
    "hammock",
    "hamster",
    "hardness",
    "hardy",
    "hare",
    "harissa",
    "harlequin bug",
    "harp seal",
    "harpy eagle",
    "hastate",
    "hatchetfish",
    "haw",
    "Hawaiian goose",
    "hawk",
    "hawthorn",
    "heather",
    "hedgehog",
    "hedges",
    "hematite",
    "hemlock",
    "hen",
    "herb",
    "herb garden",
    "hermit crab",
    "heron",
    "herring",
    "hibiscus",
    "hickory",
    "hippo",
    "hippopotamus",
    "hoe",
    "holly",
    "hollyhock",
    "honey bee",
    "honeybee",
    "honeydew",
    "honeylocust",
    "honeysuckle",
    "hornet",
    "horse",
    "horse fly",
    "horseradish",
    "horseshoe crab",
    "horsetail",
    "horticulture",
    "hose",
    "hot chile peppers",
    "hound",
    "house fly",
    "hover fly",
    "howler monkey",
    "howlite",
    "human being",
    "hummingbird",
    "hummingbird feeder",
    "humpback whale",
    "husky",
    "hybrid",
    "hydrangea",
    "hyena",
    "Hyracotherium",
    "hyrax",
    "hyssop",
    "ibis",
    "ice",
    "iceberg lettuce",
    "Ichthyornis",
    "Ichthyosaurus",
    "igneous rock",
    "iguana",
    "Iguanodon",
    "imago",
    "impala",
    "imperfect flower",
    "inclusion",
    "incomplete flower",
    "Indian blanket",
    "Indian elephant",
    "inflorescence",
    "insect",
    "insectivores",
    "internode",
    "invertebrates",
    "ipil",
    "iris",
    "Irish setter",
    "ironwood",
    "isopod",
    "ivy",
    "jack pine",
    "jack rabbit",
    "Jack Russell terrier",
    "jackfruit",
    "jacktree",
    "jade",
    "jadeite",
    "jaguar",
    "Janenschia",
    "Japanese beetle",
    "Japanese crane",
    "Japanese maple",
    "jasmine",
    "jasmine flowers",
    "jasper",
    "javelina",
    "jay",
    "jellyfish",
    "jerboa",
    "jerk spice",
    "jessamine",
    "jet",
    "jicama",
    "joey",
    "John Dory",
    "Johnny-jump-up",
    "jonquil",
    "jujuba",
    "Julia butterfly",
    "jumping bean",
    "jumping bean moth",
    "junco",
    "junebug",
    "jungle",
    "juniper",
    "juniper berry",
    "kaffir lime leaves",
    "kakapo",
    "kale",
    "kangaroo",
    "kangaroo paw",
    "kangaroo rat",
    "kapok tree",
    "karakul",
    "karat",
    "katsura",
    "katydid",
    "keel-billed toucan",
    "kelp",
    "Kentrosaurus",
    "killer whale",
    "king cobra",
    "king crab",
    "kinkajou",
    "kissing bug",
    "kiwi",
    "knobbed whelk",
    "koala",
    "kohlrabi",
    "Komodo dragon",
    "kookaburra",
    "krill",
    "Kronosaurus",
    "Kudu",
    "kudzu",
    "kukui nut",
    "kumquat",
    "kunzite",
    "Labrador retriever",
    "labradorite",
    "lacewing",
    "lady's slipper",
    "ladybug",
    "lagomorph",
    "lake trout",
    "lamina",
    "lanceolate leaf",
    "land",
    "lantana",
    "lanternfish",
    "lapidary",
    "lapis lazuli",
    "larch",
    "larkspur",
    "larva",
    "lateral bud",
    "laurel",
    "lava",
    "lavender",
    "lawn",
    "lawnmower",
    "lead scar",
    "leaf",
    "leafcutter ant",
    "leafhopper",
    "leaflet",
    "leek",
    "leghorn",
    "legume",
    "lemming",
    "lemon",
    "lemon balm",
    "lemon shark",
    "lemon verbena",
    "lemur",
    "lentils",
    "leopard",
    "lettuce",
    "Lhasa apso",
    "lice",
    "licorice",
    "lightning",
    "lightning bug",
    "lilac",
    "lily",
    "lily-of-the-valley",
    "Lima bean",
    "lime",
    "limestone",
    "limpet",
    "linden",
    "lingonberry",
    "lion",
    "Liopleurodon",
    "lithified",
    "live oak",
    "lizard",
    "llama",
    "lobed",
    "loblolly pine",
    "lobster",
    "locust",
    "loess",
    "loggerhead turtle",
    "lone pine",
    "longhorn",
    "longhorn beetle",
    "longleaf pine",
    "loon",
    "loquat",
    "lorikeet",
    "loris",
    "louse",
    "lovage",
    "luminous shark",
    "luna moth",
    "luster",
    "lychee",
    "lynx",
    "macaque",
    "macaw",
    "mace",
    "mackerel",
    "Macrauchenia",
    "maggot",
    "magma",
    "magnetite",
    "magnolia",
    "mahogany",
    "maize",
    "mako shark",
    "malachite",
    "mallard duck",
    "mallow",
    "mamba",
    "mammal",
    "mammoth",
    "man-o'-war",
    "manatee",
    "mandarin orange",
    "mandrill",
    "mango",
    "mangrove",
    "manta ray",
    "mantid",
    "mantis",
    "maple",
    "marbled murrelet",
    "margin",
    "marigold",
    "marine mammals",
    "marionberry",
    "marjoram",
    "marmoset",
    "marmot",
    "marsupial",
    "mastiff",
    "mastodon",
    "mayflower",
    "mayfly",
    "meadowhawk",
    "meadowlark",
    "mealworm",
    "meerkat",
    "Megalodon",
    "megamouth shark",
    "melon",
    "merganser",
    "meristem",
    "metalmark butterfly",
    "metamorphic rock",
    "metamorphosis",
    "meteoroid",
    "mica",
    "mice",
    "midge",
    "midrib",
    "migrate",
    "milkweed bug",
    "millipede",
    "mimosa",
    "mineral",
    "mink",
    "minnow",
    "mint",
    "mist",
    "mistletoe",
    "moa",
    "mock orange",
    "mockingbird",
    "mole",
    "mollusk",
    "monarch",
    "monarch butterfly",
    "mongoose",
    "monitor lizard",
    "monkey",
    "monocot",
    "monotreme",
    "moonstone",
    "moose",
    "moray eel",
    "Morganucodon",
    "morning glory",
    "morpho",
    "morpho butterfly",
    "mosquito",
    "moss",
    "moss agate",
    "moth",
    "mountain laurel",
    "mountain lion",
    "mountainash",
    "mouse",
    "mudpuppy",
    "mulberry",
    "mung bean",
    "mushroom",
    "musk ox",
    "muskrat",
    "mussels",
    "mustard greens",
    "mustard seed",
    "mustelids",
    "myrtle",
    "nabarlek",
    "naked mole-rat",
    "nandu",
    "narcissus",
    "narwhal",
    "nasturtium",
    "nautilus",
    "nectar",
    "nectarine",
    "needle",
    "nene",
    "nephrite",
    "nest",
    "netted",
    "newt",
    "nightingale",
    "nine-banded armadillo",
    "node",
    "North American beaver",
    "North American porcupine",
    "northern cardinal",
    "northern elephant seal",
    "northern fur seal",
    "northern red oak",
    "northern right whale",
    "Norway maple",
    "numbat",
    "nurse shark",
    "nut",
    "nuthatch",
    "nutmeg",
    "nutria",
    "nymph",
    "oak",
    "obsidian",
    "ocelot",
    "octopus",
    "okapi",
    "okra",
    "old English sheepdog",
    "oleander",
    "olive",
    "onager",
    "onion",
    "opal",
    "opossum",
    "opposite leaves",
    "orange",
    "orange blossom",
    "orangutan",
    "orca",
    "orchard",
    "orchid",
    "oregano",
    "Oregon silverspot butterfly",
    "oriole",
    "Ornitholestes",
    "Ornithomimus",
    "oropendola",
    "Orthacanthus",
    "orthoclase",
    "oryx",
    "ostrich",
    "otter, river",
    "otter, sea",
    "ovary",
    "Oviraptor",
    "owl",
    "owl butterfly",
    "ox",
    "oxpecker",
    "oyster",
    "painted lady butterfly",
    "painted turtle",
    "palm",
    "palmate",
    "palmetto",
    "panda",
    "pangolin",
    "pansy",
    "panther",
    "papaya",
    "paper birch",
    "paper wasp",
    "paprikaa",
    "parakeet",
    "parrot",
    "parsley",
    "parsnip",
    "parted leaf",
    "pasque flower",
    "passion fruit",
    "passionflower",
    "path",
    "patio",
    "patio furniture",
    "pattypan squash",
    "pawpaw",
    "pea",
    "peach",
    "peach blossom",
    "peacock",
    "peafowl",
    "peanut",
    "peapod",
    "pear",
    "pebble",
    "pecan",
    "peduncle",
    "pekingese",
    "pelican",
    "penguin",
    "peony",
    "pepper",
    "peppermint",
    "peppers",
    "peregrine falcon",
    "perennial",
    "perfect flower",
    "peridot",
    "Perissodactyls",
    "persimmon",
    "petal",
    "petiole",
    "petrel",
    "petrified wood",
    "phloem",
    "phlox",
    "photosynthesis",
    "pickle",
    "pig",
    "pigeon",
    "pika",
    "pill bug",
    "pine",
    "pineapple",
    "pinnate",
    "pinnipeds",
    "piranha",
    "pistil",
    "pith",
    "placental mammals",
    "plankton",
    "plant pot",
    "plantain",
    "planter",
    "planthopper",
    "platybelodon",
    "platypus",
    "ploughshare tortoise",
    "plover",
    "plum",
    "plumeria",
    "plumule",
    "pluot",
    "poinsettia",
    "poison ivy",
    "polar bear",
    "pollen",
    "pollinate",
    "polliwog",
    "pomegranite",
    "pomelo",
    "pomeranian",
    "pompano",
    "pond",
    "pond skater",
    "poodle",
    "pool",
    "poplar",
    "poppy",
    "porch",
    "porch swing",
    "porcupine",
    "porpoise",
    "Port Jackson shark",
    "Portuguese water dog",
    "Postosuchus",
    "potato",
    "prairie chicken",
    "praying mantid",
    "praying mantis",
    "prickle",
    "primates",
    "primrose",
    "Proboscideans",
    "pronghorn",
    "protozoan",
    "prune",
    "pufferfish",
    "puffin",
    "pug",
    "pulse",
    "puma",
    "pumice",
    "pumpkin",
    "pupa",
    "pupfish",
    "pussy willow",
    "pyrite",
    "pyroclastic flow",
    "python",
    "Quaesitosaurus",
    "quagga",
    "quail",
    "quaking aspen",
    "quartz",
    "Queen Alexandra's birdwing",
    "Queen Alexandra's birdwing butterfly",
    "Queen Anne's lace",
    "queen conch",
    "quetzal",
    "quince",
    "quokka",
    "quoll",
    "rabbit",
    "raccoon",
    "rachis",
    "radicchio",
    "radish",
    "rain",
    "rain forest",
    "raisin",
    "rake",
    "ranunculus",
    "raspberry",
    "rat",
    "rattlesnake",
    "ray",
    "red hooded duck",
    "red kangaroo",
    "red panda",
    "red wolf",
    "red-tailed hawk",
    "redbilled oxpecker",
    "redbud",
    "redwood",
    "reindeer",
    "reniform",
    "reptile",
    "resin",
    "reticulate",
    "rhea",
    "rhino",
    "rhinoceros",
    "Rhode Island red",
    "rhododendron",
    "rhubarb",
    "right whale",
    "ring-billed gull",
    "ring-tailed lemur",
    "rings",
    "ringtail possum",
    "river otter",
    "roach",
    "roadrunner",
    "robber fly",
    "robin",
    "rock",
    "rock cycle",
    "rock dove",
    "rocket",
    "rockhopper penguin",
    "rocks",
    "rodent",
    "romaine",
    "rooster",
    "root",
    "root cap",
    "root hairs",
    "root tip",
    "rootstock",
    "rose",
    "rose quartz",
    "rosemary",
    "rottweiler",
    "roundworm",
    "rubber tree",
    "ruby",
    "ruby-throated hummingbird",
    "rue",
    "rutabaga",
    "safflower",
    "saffron",
    "sage",
    "sage brush",
    "sailfish",
    "salad",
    "salad burnet",
    "salamander",
    "salmon",
    "salsa",
    "salsify",
    "salt",
    "sand",
    "sand dollar",
    "sandpiper",
    "sandstone",
    "sap",
    "sapling",
    "sapphire",
    "sard",
    "sardonyx",
    "sassafras",
    "savory",
    "scallion",
    "scallop",
    "scarab",
    "scarlet macaw",
    "schist",
    "scorpion",
    "Scotch pine",
    "Scottish terrier",
    "sea anemone",
    "sea cow",
    "sea cucumber",
    "sea otter",
    "sea star",
    "sea turtle",
    "sea urchin",
    "sea weed",
    "sea worm",
    "seahorse",
    "seal",
    "sealion",
    "seaweed",
    "sedimentary rock",
    "seed",
    "seed pod",
    "seedling",
    "sego lily",
    "seismograph",
    "semi-precious",
    "sepal",
    "sequoia",
    "serpentine",
    "serrate leaf",
    "serval",
    "serviceberry",
    "shallot",
    "shamrock",
    "shark",
    "shed",
    "sheep",
    "shoot",
    "shovel",
    "shrew",
    "shrimp",
    "shrub",
    "siamang",
    "Siberian husky",
    "silica",
    "silkworm",
    "silt",
    "silver maple",
    "silverfish",
    "simple leaf",
    "Sitka spruce",
    "skink",
    "skipper",
    "skunk",
    "sleet",
    "slippery elm",
    "sloth",
    "slow worm",
    "slug",
    "Smilodon",
    "snail",
    "snake",
    "snapdragon",
    "snapper",
    "snapping turtle",
    "snout butterfly",
    "snow",
    "snow goose",
    "snow leopard",
    "snowy owl",
    "soapstone",
    "sod",
    "sodalite",
    "softshell turtle",
    "soil",
    "sorrel",
    "soybean",
    "sparrow",
    "spearmint",
    "spectacled caiman",
    "spectacled porpoise",
    "spider",
    "spinach",
    "spine",
    "spinel",
    "spiny anteater",
    "spiny lizard",
    "spittlebug",
    "sponge",
    "spore",
    "spotted owl",
    "springtail",
    "sprinkler",
    "sprout",
    "sprouts",
    "spruce",
    "spuds",
    "squash",
    "squid",
    "squirrel",
    "St. Bernard",
    "stag beetle",
    "stalactite",
    "stalagmite",
    "stalk",
    "stamen",
    "stand",
    "star anise",
    "star fruit",
    "starfish",
    "starling",
    "Stegosaurus",
    "stem",
    "stepping stone",
    "stigma",
    "stingray",
    "stink bug",
    "stipule",
    "stock",
    "stoma",
    "stone",
    "stonefly",
    "stoop",
    "stork",
    "storm",
    "strawberry",
    "string bean",
    "style",
    "succotash",
    "succulents",
    "sugar glider",
    "sugar maple",
    "sulphur butterfly",
    "sumac",
    "sun",
    "sunfish",
    "sunflower",
    "sunlight",
    "swallowtail butterfly",
    "swan",
    "sweet pea",
    "sweet potato",
    "sweetgum",
    "swift",
    "swimming pool",
    "swing",
    "Swiss chard",
    "swordfish",
    "sycamore",
    "T. rex",
    "tadpole",
    "talc",
    "talus",
    "tamarin",
    "tanager",
    "tangelo",
    "tangerine",
    "tap root",
    "tapir",
    "tarantula",
    "taro",
    "tarpon",
    "tarragon",
    "tarsier",
    "Tasmanian devil",
    "Tasmanian tiger",
    "teak",
    "Teratosaurus",
    "terminal bud",
    "termite",
    "tern",
    "terrace",
    "terrier",
    "Thecodontosaurus",
    "Thescelosaurus",
    "thistle",
    "thorn",
    "three-toed sloth",
    "thresher shark",
    "thrip",
    "thunder",
    "thyme",
    "tick",
    "tickseed",
    "tiger",
    "tiger beetle",
    "tiger lily",
    "tiger moth",
    "tiger shark",
    "tiger swallowtail butterfly",
    "tiger's eye",
    "toad",
    "tomatillo",
    "tomato",
    "toothed",
    "topaz",
    "Torosaurus",
    "tortoise",
    "toucan",
    "tourmaline",
    "Trachodon",
    "trampoline",
    "trash can",
    "tree",
    "tree fern",
    "tree shrew",
    "tree sparrow",
    "treefrog",
    "Triceratops",
    "trillium",
    "Trilobite",
    "Troodon",
    "trout",
    "trumpeter swan",
    "trunk",
    "tsavorite",
    "tsetse fly",
    "tuatara",
    "tuber",
    "tulip",
    "tulip-tree",
    "tumbleweeds",
    "tumeric",
    "tuna",
    "tundra wolf",
    "tupelo",
    "turkey",
    "turnip",
    "turquoise",
    "turtle",
    "twig",
    "Tyrannosaurus rex",
    "ugli fruit",
    "Ultrasaurus",
    "Ulysses butterfly",
    "umbrellabird",
    "unakite",
    "understory",
    "undulate leaf margin",
    "ungulates",
    "uniramians",
    "upright red maple",
    "urchin",
    "Utahraptor",
    "valley quail",
    "vampire bat",
    "vanilla",
    "vascular plant",
    "vegetable",
    "vegetable garden",
    "vegetation",
    "veiled chameleon",
    "vein",
    "Velociraptor",
    "venation",
    "venomous animals",
    "Venus flytrap",
    "veronica",
    "vertebrates",
    "vetch",
    "viburnum",
    "viceroy butterfly",
    "vine",
    "vinegarroon",
    "violet",
    "viper",
    "Virginia opossum",
    "vitreous",
    "volcanic bomb",
    "volcanic glass",
    "volcano",
    "vulcanite",
    "Vulcanodon",
    "vulture",
    "wading pool",
    "wairakite",
    "walkingstick",
    "walkway",
    "wallaby",
    "wallflower",
    "walnut",
    "walrus",
    "warthog",
    "wasabi",
    "wasp",
    "water boatman",
    "water chestnut",
    "water moccasin",
    "water strider",
    "waterbug",
    "watercress",
    "watermelon",
    "waterstrider",
    "weasel",
    "Weddell seal",
    "weed",
    "weeds",
    "weeping willow",
    "weevil",
    "welcome mat",
    "west highland white terrier",
    "western meadowlark",
    "western spotted owl",
    "whale",
    "whale shark",
    "whelk",
    "whip scorpion",
    "whippet",
    "white ash",
    "white Bengal tiger",
    "white dove",
    "white oak",
    "white pelican",
    "white pine",
    "white rhinoceros",
    "white tiger",
    "white-breasted nuthatch",
    "white-spotted dolphin",
    "white-tailed deer",
    "whorled",
    "wild cat",
    "wild dog",
    "wild prairie rose",
    "wildebeest",
    "wildflowers",
    "willow",
    "wind",
    "wingnut",
    "wintergreen",
    "wisteria",
    "witchhazel",
    "wolf",
    "wolfsbane",
    "wolverine",
    "wombat",
    "wood",
    "wood louse",
    "wood nymph butterfly",
    "wood-borer",
    "woodchuck",
    "woodland caribou",
    "woodpecker",
    "woodruff",
    "woolly bear caterpillar",
    "woolly mammoth",
    "woolly rhinoceros",
    "working dog",
    "worm",
    "wren",
    "yak",
    "yam",
    "yard",
    "yeatmanite",
    "yellow mealworm",
    "yellow mongoose",
    "yellow mustard",
    "yellow-white butterfly",
    "yellowjacket",
    "yellowwood",
    "yew",
    "Yorkshire terrier",
    "yucca flower",
    "zebra",
    "zebrawood",
    "zucchini"]

for word in words:
    database.insert_word(word,False)
    
database.conn.commit()



photos=["example1.jpg","example2.jpg","example3.jpg"]

for photo in photos:
    database.insert_photo(photo,False)

database.conn.commit()
print "database created"
    
