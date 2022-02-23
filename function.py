
from re import sub, search, U, IGNORECASE

LATIN_TO_CYRILLIC = {
    'a': 'а', 'A': 'А',
    'b': 'б', 'B': 'Б',
    'd': 'д', 'D': 'Д',
    'e': 'е', 'E': 'Е',
    'f': 'ф', 'F': 'Ф',
    'g': 'г', 'G': 'Г',
    'h': 'ҳ', 'H': 'Ҳ',
    'i': 'и', 'I': 'И',
    'j': 'ж', 'J': 'Ж',
    'k': 'к', 'K': 'К',
    'l': 'л', 'L': 'Л',
    'm': 'м', 'M': 'М',
    'n': 'н', 'N': 'Н',
    'o': 'о', 'O': 'О',
    'p': 'п', 'P': 'П',
    'q': 'қ', 'Q': 'Қ',
    'r': 'р', 'R': 'Р',
    's': 'с', 'S': 'С',
    't': 'т', 'T': 'Т',
    'u': 'у', 'U': 'У',
    'v': 'в', 'V': 'В',
    'x': 'х', 'X': 'Х',
    'y': 'й', 'Y': 'Й',
    'z': 'з', 'Z': 'З',
    'ʼ': 'ъ',  # TODO: case?
}
LATIN_VOWELS = (
    'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'o‘', 'O‘'
)

# These words cannot be reliably converted to cyrillic because of the lossy
# nature of the to_latin converter.
TS_WORDS = {
    'aberra(ts)ion': 'аберрацион',
    'aberra(ts)iya': 'аберрация',
    'abza(ts)': 'абзац',
    'aboli(ts)iya': 'аболиция',
    'absorb(s)iya': 'абсорбция',
    'abstrak(s)ionizm': 'абстракционизм',
    'abstrak(s)ionist': 'абстракционист',
    'abstrak(s)iya': 'абстракция',
    'abs(s)ess': 'абсцесс',
    'avianose(ts)': 'авианосец',
    'avia(ts)iya': 'авиация',
    'avtoinspek(s)iya': 'автоинспекция',
    'avtopr(s)ep': 'автопрцеп',
    'avtostan(s)iya': 'автостанция',
    'agglyutina(ts)iya': 'агглютинация',
    'agita(ts)ion': 'агитацион',
    'agita(ts)iya': 'агитация',
    'aglomera(ts)iya': 'агломерация',
    'agnosti(ts)izm': 'агностицизм',
    'agromeliora(ts)iya': 'агромелиорация',
    'adapta(ts)iya': 'адаптация',
    'administra(ts)iya': 'администрация',
    'adsorb(s)iya': 'адсорбция',
    'aka(ts)iya': 'акация',
    'akklimatiza(ts)iya': 'акклиматизация',
    'akkomoda(ts)iya': 'аккомодация',
    'akkredita(ts)iya': 'аккредитация',
    'ak(s)ent': 'акцент',
    'ak(s)iz': 'акциз',
    'ak(s)ioner': 'акционер',
    'ak(s)ionerlik': 'акционерлик',
    'ak(s)iya': 'акция',
    'ak(s)iyadorlik': 'акциядорлик',
    'allitera(ts)iya': 'аллитерация',
    'amortiza(ts)iya': 'амортизация',
    'amputa(ts)iya': 'ампутация',
    'annota(ts)iya': 'аннотация',
    'annulya(ts)iya': 'аннуляция',
    'anti(ts)iklon': 'антициклон',
    'antra(ts)it': 'антрацит',
    'apellya(ts)iya': 'апелляция',
    'appendi(ts)it': 'аппендицит',
    'applika(ts)iya': 'аппликация',
    'aproba(ts)iya': 'апробация',
    'argumenta(ts)iya': 'аргументация',
    'assimilya(ts)iya': 'ассимиляция',
    'asso(ts)ia(ts)iya': 'ассоциация',
    'attesta(ts)ion': 'аттестацион',
    'attesta(ts)iya': 'аттестация',
    'attrak(s)ion': 'аттракцион',
    'auk(s)ion': 'аукцион',
    'a(ts)etilen': 'ацетилен',
    'a(ts)eton': 'ацетон',
    'aeronaviga(ts)iya': 'аэронавигация',
    'bakteri(ts)id': 'бактерицид',
    'ba(ts)illar': 'бациллар',
    'bioloka(ts)iya': 'биолокация',
    'biolyumines(s)en(s)iya': 'биолюминесценция',
    'bo(ts)man': 'боцман',
    'bronenose(ts)': 'броненосец',
    'bru(ts)ellyoz': 'бруцеллёз',
    'vak(s)ina': 'вакцина',
    'valva(ts)iya': 'вальвация',
    'vegeta(ts)ion': 'вегетацион',
    'vegeta(ts)iya': 'вегетация',
    'venepunk(s)iya': 'венепункция',
    'ventilya(ts)ion': 'вентиляцион',
    'ventilya(ts)iya': 'вентиляция',
    'vibra(ts)iya': 'вибрация',
    'vibroizolya(ts)iya': 'виброизоляция',
    'vi(ts)e-': 'вице-',
    'vi(ts)e-admiral': 'вице-адмирал',
    'vi(ts)e-prezident': 'вице-президент',
    'vulkaniza(ts)iya': 'вулканизация',
    'galli(ts)izm': 'галлицизм',
    'gallyu(ts)ina(ts)iya': 'галлюцинация',
    'galvaniza(ts)iya': 'гальванизация',
    'gastrol-kon(s)ert': 'гастроль-концерт',
    'gaubi(ts)a': 'гаубица',
    'gelio(ts)entrik': 'гелиоцентрик',
    'geno(ts)id': 'геноцид',
    'geo(ts)entrik': 'геоцентрик',
    'gerbi(ts)idlar': 'гербицидлар',
    'ger(s)': 'герц',
    'ger(s)og': 'герцог',
    'gia(ts)int': 'гиацинт',
    'gidromeliora(ts)iya': 'гидромелиорация',
    'gidromexaniza(ts)iya': 'гидромеханизация',
    'gidrostan(s)iya': 'гидростанция',
    'gidroelektrostan(s)iya': 'гидроэлектростанция',
    'giperinflya(ts)iya': 'гиперинфляция',
    'gipo(ts)entr': 'гипоцентр',
    'gli(ts)erin': 'глицерин',
    'glya(ts)iolog': 'гляциолог',
    'glya(ts)iologiya': 'гляциология',
    'gorchi(ts)a': 'горчица',
    'gravita(ts)iya': 'гравитация',
    'grada(ts)iya': 'градация',
    'guseni(ts)a': 'гусеница',
    'devalva(ts)iya': 'девальвация',
    'degaza(ts)iya': 'дегазация',
    'degenera(ts)iya': 'дегенерация',
    'degustat(s)iya': 'дегустатция',
    'deduk(s)iya': 'дедукция',
    'dezaktiva(ts)iya': 'дезактивация',
    'dezinsek(s)iya': 'дезинсекция',
    'dezinfek(s)iya': 'дезинфекция',
    'dezinfek(s)iyalamoq': 'дезинфекцияламоқ',
    'deklama(ts)iya': 'декламация',
    'deklama(ts)iyachi': 'декламациячи',
    'deklara(ts)iya': 'декларация',
    'dekora(ts)iya': 'декорация',
    'delega(ts)iya': 'делегация',
    'delimita(ts)iya': 'делимитация',
    'demarka(ts)iya': 'демаркация',
    'demilitariza(ts)iya': 'демилитаризация',
    'demobiliza(ts)iya': 'демобилизация',
    'denaturaliza(ts)iya': 'денатурализация',
    'denomina(ts)iya': 'деноминация',
    'denonsa(ts)iya': 'денонсация',
    'depilya(ts)iya': 'депиляция',
    'deporta(ts)iya': 'депортация',
    'deratiza(ts)iya': 'дератизация',
    'deriva(ts)ion': 'деривацион',
    'deriva(ts)iya': 'деривация',
    'desika(ts)iya': 'десикация',
    'detona(ts)iya': 'детонация',
    'defini(ts)iya': 'дефиниция',
    'defi(ts)it': 'дефицит',
    'deflya(ts)iya': 'дефляция',
    'defolia(ts)iya': 'дефолиация',
    'deforma(ts)iya': 'деформация',
    'de(ts)igramm': 'дециграмм',
    'de(ts)ilitr': 'децилитр',
    'de(ts)imetr': 'дециметр',
    'dik(s)iya': 'дикция',
    'direk(s)iya': 'дирекция',
    'diskvalifika(ts)iya': 'дисквалификация',
    'diskrimina(ts)iya': 'дискриминация',
    'disloka(ts)iya': 'дислокация',
    'dispropor(s)iya': 'диспропорция',
    'disserta(ts)iya': 'диссертация',
    'dissimilya(ts)iya': 'диссимиляция',
    'disso(ts)ia(ts)iya': 'диссоциация',
    'distan(s)ion': 'дистанцион',
    'distan(s)iya': 'дистанция',
    'distillya(ts)iya': 'дистилляция',
    'differen(s)ial': 'дифференциал',
    'differen(s)ia(ts)iya': 'дифференциация',
    'differen(s)iyalamoq': 'дифференцияламоқ',
    'dota(ts)iya': 'дотация',
    'do(ts)ent': 'доцент',
    'jinoiy-pro(ts)essual': 'жиноий-процессуал',
    'identifika(ts)iya': 'идентификация',
    'izolya(ts)ion': 'изоляцион',
    'izolya(ts)iya': 'изоляция',
    'izolya(ts)iyalamoq': 'изоляцияламоқ',
    'illyumina(ts)iya': 'иллюминация',
    'illyustra(ts)iya': 'иллюстрация',
    'immigra(ts)iya': 'иммиграция',
    'immobiliza(ts)iya': 'иммобилизация',
    'impoten(s)iya': 'импотенция',
    'improviza(ts)iya': 'импровизация',
    'inaugura(ts)iya': 'инаугурация',
    'inventariza(ts)iya': 'инвентаризация',
    'investi(ts)iya': 'инвестиция',
    'ingalya(ts)iya': 'ингаляция',
    'indeksa(ts)iya': 'индексация',
    'induk(s)ion': 'индукцион',
    'induk(s)iya': 'индукция',
    'iner(s)iya': 'инерция',
    'iner(s)iyali': 'инерцияли',
    'inkvizi(ts)iya': 'инквизиция',
    'inkorpora(ts)iya': 'инкорпорация',
    'inkuba(ts)iya': 'инкубация',
    'innova(ts)iya': 'инновация',
    'inspek(s)iya': 'инспекция',
    'instar(s)iya': 'инстарция',
    'instruk(s)iya': 'инструкция',
    'ins(s)enirovka': 'инсценировка',
    'integra(ts)iya': 'интеграция',
    'intelligen(s)iya': 'интеллигенция',
    'interven(s)iya': 'интервенция',
    'interven(s)iyachi': 'интервенциячи',
    'interna(ts)ional': 'интернационал',
    'interna(ts)ionalizm': 'интернационализм',

    'interna(ts)ionalist': 'интернационалист',
    'intoksika(ts)iya': 'интоксикация',
    'intona(ts)ion': 'интонацион',
    'intona(ts)iya': 'интонация',
    'intui(ts)iya': 'интуиция',
    'infek(s)ion': 'инфекцион',
    'infek(s)iya': 'инфекция',
    'inflya(ts)iya': 'инфляция',
    'informa(ts)ion': 'информацион',
    'informa(ts)iya': 'информация',
    'inʼek(s)iya': 'инъекция',
    'irra(ts)ional': 'иррационал',
    'irriga(ts)ion': 'ирригацион',
    'irriga(ts)iya': 'ирригация',
    'kalkulya(ts)iya': 'калькуляция',
    'kal(s)iy': 'кальций',
    'kanaliza(ts)iya': 'канализация',
    'kan(s)eliyariya': 'канцелиярия',
    'kan(s)erogen': 'канцероген',
    'kan(s)ler': 'канцлер',
    'kapitaliza(ts)iya': 'капитализация',
    'kapitulya(ts)iya': 'капитуляция',
    'kassa(ts)iya': 'кассация',
    'katol(s)izm': 'католцизм',
    'kvalifika(ts)iya': 'квалификация',
    'kvar(s)': 'кварц',
    'kvar(s)it': 'кварцит',
    'kvitan(s)iya': 'квитанция',
    'kinokon(s)ert': 'киноконцерт',
    'kinos(s)enariy': 'киносценарий',
    'klassifika(ts)iya': 'классификация',
    'klassi(ts)izm': 'классицизм',
    'koali(ts)ion': 'коалицион',
    'koali(ts)iya': 'коалиция',
    'kodifika(ts)iya': 'кодификация',
    'kollek(s)ioner': 'коллекционер',
    'kollek(s)iya': 'коллекция',
    'kollek(s)iyachchi': 'коллекцияччи',
    'kolon(s)ifra': 'колонцифра',
    'kombina(ts)iya': 'комбинация',
    'kommer(s)iya': 'коммерция',
    'kommunika(ts)iya': 'коммуникация',
    'kommuta(ts)iya': 'коммутация',
    'kompensa(ts)iya': 'компенсация',
    'kompeten(s)iya': 'компетенция',
    'kompilya(ts)iya': 'компиляция',
    'kompozi(ts)ion': 'композицион',
    'kompozi(ts)iya': 'композиция',
    'konvek(s)iya': 'конвекция',
    'konven(s)iya': 'конвенция',
    'konverta(ts)iya': 'конвертация',
    'kondensa(ts)iya': 'конденсация',
    'kondi(ts)iya': 'кондиция',
    'kondi(ts)ioner': 'кондиционер',
    'konkuren(s)iya': 'конкуренция',
    'konserva(ts)iya': 'консервация',
    'konsigna(ts)iya': 'консигнация',
    'konsolida(ts)iya': 'консолидация',
    'konsor(s)ium': 'консорциум',
    'konspira(ts)iya': 'конспирация',
    'konstitu(ts)ion': 'конституцион',
    'konstitu(ts)iya': 'конституция',
    'konstitu(ts)iyaviy': 'конституциявий',
    'konstruk(s)iya': 'конструкция',
    'konsulta(ts)iya': 'консультация',
    'kontrakta(ts)iya': 'контрактация',
    'kontribu(ts)iya': 'контрибуция',
    'kontrrevolyu(ts)ion': 'контрреволюцион',
    'kontrrevolyu(ts)ioner': 'контрреволюционер',
    'kontrrevolyu(ts)iya': 'контрреволюция',
    'konfedera(ts)iya': 'конфедерация',
    'konferen(s)-zal': 'конференц-зал',
    'konferen(s)iya': 'конференция',
    'konfiska(ts)iya': 'конфискация',
    'konfronta(ts)iya': 'конфронтация',
    'konfu(ts)iylik': 'конфуцийлик',
    'konfu(ts)iychilik': 'конфуцийчилик',
    'kon(s)entrat': 'концентрат',
    'kon(s)entratli': 'концентратли',
    'kon(s)entra(ts)ion': 'концентрацион',
    'kon(s)entra(ts)iya': 'концентрация',
    'kon(s)entra(ts)iyalashmoq': 'концентрациялашмоқ',
    'kon(s)entrik': 'концентрик',
    'kon(s)ep(s)iya': 'концепция',
    'kon(s)ern': 'концерн',
    'kon(s)ert': 'концерт',
    'kon(s)ertmeyster': 'концертмейстер',
    'kon(s)essiya': 'концессия',
    'kon(s)lager': 'концлагерь',
    'koopera(ts)iya': 'кооперация',
    'koopta(ts)iya': 'кооптация',
    'koordina(ts)ion': 'координацион',
    'koordina(ts)iya': 'координация',
    'korpora(ts)iya': 'корпорация',
    'korrelya(ts)iya': 'корреляция',
    'korresponden(s)iya': 'корреспонденция',
    'korrup(s)iya': 'коррупция',
    'koeffi(ts)iyent': 'коэффициент',
    'krema(ts)iya': 'кремация',
    'kristalliza(ts)iya': 'кристаллизация',
    'kulmina(ts)ion': 'кульминацион',
    'kulmina(ts)iya': 'кульминация',
    'kultiva(ts)iya': 'культивация',
    'lakta(ts)iya': 'лактация',

    'lamina(ts)iya': 'ламинация',
    'lan(s)et': 'ланцет',
    'levomi(ts)etin': 'левомицетин',
    'legitima(ts)iya': 'легитимация',
    'leyko(ts)itlar': 'лейкоцитлар',
    'leyko(ts)itoz': 'лейкоцитоз',
    'lek(s)iya': 'лекция',
    'liberaliza(ts)iya': 'либерализация',
    'li(ts)ey': 'лицей',
    'li(ts)enziya': 'лицензия',
    'lokaliza(ts)iya': 'локализация',
    'loka(ts)iya': 'локация',
    'lo(ts)man': 'лоцман',
    'lyumenis(s)en(s)iya': 'люменисценция',
    'lyute(ts)iy': 'лютеций',
    'manipulya(ts)iya': 'манипуляция',
    'margane(ts)': 'марганец',
    'matri(ts)a': 'матрица',
    'medi(ts)ina': 'медицина',
    'meliora(ts)iya': 'мелиорация',
    'menstrua(ts)iya': 'менструация',
    'metalliza(ts)iya': 'металлизация',
    'metiza(ts)iya': 'метизация',
    'mexaniza(ts)iya': 'механизация',
    'mexaniza(ts)iyalash': 'механизациялаш',
    'mexaniza(ts)iyalashmoq': 'механизациялашмоқ',
    'mexani(ts)izm': 'механицизм',
    'migra(ts)iya': 'миграция',
    'mizans(s)ena': 'мизансцена',
    'militariza(ts)iya': 'милитаризация',
    'mili(ts)ioner': 'милиционер',
    'mili(ts)iya': 'милиция',
    'mili(ts)iyaxona': 'милицияхона',
    'mineraliza(ts)iya': 'минерализация',
    'minonose(ts)': 'миноносец',
    'misti(ts)izm': 'мистицизм',
    'mobiliza(ts)iya': 'мобилизация',
    'moderniza(ts)iya': 'модернизация',
    'moderniza(ts)iyalamoq': 'модернизацияламоқ',
    'modifika(ts)iya': 'модификация',
    'moto(ts)ikl': 'мотоцикл',
    'moto(ts)iklet': 'мотоциклет',
    'moto(ts)ikletchi': 'мотоциклетчи',
    'moto(ts)iklli': 'мотоциклли',
    'moto(ts)iklchi': 'мотоциклчи',
    'multiplika(ts)ion': 'мультипликацион',
    'multiplika(ts)iya': 'мультипликация',
    'muni(ts)ipaliza(ts)iya': 'муниципализация',
    'muni(ts)ipalitet': 'муниципалитет',
    'naviga(ts)iya': 'навигация',
    'naturaliza(ts)iya': 'натурализация',
    'na(ts)ionaliza(ts)iya': 'национализация',
    'nene(ts)': 'ненец',
    'nene(ts)lar': 'ненецлар',
    'nitrogli(ts)erin': 'нитроглицерин',
    'nomina(ts)iya': 'номинация',
    'nostrifika(ts)iya': 'нострификация',
    'nullifika(ts)iya': 'нуллификация',
    'obliga(ts)iya': 'облигация',
    'obroga(ts)iya': 'оброгация',
    'observa(ts)iya': 'обсервация',
    'okkupa(ts)ion': 'оккупацион',
    'okkupa(ts)iya': 'оккупация',
    'okkupa(ts)iyachi': 'оккупациячи',
    'opera(ts)iya': 'операция',
    'opera(ts)iyaviy': 'операциявий',
    'oppozo(ts)ion': 'оппозоцион',
    'oppozi(ts)iya': 'оппозиция',
    'oppozi(ts)iyachi': 'оппозициячи',
    'op(s)ion': 'опцион',
    'ordinare(ts)': 'ординарец',
    'oriyenta(ts)iya': 'ориентация',
    'osteomalya(ts)iya': 'остеомаляция',
    'ofi(ts)er': 'офицер',
    'ofi(ts)iant': 'официант',
    'ofi(ts)iantka': 'официантка',
    'palpa(ts)iya': 'пальпация',
    'pa(ts)iyent': 'пациент',
    'pa(ts)ifizm': 'пацифизм',
    'pa(ts)ifist': 'пацифист',
    'peni(ts)(s)ilin': 'пениццилин',
    'pesti(ts)idlar': 'пестицидлар',
    'peti(ts)iya': 'петиция',
    'petli(ts)a': 'петлица',
    'pigmenta(ts)iya': 'пигментация',
    'pin(s)et': 'пинцет',
    'pi(ts)(s)a': 'пицца',
    'planta(ts)iya': 'плантация',
    'pla(ts)darm': 'плацдарм',
    'pla(ts)kart': 'плацкарт',
    'pla(ts)karta': 'плацкарта',
    'pla(ts)kartali': 'плацкартали',
    'plebis(s)it': 'плебисцит',
    'podstan(s)iya': 'подстанция',
    'pozi(ts)ion': 'позицион',
    'pozi(ts)iya': 'позиция',
    'poli(ts)iya': 'полиция',
    'poli(ts)iyachi': 'полициячи',
    'poli(ts)meyster': 'полицмейстер',
    'pollyu(ts)iya': 'поллюция',
    'populya(ts)iya': 'популяция',
    'por(s)iya': 'порция',
    'poten(s)ial': 'потенциал',
    'prezenta(ts)iya': 'презентация',
    'press-konferen(s)iya': 'пресс-конференция',
    'preferen(s)iya': 'преференция',
    'privatiza(ts)iya': 'приватизация',
    'prin(s)ip': 'принцип',

    'prin(s)ipial': 'принципиал',
    'prin(s)ipiallik': 'принципиаллик',
    'prin(s)ipli': 'принципли',
    'prin(s)ipsiz': 'принципсиз',
    'pri(ts)ep': 'прицеп',
    'provin(s)ializm': 'провинциализм',
    'provin(s)iya': 'провинция',
    'provoka(ts)iya': 'провокация',
    'proyek(s)iya': 'проекция',
    'proyek(s)iyalamoq': 'проекцияламоқ',
    'proklama(ts)iya': 'прокламация',
    'prolonga(ts)iya': 'пролонгация',
    'propor(s)ional': 'пропорционал',
    'propor(s)ionallik': 'пропорционаллик',
    'propor(s)iya': 'пропорция',
    'protek(s)ionizm': 'протекционизм',
    'pro(ts)ent': 'процент',
    'pro(ts)entli': 'процентли',
    'pro(ts)entchi': 'процентчи',
    'pro(ts)ess': 'процесс',
    'pro(ts)essor': 'процессор',
    'pro(ts)essual': 'процессуал',
    'publi(ts)ist': 'публицист',
    'publi(ts)istik': 'публицистик',
    'publi(ts)istika': 'публицистика',
    'punktua(ts)ion': 'пунктуацион',
    'punktua(ts)iya': 'пунктуация',
    'punk(s)iya': 'пункция',
    'radia(ts)ion': 'радиацион',
    'radia(ts)iya': 'радиация',
    'radioloka(ts)iya': 'радиолокация',
    'radionaviga(ts)iya': 'радионавигация',
    'radiostan(s)iya': 'радиостанция',
    'rane(ts)': 'ранец',
    'ratifika(ts)iya': 'ратификация',
    'rafina(ts)iya': 'рафинация',
    'rafina(ts)iyalash': 'рафинациялаш',
    'ra(ts)ion': 'рацион',
    'ra(ts)ional': 'рационал',
    'ra(ts)ionalizator': 'рационализатор',
    'ra(ts)ionalizatorlik': 'рационализаторлик',
    'ra(ts)ionaliza(ts)iya': 'рационализация',
    'ra(ts)ionalizm': 'рационализм',
    'ra(ts)ionalist': 'рационалист',
    'ra(ts)ionlallashmoq': 'рационлаллашмоқ',
    'ra(ts)iya': 'рация',
    'reabilita(ts)iya': 'реабилитация',
    'reak(s)ion': 'реакцион',
    'reak(s)ioner': 'реакционер',
    'reak(s)iya': 'реакция',
    'reak(s)iyachi': 'реакциячи',
    'realiza(ts)iya': 'реализация',
    'reanima(ts)iya': 'реанимация',
    'revalva(ts)iya': 'ревальвация',
    'revolyu(ts)ion': 'революцион',
    'revolyu(ts)ioner': 'революционер',
    'revolyu(ts)iya': 'революция',
    'regenera(ts)iya': 'регенерация',
    'registra(ts)iya': 'регистрация',
    'redak(s)ion': 'редакцион',
    'redak(s)iya': 'редакция',
    'reduk(s)iya': 'редукция',
    'reduplika(ts)iya': 'редупликация',
    'rezek(s)iya': 'резекция',
    'reziden(s)iya': 'резиденция',
    'rezolyu(ts)iya': 'резолюция',
    'reinvesti(ts)iya': 'реинвестиция',
    'rekvizi(ts)iya': 'реквизиция',
    'reklama(ts)iya': 'рекламация',
    'rekognos(s)irovka': 'рекогносцировка',
    'rekomenda(ts)iya': 'рекомендация',
    'rekonstruk(s)iya': 'реконструкция',
    'rekonstruk(s)iyalamoq': 'реконструкцияламоқ',
    'remilitariza(ts)iya': 'ремилитаризация',
    'repara(ts)iya': 'репарация',
    'repatri(ts)iya': 'репатриция',
    'repeti(ts)iya': 'репетиция',
    'reprivatiza(ts)iya': 'реприватизация',
    'reproduk(s)iya': 'репродукция',
    'restavra(ts)iya': 'реставрация',
    'retranslya(ts)iya': 'ретрансляция',
    'reforma(ts)iya': 'реформация',
    'refrak(s)iya': 'рефракция',
    're(ts)enzent': 'рецензент',
    're(ts)enziya': 'рецензия',
    're(ts)ept': 'рецепт',
    're(ts)eptorlar': 'рецепторлар',
    're(ts)idiv': 'рецидив',
    're(ts)idivist': 'рецидивист',
    're(ts)ipiyent': 'реципиент',
    'reevakua(ts)iya': 'реэвакуация',
    'reemigra(ts)iya': 'реэмиграция',
    'ri(ts)arlik': 'рицарлик',
    'ri(ts)ar': 'рицарь',
    'rota(ts)ion': 'ротацион',
    'sana(ts)iya': 'санация',
    'sana(ts)iyalash': 'санациялаш',
    'sank(s)iya': 'санкция',
    'sekre(ts)iya': 'секреция',
    'sek(s)iya': 'секция',
    'selek(s)ion': 'селекцион',
    'selek(s)iya': 'селекция',
    'selek(s)iyachi': 'селекциячи',
    'selek(s)iyachilik': 'селекциячилик',
    'sensa(ts)ion': 'сенсацион',
    'sensa(ts)iya': 'сенсация',
    'signaliza(ts)iya': 'сигнализация',

    'sili(ts)iy': 'силиций',
    'situa(ts)iya': 'ситуация',
    'skepti(ts)izm': 'скептицизм',
    'slane(ts)': 'сланец',
    'so(ts)ial': 'социал',
    'so(ts)ial-demokrat': 'социал-демократ',
    'so(ts)ial-demokratik': 'социал-демократик',
    'so(ts)ial-demokratiya': 'социал-демократия',
    'so(ts)ializa(ts)iya': 'социализация',
    'so(ts)ializm': 'социализм',
    'so(ts)ialist': 'социалист',
    'so(ts)ialistik': 'социалистик',
    'so(ts)iolingvistika': 'социолингвистика',
    'so(ts)iolog': 'социолог',
    'so(ts)iologik': 'социологик',
    'so(ts)iologiya': 'социология',
    'spekulya(ts)iya': 'спекуляция',
    'spe(ts)ifik': 'специфик',
    'spe(ts)ifika': 'специфика',
    'spe(ts)ifika(ts)iya': 'спецификация',
    'stabiliza(ts)iya': 'стабилизация',
    'stan(s)iya': 'станция',
    'sta(ts)ionar': 'стационар',
    'steriliza(ts)iya': 'стерилизация',
    'stoi(ts)izm': 'стоицизм',
    'stron(s)iy': 'стронций',
    'substan(s)iya': 'субстанция',
    's(s)enariy': 'сценарий',
    's(s)enariychi': 'сценарийчи',
    's(s)enarist': 'сценарист',
    'tabli(ts)a': 'таблица',
    'tan(s)a': 'танца',
    'teleins(s)enirovka': 'телеинсценировка',
    'telekommunika(ts)iya': 'телекоммуникация',
    'telemexaniza(ts)iya': 'телемеханизация',
    'tenden(s)ioz': 'тенденциоз',
    'tenden(s)iozlik': 'тенденциозлик',
    'tenden(s)iya': 'тенденция',
    'tepli(ts)a': 'теплица',
    'teploizolya(ts)iya': 'теплоизоляция',
    'termoizolya(ts)iya': 'термоизоляция',
    'ter(s)et': 'терцет',
    'ter(s)iya': 'терция',
    'texne(ts)iy': 'технеций',
    'tradi(ts)ion': 'традицион',
    'tradi(ts)iya': 'традиция',
    'transkrip(s)ion': 'транскрипцион',
    'transkrip(s)iya': 'транскрипция',
    'transkrip(s)iyalamoq': 'транскрипцияламоқ',
    'translitera(ts)iya': 'транслитерация',
    'translya(ts)ion': 'трансляцион',
    'translya(ts)iya': 'трансляция',
    'transplanta(ts)iya': 'трансплантация',
    'transforma(ts)iya': 'трансформация',
    'transforma(ts)iyalamoq': 'трансформацияламоқ',
    'trape(ts)iya': 'трапеция',
    'trepana(ts)iya': 'трепанация',
    'uborshi(ts)a': 'уборшица',
    'uzurpa(ts)iya': 'узурпация',
    'unifika(ts)iya': 'унификация',
    'unifika(ts)iyalashtirmoq': 'унификациялаштирмоқ',
    'unter-ofi(ts)er': 'унтер-офицер',
    'urbaniza(ts)iya': 'урбанизация',
    'fago(ts)it': 'фагоцит',
    'falsifika(ts)iya': 'фальсификация',
    'farma(ts)evt': 'фармацевт',
    'farma(ts)evtika': 'фармацевтика',
    'farma(ts)iya': 'фармация',
    'federa(ts)iya': 'федерация',
    'fermenta(ts)iya': 'ферментация',
    'film-kon(s)ert': 'фильм-концерт',
    'filtra(ts)iya': 'фильтрация',
    'fiton(s)id': 'фитонцид',
    'forma(ts)iya': 'формация',
    'frak(s)ion': 'фракцион',
    'frak(s)iooner': 'фракциоонер',
    'frak(s)iya': 'фракция',
    'fran(s)iya': 'франция',
    'fran(s)uz': 'француз',
    'fran(s)uzlar': 'французлар',
    'fran(s)uzcha': 'французча',
    'fri(ts)': 'фриц',
    'funk(s)ional': 'функционал',
    'funk(s)iya': 'функция',
    'xemosorb(s)iya': 'хемосорбция',
    'xole(ts)istit': 'холецистит',
    '(s)anga': 'цанга',
    '(s)apfa': 'цапфа',
    '(s)edra': 'цедра',
    '(s)eziy': 'цезий',
    '(s)eytnot': 'цейтнот',
    '(s)ellofan': 'целлофан',
    '(s)elluloid': 'целлулоид',
    '(s)ellyuloza': 'целлюлоза',
    '(s)elsiy': 'цельсий',
    '(s)ement': 'цемент',
    '(s)ementlamoq': 'цементламоқ',
    '(s)enz': 'ценз',
    '(s)enzor': 'цензор',
    '(s)enzura': 'цензура',
    '(s)ent': 'цент',
    '(s)entner': 'центнер',
    '(s)entnerli': 'центнерли',
    '(s)entnerchi': 'центнерчи',
    '(s)entralizm': 'централизм',
    '(s)entrizm': 'центризм',
    '(s)entrist': 'центрист',
    '(s)entrifuga': 'центрифуга',
    '(s)eriy': 'церий',
    '(s)esarka': 'цесарка',
    '(s)ex': 'цех',
    '(s)ian': 'циан',

    '(s)ianli': 'цианли',
    '(s)iviliza(ts)iya': 'цивилизация',
    '(s)igara': 'цигара',
    '(s)ikl': 'цикл',
    '(s)iklik': 'циклик',
    '(s)ikllashtirmoq': 'цикллаштирмоқ',
    '(s)iklli': 'циклли',
    '(s)iklon': 'циклон',
    '(s)iklotron': 'циклотрон',
    '(s)ilindr': 'цилиндр',
    '(s)ilindrik': 'цилиндрик',
    '(s)ilindrli': 'цилиндрли',
    '(s)inga': 'цинга',
    '(s)ink': 'цинк',
    '(s)inkograf': 'цинкограф',
    '(s)inkografiya': 'цинкография',
    '(s)irk': 'цирк',
    '(s)irkoniy': 'цирконий',
    '(s)irkul': 'циркуль',
    '(s)irkulyar': 'циркуляр',
    '(s)irkchi': 'циркчи',
    '(s)irroz': 'цирроз',
    '(s)isterna': 'цистерна',
    '(s)isternali': 'цистернали',
    '(s)istit': 'цистит',
    '(s)itata': 'цитата',
    '(s)itatabozlik': 'цитатабозлик',
    '(s)ito-': 'цито-',
    '(s)itodiagnostika': 'цитодиагностика',
    '(s)itokimyo': 'цитокимё',
    '(s)itoliz': 'цитолиз',
    '(s)itologiya': 'цитология',
    '(s)itrus': 'цитрус',
    '(s)iferblat': 'циферблат',
    '(s)iferblatli': 'циферблатли',
    '(s)okol': 'цоколь',
    '(s)unami': 'цунами',
    'cherepi(ts)a': 'черепица',
    'shvey(s)ar': 'швейцар',
    'shmu(ts)titul': 'шмуцтитул',
    'shni(ts)el': 'шницель',
    'shpri(ts)': 'шприц',
    'shtangen(s)irkul': 'штангенциркуль',
    'evakua(ts)iya': 'эвакуация',
    'evolyu(ts)ion': 'эволюцион',
    'evolyu(ts)iya': 'эволюция',
    'ego(ts)entrizm': 'эгоцентризм',
    'eksguma(ts)iya': 'эксгумация',
    'ekspedi(ts)ion': 'экспедицион',
    'ekspedi(ts)iya': 'экспедиция',
    'ekspedi(ts)iyachi': 'экспедициячи',
    'ekspluata(ts)iya': 'эксплуатация',
    'ekspluata(ts)iyachi': 'эксплуатациячи',
    'ekspozi(ts)iya': 'экспозиция',
    'ekspropria(ts)iya': 'экспроприация',
    'ekstradi(ts)iya': 'экстрадиция',
    'ekstrak(s)iya': 'экстракция',
    'elektrifika(ts)iya': 'электрификация',
    'elektrostan(s)iya': 'электростанция',
    'emansipa(ts)iya': 'эмансипация',
    'emigra(ts)iya': 'эмиграция',
    'emo(ts)ional': 'эмоционал',
    'emo(ts)ionallik': 'эмоционаллик',
    'emo(ts)iya': 'эмоция',
    'empiriokriti(ts)izm': 'эмпириокритицизм',
    'en(s)efalit': 'энцефалит',
    'en(s)efalogramma': 'энцефалограмма',
    'en(s)iklopedik': 'энциклопедик',
    'en(s)iklopedist': 'энциклопедист',
    'en(s)iklopediya': 'энциклопедия',
    'en(s)iklopediyachi': 'энциклопедиячи',
    'epi(ts)entr': 'эпицентр',
    'eritro(ts)itlar': 'эритроцитлар',
    'erudi(ts)iya': 'эрудиция',
    'eskala(ts)iya': 'эскалация',
    'esmine(ts)': 'эсминец',
    'essen(s)iya': 'эссенция',
    'yurisdik(s)iya': 'юрисдикция',
    'yurispruden(s)iya': 'юриспруденция',
    'yusti(ts)iya': 'юстиция',
}
# These words cannot be reliably transliterated into cyrillic
E_WORDS = {
    'bel(e)taj': 'бельэтаж',
    'bugun-(e)rta': 'бугун-эрта',
    'diqqat-(e)ʼtibor': 'диққат-эътибор',
    'ich-(e)t': 'ич-эт',
    'karat(e)': 'каратэ',
    'm(e)r': 'мэр',
    'obro\'-(e)ʼtiborli': 'обрў-эътиборли',
    'omon-(e)son': 'омон-эсон',
    'r(e)ket': 'рэкет',
    'sut(e)mizuvchilar': 'сутэмизувчилар',
    'upa-(e)lik': 'упа-элик',
    'xayr-(e)hson': 'хайр-эҳсон',
    'qayn(e)gachi': 'қайнэгачи',
}

SOFT_SIGN_WORDS = {
    'aviamodel': 'авиамодель',
    'avtomagistralavtomat': 'автомагистральавтомат',
    'avtomobil': 'автомобиль',
    'akvarel': 'акварель',
    'alkogol': 'алкоголь',
    'albatros': 'альбатрос',
    'albom': 'альбом',
    'alpinizm': 'альпинизм',
    'alpinist': 'альпинист',
    'alt': 'альт',
    'alternativ': 'альтернатив',
    'alternativa': 'альтернатива',
    'altimetr': 'альтиметр',
    'altchi': 'альтчи',
    'alfa': 'альфа',
    'alfa-zarralar': 'альфа-зарралар',
    'alma-terapiya': 'альма-терапия',
    'alyans': 'альянс',
    'amalgama': 'амальгама',
    'ansambl': 'ансамбль',
    'apelsin': 'апельсин',
    'aprel': 'апрель',
    'artel': 'артель',
    'artikl': 'артикль',
    'arergard': 'арьергард',
    'asfalt': 'асфальт',
    'asfaltlamoq': 'асфальтламоқ',
    'asfaltli': 'асфальтли',
    'atele': 'ателье',
    'bazalt': 'базальт',
    'balzam': 'бальзам',
    'balzamlash': 'бальзамлаш',
    'balneolog': 'бальнеолог',
    'balneologik': 'бальнеологик',
    'balneologiya': 'бальнеология',
    'balneoterapiya': 'бальнеотерапия',
    'balneotexnika': 'бальнеотехника',
    'banderol': 'бандероль',
    'barelef': 'барельеф',
    'barrel': 'баррель',
    'barer': 'барьер',
    'batalon': 'батальон',
    'belveder': 'бельведер',
    'belgiyalik': '
