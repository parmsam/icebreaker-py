from shiny import *
import shiny.experimental as x
from shiny import ui
import pandas as pd
import numpy as np
from pathlib import Path
import os

# Read in data
file_path = Path(__file__).parent / "data" / "icebreakers.csv"
## Read the data file using pandas
data = pd.read_csv(file_path)
# Declare paths to static assets
css_file = Path(__file__).parent / "www" / "styles.css"
js_file = Path(__file__).parent / "www" / "script.js"

# Define a function to get a random icebreaker
def random_icebreaker(data = data, replace = False, N = 1, include_difficult = False):
    # filter out difficult questions by default
    if not include_difficult:
        data = data[data["difficulty"] == False]
    # sample N rows from the data
    rand_row = data.sample(n = N, replace = replace)
    # paste each question and emoji together
    questions = rand_row["question"].values
    emojis = rand_row["emoji"].values
    return "\n".join([ "\n".join([q,e]) for q, e in zip(questions, emojis)])

# Define the app
app_ui = ui.page_fluid(
    ui.head_content(
        ui.HTML('<link rel="shortcut icon" href="/images/favicon.ico" >')   
    ),
    ui.include_css(css_file, method="link_files"),
    ui.include_js(js_file, method="link_files"),
    ui.h1("🧊 break the ice ⛏️"),
    ui.em(ui.HTML(
        "by <a href='https://github.com/parmsam/icebreaker-py/' target='_blank'>parmsam</a>")),
    ui.input_slider("obs", "pick number of icebreakers", min=0, max=5, value = 1, step = 1),
    ui.input_switch("difficulty", "include difficult questions", value = False),
    x.ui.tooltip(
        ui.input_action_button(
            "random", "randomize", 
            icon = "", class_ = "btn-primary",
        ),
        "",
    ),
    ui.br(), 
    ui.br(), 
    ui.p(
        ui.output_text_verbatim(
            "icebreaker",
            placeholder = False,
        )
    ),
    ui.panel_conditional(
        "input.random",
        ui.input_action_button(
            "copy", "copy", 
            icon = "📋", class_="btn-sm"
        ),
    )
)

def server(input, output, session):
    @reactive.Calc
    def new_question():
        input.random()
        x = random_icebreaker(
            N=input.obs(),
            include_difficult = input.difficulty()
            )
        return x

    @output
    @render.text
    @reactive.event(input.random)
    def icebreaker():
        return new_question()

app = App(app_ui, server)