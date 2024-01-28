from pyscript import document

def make_mad_lib(event):
    name = document.querySelector("#name")
    name_output = name.value
    weed = document.querySelector("#weed")
    weed_output = weed.value
    crayon = document.querySelector("#crayon")
    crayon_output = crayon.value
    police = document.querySelector("#police")
    police_output = police.value
    output_div = document.querySelector("#output")
    output_div.innerHTML = f"<em>{name_output}</em>&comma; is that a {weed_output}? No&comma; this is a {crayon_output}&period; I&apos;m calling the {police_output}! <br> <a href=\"https://www.youtube.com/watch?v=g6cIYDvFS-U\" target=\"_blank\">Original Vine</a>"
