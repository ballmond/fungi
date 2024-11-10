from fasthtml.common import *
css = Style(':root {--pico-font-size:90%,--pico-font-family: Pacifico, cursive;}')
app = FastHTML(hdrs=(picolink, css))

def home():
   return Table(Tbody(Tr(
            Td(Div(
                A("Home", href="/"), 
                align="center")),
            ),),width="100%", border="0",),

@app.route("/")
def get():
    return (Title("Wood decay fungi"), 
            Main(
              Table(Tbody(Tr(
                  Td(Div(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170082/fungi/birds_nest_shywg6.jpg", alt="birds nest")), data_tooltip="birds nest"),
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170081/fungi/coral_qtnnex.jpg", alt="coral")),
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170081/fungi/crust_and_parchment_ulle4s.jpg", alt="crust and parchment")),
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170081/fungi/cup_and_saucer_dlst0o.jpg", alt="cup and saucer")),
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170080/fungi/gilled_rfqxpo.jpg", alt="grilled")),
                  ),),width="100%", border="0",),
              H1('Fungi Growing on Wood', align="center"),
              P('Keys, photographs, and descriptions of macroscopic fungi utilizing wood as a substrate in', Br(), 'northeastern North America', align="center"),
              P('by Gary Emberger', align="center"),
              Table(Tbody(Tr(
                  Td(Div(
                     A("Introduction", data_tooltip="Introduction", href="/introduction"), " | ", A("Shape Key", href="/shape-key"), " | ", A("Species List", href="/species-list"),
                     align="center")),
                  ),),width="100%", border="0",),
              Table(Tbody(Tr(
                  Td(Div(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170080/fungi/jelly_su2tey.jpg", alt="jelly")), data_tooltip="jelly"),
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170079/fungi/poroid_cxzog7.jpg", alt="poroid", data_tooltip="poroid")),
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170079/fungi/puffball_wfzekp.jpg", alt="puffball")),
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170079/fungi/spines_and_teeth_ef49yh.jpg", alt="spines and teeth")),
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170079/fungi/stinkhorn_m1iinf.jpg", alt="stinkhorn")),
                  ),),width="100%", border="0",),
            cls="container"
            )
          )

@app.route("/introduction")
def get():
  return (
     Main(
        H1("Introduction", align="center"),
        P(Strong("Purpose"), ": Fungi Growing on Wood  is a web site devoted to the identification and appreciation of fungi growing in close association with living trees,  dead  trees, and woody debris. These important organisms are commonly called lignicolous fungi.", align="left"),
        P(Strong("Area of Usefulness"), ": The  keys are useful for identifying fungi in Northeastern North America. As with all regional keys, coverage  decreases toward the periphery of the specified range. However, many of the species included in this site are more widely distributed than the indicated area.", align="left"),
        P(Strong("Approach to Identification"), ": Identification of lignicolous fungi at  this site requires the use of dichotomous keys. Such keys require the user to observe and identify macroscopic characters of the unknown fungus in order to make choices between alternative possibilities. A glossary is provided to illustrate and define the characteristics used in the keys.", align="left"),
        P(Strong("Restriction to lignicolous fungi"), ": The keys work only for parasitic and saprotrophic fungal species found on wood. This restricted focus simplifies the identification process because the many, many nonlignicolous species are excluded from the keys.", align="left"),
        P(Strong("More Information"), ": The menu below provides links to more information about the website including guidelines for using dichotomous keys, information on the importance of lignicolous fung, and a glossary illustrating many of the macroscopic features of fungi used in the keys.", align="left"),
        Table(Tbody(Tr(
            Td(Div(
                A("Home", href="/"), " | ", A("Shape Key", href="/shape-key"),
                align="center")),
            ),),width="100%", height="auto", border="0",),
        cls="container")
  )

@app.route("/shape-key")
def get():
  return (
     Main(
        H1("Key to Shapes", align="center"),
        P("To begin keying, compare the specimen at hand to the illustrated and described shape categories  below. After determining the best fit, go to the dichotomous key for that category  to continue the identification process. Bear in mind that only one picture is used here to illustrate an entire group. Pay as much attention to the description as to the single image. Once you are more familiar with the shape categories, you can go directly to the keys via the menu below.", align="center"),
        Table(Tbody(
           Tr(
            Td(Div(
                A("Bird's nest", href="/"),
                " | ", 
                A("Club, coral, leafy", href="/"),
                " | ", 
                A("Crust and parchment", href="/"),
                " | ", 
                A("Cup and saucher", href="/"),
                " | ", 
                A("Gilled", href="/"),
                align="center")),
            ),
           Tr(
            Td(Div(
                A("Jelly", href="/"),
                " | ", 
                A("Poroid", href="/"),
                " | ", 
                A("Puffball and cushion", href="/"),
                " | ", 
                A("Stinkhorn", href="/"),
                " | ", 
                A("Teeth and spine", href="/"),
                align="center")),
            ),
          ),width="100%", height="auto", border="0",),
        Table(Tbody(
           Tr(
            Td(H3("Example")),
            Td(H3("Shape Category")),
            Td(H3("Description")),
            ),
           Tr(
            Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170082/fungi/birds_nest_shywg6.jpg", alt="birds nest")),
            Td(Strong("Bird's Nest"), Br(), A("Key", href="/"), Br(), A("Species List", href="/")),
            Td("These fungi look like miniature bird's nests with egg-shaped structures inside called peridioles. Bird's nest fungi are small, only 0.5 to 1 cm in diameter. Drops of water splash the peridioles out of the cups, dispersing the fungus."),
            ),
          ),width="100%", height="auto", border="5", bordercolor="00FF00"),
          home(),
        cls="container")
  )

@app.route("/species-list")
def get():
  return (
     Main(
        H1("Alphabetical Species List", align="center"),
        Div(
          P("Species in this list may also be viewed in their ", A("taxonomic classification", ".", href="/")),
        ),
        home(),
        cls="container")
  )

serve()