from views.table import TextView


def app(title, intro):
    title = TextView(text=title)
    title.write_title()
    intro = TextView(text=intro)
    intro.write_text()