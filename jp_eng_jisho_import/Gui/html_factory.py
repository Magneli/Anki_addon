# -.- coding: utf-8 -.-


def display_search_result(widget):
    if widget.search_result.get_result_count() > 0:
        display_results(widget)
        widget.htmlarea.setHtml(makehtml(widget.search_result))
    else:
        widget.htmlarea.setHtml("wat none")


def display_results(widget):
    str = "<html> <head> <title>Result</title> </head> <body> "
    div1 = make_div_start("font-size:20px;align:justify; display: inline-block; background-color:red")
    div2 = make_div_start("font-size:20px;align:justify; display: inline-block; background-color:grey")
    div3 = make_div_start("width:%;align:justify;background-color:yellow; display: inline-block")

    wat = u'<ruby><rb>東京</rb><rp>(</rp><rt>とうきょう</rt><rp>)</rp></ruby>'

    for i in range(0, widget.search_result.get_result_count()):
        str += make_div_start(
            "height:;overflow:auto;border-style: solid;border-radius: 5px;padding:4px") + div1 + widget.search_result.get_expression_number(
            i) + make_div_end() + div2 + widget.search_result.get_reading_number(
            i) + make_div_end() + div3 + widget.search_result.get_meaning_number(
            i) + wat + "</div> </div>"

    str += "</body></html>"
    widget.htmlarea.setHtml(str)


def make_div_start(style):
    return "<div style=\"" + style + "\">"


def make_div_end():
    return "</div>"


def makehtml(search_result):
    return head() + body(search_result) + tail()


def head():
    return "<html> <head> <title>Result</title> </head> <body> \n"


numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']


def body(search_result):
    result = ""
    start = "<div style=\"display:block;border-radius:5px;margin:5px\">\n"
    table_start = "\n<table style=\"margin-left: 0px; margin-right: auto\">\n<tr>\n<td valign=\"top\">\n"
    div_start_start = "\n<div style = \"font-size:40px;background-color:#ddd;border-radius:5px; vertical-align:top ;display: inline;margin:4px;\">\n"
    div_start_end = "\n</div>\n"
    for i in range(0, search_result.get_result_count()):
        result += start + table_start+div_start_start + numbers[i] + div_start_end+"</td><td>"
        result += make_divs(search_result.get_expression_number(i), search_result.get_reading_number(i),
                            search_result.get_meaning_number(i), search_result.get_note_number(i))
    return result


def make_divs(expression, reading, meaning, note):
    end = "\n</div>\n"
    return make_expression_reading(expression, reading) + make_note_bit(note) + make_meaning_bit(
        meaning.replace('\n', "<br>")) +"\n</td>\n </tr>\n  </table>\n"+ end


def make_meaning_bit(meaning):
    return "\n<div>" + meaning + "</div></div>\n"


def make_note_bit(note):
    start = "<div style = \"font-size:15px;background-color:#fff; display: inline-block;border-radius: 5px;padding:1px\">\n"
    end = "\n</div>\n"
    return start + note + end


def make_expression_reading(expression, reading):
    start = "\n<div style = \"background-color:#ddd;display:inline-block;font-size:20px;\">\n<div>\n<div style = \"display: inline-block\">\n"
    mid = "\n</div>\n <div style = \"display: inline-block;\">\n"
    end = "\n</div> \n </div>\n\n"
    return start + expression + mid + reading + end


def tail():
    return "</body></html>"


if __name__ == "__main__":
    import sys
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from Search_handler import Jp_to_eng_word_search_handler

    searcher = Jp_to_eng_word_search_handler.Jp_to_eng_word_search_handler()

    result = searcher.search("食べる")

    print makehtml(result)
