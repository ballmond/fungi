from fasthtml.common import *
css = Style(':root {--pico-font-size:90%,--pico-font-family: Pacifico, cursive;}')
app = FastHTML(hdrs=(picolink, css))


@app.route("/")
def get():
    return (Title("Wood decay fungi"), 
            Main(
              Table(Tbody(Tr(
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170082/fungi/birds_nest_shywg6.jpg", alt="birds nest")),
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
                     A("Introduction", href="/introduction"), " | ", A("Shape Key", href="/shape-key"), " | ", A("Species List", href="/species-list"),
                     align="center")),
                  ),),width="100%", border="0",),
              Table(Tbody(Tr(
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170080/fungi/jelly_su2tey.jpg", alt="jelly")),
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170079/fungi/poroid_cxzog7.jpg", alt="poroid")),
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170079/fungi/puffball_wfzekp.jpg", alt="puffball")),
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170079/fungi/spines_and_teeth_ef49yh.jpg", alt="spines and teeth")),
                  Td(Img(src="https://res.cloudinary.com/dptfyzzyl/image/upload/v1731170079/fungi/stinkhorn_m1iinf.jpg", alt="stinkhorn")),
                  ),),width="100%", border="0",),
            cls="container"
            )
          )

@app.route("/introduction")
def get():
  return

@app.route("/shape-key")
def get():
  return

@app.route("/species-list")
def get():
  return

serve()