


define g = Character('...', color="#9fc4d6")
define gg = Character('[gg]', color="#9fc4d6")
define li = Character('Лиза', color="#ffc9e4")
define D = Character('Директор', color="#5d6ca8")
define k = Character('Коллега', color="#5da873")
define s = Character('Секретарь', color="#c036c7")





define audio.ggbomj = "audio/bomzh.mp3"
define audio.direcyli = "audio/diryl.mp3"
define audio.koffeyok = "audio/koffe.mp3"
define audio.glavmenu = "audio/menushka.mp3"
define audio.offishe = "audio/offis.mp3"
define audio.doma = "audio/xata.mp3"

define audio.xlopdver = "audio/zakrdver.mp3"
define audio.ry4ka = "audio/ryka.mp3"
define audio.shakira = "audio/shura.mp3"
define audio.tiffan = "audio/oshibo4ka.mp3"
define audio.kukold = "audio/zvon.mp3"
define audio.shumnoblyat = "audio/ALLOBLYAT.mp3"
define audio.tiktok = "audio/tuktukblyat.mp3"
define audio.hihik = "audio/hihihaha.mp3"


label start:

    play music doma

    scene bg home

    show gg home with fade

    play sound kukold

    "Вас разбудил звонок в дверь."

    g "Кто бы это мог быть? Я давно никому не звонил и не писал. С чего бы кому-то ко мне приходить?"

    "Нехотя вы надели тапки и направились к двери."
    scene bg dver with slideright
    show kurier
    "За дверью стоял курьер."
    "Он протягивает вам конверт."
    menu:
        "взять конверт":

            jump vzyal
        "не брать":
            jump nebrat


    return

label vzyal:
    scene bg home1svet
    play sound xlopdver
    show gg home with moveinleft
    "Вы взяли конверт и закрыли дверь."
    "В конверте было приглашение на работу."

    menu:
        "идти на работу":

            jump idti
        "остаться дома":
            jump doma

    return

label idti:
    scene bg home1svet
    show gg home
    "Вы решаетесь пойти на работу."

    menu:
        g "Может, стоит привести себя в порядок?"
        "собраться":
            jump umit
        "идти как есть":
            jump gryaznii
    return

label umit:
    scene bg zerkalo
    show gg umit
    "Вы умылись и подошли к шкафу, чтобы переодеться."

    menu:
        g "Что же надеть?"
        "косуха и джинсы":
            jump dzinsi
        "папина рубашка":
            jump rubashka


    return

label rubashka:
    scene bg zerkalo
    show gg umit
    g "Отец говорил, что она приносила ему удачу."
    scene bg zerkalo
    play sound shakira
    show gg rubashka with moveinbottom
    "Вы надеваете рубашку, но она оказывается вам велика."
    menu:
        "поправить":


            jump norm
        "оставить как есть":
            jump nenorm
    return

label norm:
    scene bg zerkalo
    show gg rubashka
    g "Лучше ее поправить, чтобы не мешалась."
    play sound shakira
    show gg ofis with dissolve
    "Вы заправили рубашку в брюки и аккуратно закатали рукава."
    stop music fadeout 2
    scene bg zdanie
    play music direcyli
    "Теперь вы выглядите идеально. Время идти на работу."
    scene bg direktor
    show direktor
    D "Поздравляю, вы приняты."

    D "Прошу заполните эту анкету."

    $ gg = renpy.input("Как вас зовут?", length = 20, default = "Григорий", allow = " абвгдеёжзийаклмнопрстуфхцчшщъыьэюя-АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ").strip()
    if gg =="":
        $ gg = "Григорий"
    play sound ry4ka
    D "ну что ж мистер {color=#9fc4d6}[gg]{/color}, можете начинать работу."

    stop music fadeout 2
    scene bg koridor
    play music offishe
    show tolpa1
    "Вы проходите по коридору."
    "Впереди стоят люди и о чем-то болтают."
    menu:
        "подойти, поговорить":
            jump podoiti
        "пройти на своё рабочее место":
            jump mesto
    return

label podoiti:
    scene bg koridor
    show tolpa:
        xalign 0.8
    show li norm:
        xalign 1.1
    show gg ofis with moveinleft:
        xalign 0.1
    "Вы решаетесь подойти и заговорить с вашими новыми коллегами."
    gg "З-здравствуйте."
    "Ваш голос еле слышен."
    show li hihi:
        xalign 1.1
    show gg ofis1krasn:
        xalign 0.1
    play sound hihik
    "Одна из девушек хихикнула.{w} Это заставило вас смутиться."
    hide gg ofis1krasn with moveoutleft
    scene bg mesto
    show gg ofis with moveinleft
    "Вы проходите на своё рабочее место."
    show gg ofis with easeinleft:
        xalign 0.8
    show li eh with easeinleft:
        xalign 0.2
    "К вам подходит та самая девушка."
    li "Привет. Ты не обиделся? Прости, если что. Я не хотела тебя обидеть."
    show li hi1
    li "Просто ты выглядел так забавно и мило."
    menu:
        "проигнорировать":
            jump ignor
        "кивнуть":
            jump kivok
    return

label mesto:
    scene bg mesto
    show gg ofis with moveinleft
    "Вы проходите на своё рабочее место."
    show gg ofis with easeinleft:
        xalign 0.8
    show li norm with easeinleft:
        xalign 0.2
    "К вам подходит девушка из толпы."
    li "Привет. Я – {color=#ffc9e4}{b}Лиза{/b}{/color}. Я, вроде, твоя наставница."
    menu:
        "проигнорировать":
            jump ignor
        "кивнуть":
            jump kivokeh
    return

label ignor:
    show li eh
    "Вы игнорируете девушку и продолжаете работу."
    li "Ам… Прости что отвлекла. Я, пожалуй, пойду."
    hide li eh with easeoutleft
    show gg ofis with easeinleft:
        xalign 0.5
    "Девушка ушла опечаленной."
    play sound shumnoblyat
    show kolega with moveinright:
        xalign 1.0
    $ renpy.notify("к чему это он?")
    k "Новенький, будь аккуратнее. Говорят: она – ведьма. "
    
    hide kolega with moveoutright
    "Вы киваете и вновь принимаетесь за работу."
    scene bg mesto1vecer
    play sound tiktok
    show gg ofis1ustal
    "Часа через 2 вас начинает клонить в сон."
    stop music fadeout 2
    scene bg kofe
    play music koffeyok
    show gg ofis with easeinleft:
        xalign 0.5
    "Вы встаете и направляетесь в кафетерий. "
    show gg ofis with easeinleft:
        xalign 0.8
    show li 2kofe with easeinleft:
        xalign 0.2
    "К вам снова подходит Лиза. "
    li "Как успехи? Есть какие-нибудь сложности? "
    show li 11kofe
    show gg ofis1kofe mm
    "Девушка протягивает вам кофе.{w} Вы с осторожностью берете его. "
    gg "Нет.{w} Всё нормально. "
    li "Слушай, {color=#9fc4d6}[gg]{/color}, дай мне свой номер."
    menu:
        "дать номер":
            jump nom
        "отказать":
            jump otkaz
    return

label kivok:
    show gg ofis1krasn
    "Её улыбка довольно милая. Вы аккуратно киваете."
    li "Меня {color=#ffc9e4}Лиза{/color} зовут."
    gg "{color=#9fc4d6}[gg]{/color}."
    li "Очень приятно, {color=#9fc4d6}[gg]{/color}. Я, вроде, твоя наставница, или что-то типа того. Так что – обращайся, если возникнут вопросы."
    "Вы вновь киваете."
    hide li with easeoutleft
    show gg ofis with easeinleft:
        xalign 0.5
    "Девушка уходит, улыбнувшись на прощание."
    play sound shumnoblyat
    show kolega with moveinright:
        xalign 1.0
    $ renpy.notify("к чему это он?")
    k "Новенький, будь аккуратнее. Говорят: она – ведьма."
    
    hide kolega with moveoutright
    "Вы киваете и вновь принимаетесь за работу."
    scene bg mesto1vecer
    play sound tiktok
    show gg ofis1ustal
    "Часа через 2 вас начинает клонить в сон."
    stop music fadeout 2
    scene bg kofe
    play music koffeyok
    show gg ofis with easeinleft:
        xalign 0.5
    "Вы встаете и направляетесь в кафетерий. "
    show gg ofis with easeinleft:
        xalign 0.8
    show li 2kofe with easeinleft:
        xalign 0.2
    "К вам снова подходит Лиза. "
    li "Как успехи? Есть какие-нибудь сложности? "
    show li 11kofe
    show gg ofis1kofe
    "Девушка протягивает вам кофе.{w} Вы с осторожностью берете его. "
    gg "Нет.{w} Всё нормально. "
    li "Слушай,[gg], дай мне свой номер."
    menu:
        "дать номер":
            jump nom
        "отказать":
            jump otkaz
    return

label kivokeh:
    show gg ofis1krasn
    "Её улыбка довольно милая. Вы тихо произносите."
    gg "{color=#9fc4d6}[gg]{/color}."
    li "Очень приятно, {color=#9fc4d6}[gg]{/color}. Я, вроде, твоя наставница, или что-то типа того. Так что – обращайся, если возникнут вопросы."
    "Вы вновь киваете."
    hide li with easeoutleft
    show gg ofis with easeinleft:
        xalign 0.5
    "Девушка уходит, улыбнувшись на прощание."
    play sound shumnoblyat
    show kolega with moveinright:
        xalign 1.0
    $ renpy.notify("к чему это он?")
    k "Новенький, будь аккуратнее. Говорят: она – ведьма."
    hide kolega with moveoutright
    "Вы киваете и вновь принимаетесь за работу."
    scene bg mesto1vecer
    play sound tiktok
    show gg ofis1ustal
    "Часа через 2 вас начинает клонить в сон."
    stop music fadeout 2
    scene bg kofe
    play music koffeyok
    show gg ofis with easeinleft:
        xalign 0.5
    "Вы встаете и направляетесь в кафетерий. "
    show gg ofis with easeinleft:
        xalign 0.8
    show li 2kofe with easeinleft:
        xalign 0.2
    "К вам снова подходит Лиза. "
    li "Как успехи? Есть какие-нибудь сложности? "
    show li 11kofe
    show gg ofis1kofe
    "Девушка протягивает вам кофе.{w} Вы с осторожностью берете его. "
    gg "Нет.{w} Всё нормально. "
    li "Слушай, [gg], дай мне свой номер."
    menu:
        "дать номер":
            jump nom
        "отказать":
            jump otkaz
    return

label nom:
    show gg ofis1tel
    gg "Д-да, конечно."
    "Вы рыскаете в контактах телефона в поисках собственного номера."
    "Спустя пару секунд вы диктуете его девушке."
    show li tel hehe
    li "Я напишу тебе вечером."
    show gg ofis1kofe hi
    hide li tel hehe with easeoutleft
    "Кажется, эта новость приободряет вас."
    hide gg with easeoutleft
    stop music fadeout 2
    scene bg mesto
    play music offishe
    show gg ofis with easeinright
    "Вы возвращаетесь на своё рабочее место и возобновляете работу."
    show li norm with easeinleft:
        xalign 0.3
    show gg ofis with easeinleft:
        xalign 0.7
    "Девушка почти бесшумно подходит к вам."

    li "Тебе помощь не нужна?"
    gg "Нет, спасибо, всё хорошо."
    scene bg problem
    play sound tiffan
    "На экране вашего монитора появляется ошибка. "
    scene bg mesto
    show gg ofis1am:
        xalign 0.7
    $ renpy.notify("ЧТО?")
    show li hi1:
        xalign 0.3
    li "Не волнуйся, я помогу."
    "Девушка быстро устранила проблему."
    hide li with easeoutleft
    "Она мило улыбается и уходит."
    scene bg mesto1noc
    play sound tiktok
    "Рабочий день закончен."
    stop music fadeout 2
    scene bg home1noc with fade
    play sound xlopdver
    play music doma
    "Вы возвращаетесь домой."

    return

label otkaz:
    show li 11kofe eh
    show gg ofis1kofe m
    gg "Извини, я не даю номер малознакомым людям."
    "Кажется, эти слова огорчили Лизу."
    hide li with easeoutleft
    hide gg with easeoutleft
    stop music fadeout 2
    scene bg mesto
    play music offishe
    show gg ofis with easeinright
    "Вы возвращаетесь на своё рабочее место и возобновляете работу."
    show li norm with easeinleft:
        xalign 0.3
    show gg ofis with easeinleft:
        xalign 0.7
    "Девушка почти бесшумно подходит к вам."

    li "Тебе помощь не нужна?"
    gg "Нет, спасибо, всё хорошо."
    scene bg problem
    play sound tiffan
    "На экране вашего монитора появляется ошибка. "
    scene bg mesto
    show gg ofis1rr:
        xalign 0.7

    $ renpy.notify("ВЕДЬМА!")
    show li hi1:
        xalign 0.3
    li "Не волнуйся, я помогу."
    "Девушка быстро устранила проблему."
    hide li with easeoutleft
    "Она мило улыбается и уходит."
    scene bg mesto1noc
    play sound tiktok
    "Рабочий день закончен."
    stop music fadeout 2
    scene bg home1noc with fade
    play sound xlopdver
    play music doma
    "Вы возвращаетесь домой."

    return

label nenorm:
    scene bg zerkalo
    show gg rubashka
    g "Думаю, ничего не будет, если я пойду так."
    stop music fadeout 2
    scene bg zdanie
    play music ggbomj
    "На собеседовании вы не смогли даже ручку в руки взять, из-за длинных рукавов."
    scene bad end 2 with fade
    D "Что это за внешний вид?!"
    "Вас не взяли на работу."
    return

label dzinsi:
    play sound shakira
    scene bg zerkalo
    show gg dzinsi with moveinbottom
    "Вы надели кожаную косуху и модные джинсы с дырками, и отправились на собеседование."
    stop music fadeout 2
    scene bg zdanie
    play music ggbomj
    scene bad end 2 with fade
    D "Что это за внешний вид?!"

    "Вас не взяли на работу."
    return

label gryaznii:
    scene bg home1svet
    show gg home
    g "А какой в этом смысл? На меня вряд ли кто-то обратит внимание."
    "Вы пошли на собеседование в том, в чем были."
    stop music fadeout 2
    scene bg zdanie
    play music ggbomj
    scene bad end 2 with fade
    D "Что это за внешний вид?!"

    "Вас не взяли на работу."
    return

label doma:
    scene bg home1svet
    show gg home
    "Вы не идете на работу."
    stop music fadeout 2
    scene bad end 1 with fade
    play music ggbomj
    "Вскоре вас выгнали из квартиры за неуплату. {w} Теперь вы живете на улице."
    return

label nebrat:
    scene bg dver net
    show gg home
    play sound xlopdver
    "Вы закрыли дверь перед курьером"
    stop music fadeout 2
    scene bad end 1 with fade
    play music ggbomj
    "Вскоре вас выгнали из квартиры за неуплату. {w} Теперь вы живете на улице."
    return