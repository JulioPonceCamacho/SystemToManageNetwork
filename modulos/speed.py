import os
from time import sleep
import subprocess as sb
from pyautogui import hotkey
from datetime import datetime as dt
class speed():
    def __init__(self) -> None:
        pass
    def Velocidad_Internet(self,inf):
        intentos=0
        while intentos<3:
            shell_cmd = sb.run(["modulos/SpeedTest/speedtest.exe"], capture_output=True, text=True)
            command_output=(shell_cmd.stdout)
            if "FAILED" not in str(command_output):
                break
            else:
                print("Error, reintentando: "+str(intentos))
                intentos+=1
        if intentos==3:
            inf.Errores.append([f"{dt.now().hour}:{dt.now().minute}",inf.SSID,f"La red tiene latencia alta, todas las pruebas terminaron en error."])
        elif intentos>0:
            inf.Errores.append([f"{dt.now().hour}:{dt.now().minute}",inf.SSID,f"La red tiene latencia alta, hubo {intentos} reintentos de la prueba."])
        if intentos<3:
            command_output=command_output.replace("             ","-*")
            command_output=command_output.replace(" ","")
            aux=str(command_output).split("\n")
            sin=""
            PingD=""
            PingB=""
            for i in aux:
                if "Server:" in i:
                    Host=i.replace("Server:","")
                elif "ISP:" in i:
                    Sponsor=i.replace("ISP: ","")
                elif "Download:" in i:
                    a=i.replace("Download:","")
                    a2=a.split("Mbps")
                    dwnl=a2[0]
                    sin="d"
                elif "Upload:" in i:
                    a=i.replace("Upload:","")
                    a2=a.split("Mbps")
                    upl=a2[0]
                    sin="b"
                elif "-*" in i:
                    if sin=="d":
                        a=i.replace("-*","").split("ms")
                        PingD=a[0]
                    elif sin =="b":
                        a=i.replace("-*","").split("ms")
                        PingB=a[0]
            ping=str(round((float(PingB)+float(PingD))/2,2))
            return dwnl, upl, PingD,PingB, ping, Host,Sponsor
        else:
            return "0", "0", "0","0", "0", "Error de alta latencia.","Error."
    def velocidad_Todo(self,obj,senal,inf,listo):
        hotkey("win", "a")
        redes= sb.run(["netsh", "wlan", "show","profile"], capture_output=True, text=True).stdout
        ls=redes.split("\n")
        for i in ls:
            if ":" in i  and "actual" not in i and "current" not in i:
                aux=i.split(":")[1]
                aux=aux.strip()
                if aux!="":
                    intentos=0
                    while intentos<3:
                        conexion=os.system(f'''cmd /c "netsh wlan connect name="{aux}"''')
                        if conexion==0:
                            break
                        else:
                            intentos+=1
                        sleep(1)
                    if conexion==0:
                        print("Conectado: "+aux)
                        sleep(5)
                        try:
                            obj.velocidad=self.Velocidad_Internet(inf)
                            senal.emit(1)
                        except:
                            inf.Errores.append([f"{dt.now().hour}:{dt.now().minute}",aux,"Ocurrio un error con red y no se completo la prueba."])
                    else:
                        now = dt.now()
                        inf.Errores.append([f"{now.hour}:{now.minute}",aux,"No disponible"])
                    sleep(5)
        listo.emit(1)

                    