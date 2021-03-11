import autopy as ap

# a = ap.mouse.location()


def mensagem(mensagem_value):
    ap.mouse.move(1168, 707)
    ap.mouse.click()
    ap.key.type_string(mensagem_value)
    ap.mouse.move(1264, 707)
    ap.mouse.click()
