"""На входе ваша функция получит многострочную строку, состоящую из '0' и '#', где '0' обозначают пустые участки земли, а '#' - часть вашего дома. Ваша задача - определить площадь прямоугольного участка земли, который вам необходим, чтобы его хватило для постройки дома"""
def house(plan):
    if plan.count('#') == 1:
        return 1
    if plan.count('#') == 0:
        return 0
    m = []
    row = 0
    width = 0
    start_tochka = 0
    konec_tochka = 0
    k = plan.split()
    for i in range(len(k)):
        if '#' in k[i]:
            start_tochka = i
            break

    for i in range(len(k) - 1, -1, -1):

        if '#' in k[i]:
            konec_tochka = i
            break

    for i in range(len(k)):
        if k[i].count('#') > 1:

            c = k[i].rfind('#') - k[i].find('#')
            m.append(c)
        else:
            c = k[i].rfind('#')
            m.append(c)
    width = max(m) + 1

    row = (konec_tochka + 1) - start_tochka
    return row * width
