# icebreaker-py

Simple icebreaker app for conference or group events built using Shiny for Python

## app links

- [Github pages](https://parmsam.github.io/icebreaker-py/site)

## app deployment

- Command to generate site from within directory: `shinylive export . site --full-shinylive`

## dataset

- `data/icebreaker.csv` generated using ChatGPT.

## notes

- Copy button is disabled b/c Python 3 wheel issues for `pyperclip`. It does not appear to be [currently supported by shinylive](https://shiny.posit.co/py/docs/shinylive.html#installed-packages).