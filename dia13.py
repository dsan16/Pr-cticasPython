import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import wikipedia
import datetime

def audio_a_texto():
    r = sr.Recognizer()
    with sr.Microphone() as origin:
        r.pause_threshold = 0.8

        print("Escuchando...")

        audio = r.listen(origin)

        try:
            pedido = r.recognize_google(audio, language="es-ES")
            print(f"Usuario: {pedido}\n")
            return pedido
        except sr.UnknownValueError:
            print("No he entendido lo que has dicho")
            return "Sigo escuchando..."
        except sr.RequestError:
            print("No tengo conexión a Internet")
            return "Sigo escuchando..."
        except Exception as e:
            print(f"Error: {e}")
            return "Sigo escuchando..."
        
def texto_a_audio(texto):
    engine = pyttsx3.init()

    engine.say(texto)
    engine.runAndWait()


def pedir_dia():

    dia = datetime.date.today()
    print(dia)

    dia_semana = dia.weekday()
    print(dia_semana)

    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    texto_a_audio(f'Hoy es {calendario[dia_semana]}')

def pedir_hora():

    hora = datetime.datetime.now()
    hora = f'Son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    texto_a_audio(hora)

def saludo_inicial():

    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    texto_a_audio(f'{momento}, soy su asistente personal. ¿En qué te puedo ayudar?')

def pedir_cosas():

    saludo_inicial()

    comenzar = True

    while comenzar:

        pedido = audio_a_texto().lower()

        if 'abrir youtube' in pedido:
            texto_a_audio('Abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            texto_a_audio('Abriendo navegador')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            try:
                pedido = pedido.replace('busca en wikipedia', '')
                wikipedia.set_lang('es')
                resultado = wikipedia.summary(pedido, sentences=1)
                texto_a_audio('Wikipedia dice lo siguiente:')
                texto_a_audio(resultado)
            except wikipedia.exceptions.DisambiguationError as e:
                texto_a_audio("Ese término es muy amplio. Por favor, sé más específico.")
            except wikipedia.exceptions.PageError:
                texto_a_audio("No encontré ninguna página con ese término.")
            except wikipedia.exceptions.WikipediaException as e:
                texto_a_audio("Especifíca que es lo que quieres buscar en wikipedia.")
                print("Error:", e)
            except Exception as e:
                texto_a_audio("Error inesperado al buscar.")
                print("Error general:", e)
            continue
        elif 'busca en internet' in pedido:
            try:
                pedido = pedido.replace('busca en internet', '')
                pywhatkit.search(pedido)
                texto_a_audio('Esto es lo que he encontrado')
            except Exception as e:
                print(f"Error: {e}")
            continue
        elif 'reproducir' in pedido:
            texto_a_audio('Reproduciendo video')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            texto_a_audio(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                texto_a_audio(f'El precio de las acciones de {accion} es {precio_actual}')
                continue
            except:
                texto_a_audio("Perdón pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            texto_a_audio("Adiós")
            break


pedir_cosas()