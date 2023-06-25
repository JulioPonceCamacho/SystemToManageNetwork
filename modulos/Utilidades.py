import socket
import modulos.Redes
from re import match
from time import sleep
import subprocess as sb
rs=modulos.Redes.Redes() 
########################## Utilidades Varias
class Utilidades():
    def __init__(self) -> None:
        pass
    def validar_MAC(self,mac):
        if match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
            return True
        else:
            return False
    def validarNumero(self,numero):
        try:
            aux=float(numero)
            return True
        except:
            return False

    def comandos(self,cmd):
        shell_cmd = sb.run((cmd), capture_output=True, text=True)
        command_output=(shell_cmd.stdout)
        return str(command_output)
    def FormatoHTML(self,var):
        var=var.replace("\n","<br>")
        var=var.replace(" ","&nbsp;")  
        var=var.replace("\s","&nbsp;")
        var=var.replace("\t","&nbsp;&nbsp;&nbsp;&nbsp;")
        var=var.replace(".","<font color='MediumSeaGreen'>.</font>")
        var=var.replace(":","<font color='MediumSeaGreen'>:</font>")
        var=var.replace("IPv4","<font color='cyan'>IPv4</font>")
        var=var.replace("DHCP","<font color='cyan'>DHCP</font>")

        var=var.replace("IPv6","<font color='cyan'>IPv6</font>")
        var=var.replace("DNS","<font color='orange'>DNS</font>")
        var=var.replace("Ethernet","<font color='Tomato'>IPv4</font>")

        return var
    ######################### Funciones para IPConfig

    def IPCAll(self,salida):
        salida.setHtml(self.FormatoHTML(self.comandos(['ipconfig', '-all'])))
    def IPCDDNS(self,salida):
        salida.setHtml(self.FormatoHTML(self.comandos(['ipconfig', '-displaydns'])))
    def IPCFDNS(self,salida):
        salida.setHtml(self.FormatoHTML(self.comandos(['ipconfig', '-flushdns'])))
    def IPCRDNS(self,salida):
        salida.setHtml(self.FormatoHTML(self.comandos(['ipconfig', '-registerdns'])))
    def IPCAYUDA(self,salida):
        salida.setHtml(self.FormatoHTML(self.comandos(['ipconfig', '-?'])))
    def IPCMANUAL(self,parametros,salida):
        if "ipconfig" not in parametros:
            parametros="ipconfig "+parametros
        cmd=parametros.split()
        salida.setHtml(self.FormatoHTML(self.comandos(cmd)))
    ######################### Funciones para la sección PING 
    def validar_IP(self,ip):
        try:
            socket.inet_aton(ip)
            return True
        except:
            return False
    def validar_DN(self,dn):
        try:
            sb.check_output(['ping','-n','2','-w','600','-l','1',str(dn)])
            return True
        except:
            return False

    def validar_ping(self,Direcciones,paquetes, TimeOut, lenght, Tiempo):
        errores=""
        if TimeOut=="" or TimeOut==None: Time=4000
        else: 
            if self.validarNumero(TimeOut) == True: Time=TimeOut
            else: errores = errores+f"[!] El valor [{TimeOut}] no es valido.\n"
        if lenght=="" or lenght==None: len=64 
        else: 
            if self.validarNumero(lenght) == True: len=lenght
            else: errores = errores+f"[!] El valor [{lenght}] no es valido.\n"
        if Tiempo=="" or Tiempo==None: tiemp=0.2
        else: 
            if self.validarNumero(Tiempo) == True: tiemp=Tiempo
            else: errores = errores+f"[!] El valor [{Tiempo}] no es valido.\n"
        if paquetes=="" or paquetes==None: paquet=4
        else:
            if self.validarNumero(paquetes) == True: paquet=paquetes
            else: errores = errores+f"[!] El valor [{paquetes}] no es valido.\n"
        if Direcciones=="" or Direcciones==None:
            errores=errores+"[!] No se encontro ninguna dirección o host.\n"
        else:
            Direcciones=Direcciones.replace(" ","")
            aux=Direcciones.split(",")
            for i in aux:
                if self.validar_IP(i)==False and self.validar_DN(i.strip())==False:
                    errores=errores+"[!] La dirección o nombre de dominio ["+i+"] tiene un formato incorrecto.\n"
        if errores!="":  return errores,[]
        else: return "",[aux,paquet, Time, len, tiemp] 
    def help_ping(self):
        cmd = ['ping', '--help']
        shell_cmd = sb.run((cmd), capture_output=True, text=True)
        command_output=(shell_cmd.stdout)
        return str(command_output)
    def manual_ping(self,comando):
        if "ping" not in comando:
            comando="ping "+comando
        cmd=comando.split()
        shell_cmd = sb.run((cmd), capture_output=True, text=True)
        command_output=(shell_cmd.stdout)

    def ping(self,Direccion, TimeOut, lenght):
        cmd = ['ping', '-n','1','-w',TimeOut,'-l',lenght,Direccion]
        shell_cmd = sb.run((cmd), capture_output=True, text=True)
        command_output=(shell_cmd.stdout)
        return str(command_output)+"\n"
    def utilidad_Ping(self,Direcciones,paquetes, TimeOut, lenght, Tiempo,salida):
            success,datos=self.validar_ping(Direcciones,paquetes, TimeOut, lenght, Tiempo)
            if success=="":
                i=1
                auxG=""
                while i<=int(datos[1]) and salida.procPing==True:
                    for ip in datos[0]: 
                        salida.tmpBytes=str(datos[3])
                        aux=self.ping(str(ip.strip()),str(datos[2]),str(datos[3]))
                        auxL=aux.split("\n")
                        auxG=auxG+"<font color='cyan'>["+ip+"]\t"+auxL[2]+"</font><br>"
                        salida.ping=f"{i} {ip} {auxL[2]}"
                        salida.signalPing.emit(1)
                        sleep(float(datos[4]))
                    auxG=auxG+f"{i}<br>"
                    i+=1
            else:
                salida.ping=success
                salida.signalPing.emit(1)
    ################################ Utilidades TRACERT
    def tracertI(self,DN,Saltos,TimeOut,Manual,Tipo,Tipo2,salida):
        if Manual !="":
            self.tracertM(Manual,salida)
        else:
            e=""
            comando=[]
            comando.append("tracert")
            if self.validarNumero(Saltos)==False: e="[!] El numero de saltos tiene un formato incorrecto.<br>"
            elif Saltos=="":
                comando.append("-h")
                comando.append("10")
            else: 
                comando.append("-h")
                comando.append(Saltos)
            if self.validarNumero(TimeOut)==False: e="[!] El numero de TimeOut tiene un formato incorrecto.<br>"
            elif TimeOut=="": 
                comando.append("-w")
                comando.append("500")
            else: 
                comando.append("-w")
                comando.append(TimeOut)
            if Tipo==True: comando.append("-d")
            if Tipo2==True:comando.append("-r")
            if self.validar_DN(DN) == False and self.validar_IP(DN)==False: e="[!] La IP o dominio es incorrecto.<br>"
            else:  comando.append(DN)   
            if e!="":
                salida.setHtml("<font color='Tomato'>"+e+"</font>")
            else:
                salida.setHtml(self.FormatoHTML(self.comandos(comando)))

    def tracertA(self,salida):
        salida.setHtml(self.FormatoHTML(self.comandos(["arp","-?"])))
    def tracertM(self,Manual,salida):
        if "tracert" not in Manual:
            Manual="tracert "+Manual
        man=Manual.split(" ")
        salida.setHtml(self.FormatoHTML(self.comandos(man)))

    ################################ Utilidades ARP
    def ARPA(self,salida):
        salida.setHtml(self.FormatoHTML(self.comandos(["arp","-a"])))
    def ARPC(self,ip,salida,INTERFAZ):
        if (self.validar_IP(ip)==False):
            salida.setHtml("<font color='red'>La dirección IP tiene un formato incorrecto. </font>")
        else:
            direcciones=rs.escanearARP_U(ip,INTERFAZ,0,True)
            salida.setHtml(f"Dirección IPv4: <font color='cyan'> {direcciones[0]}</font><br>Dirección MAC: <font color='MediumSeaGreen'> {direcciones[1]}</font> ")
    def ARPADD(self,IP,MAC,inter,salida):
        e=""
        if self.validar_IP(IP)==False:
            e=e+(f"<font color='Tomato'>Dirección {IP} es incorrecta.<br></font>")
        if self.validar_IP(inter)==False:
            e=e+(f"<font color='Tomato'>Dirección {inter} es incorrecta.<br></font>")
        if self.validar_MAC(MAC)==False:
            e=e+(f"<font color='Tomato'>Dirección {MAC} es incorrecta.<br></font>")
        if e=="":
            MAC=MAC.replace(":","-")
            self.comandos(["arp","-s",IP,MAC,inter])
            salida.setHtml(f"<font color='cyan'>Dirección {IP} agregada correctamente")
        else:
            salida.setHtml(e)
    def ARPR(self,IP,inter,salida):
        e=""
        if self.validar_IP(IP)==False:
            e=e+(f"<font color='Tomato'>Dirección {IP} es incorrecta.<br></font>")
        if self.validar_IP(inter)==False:
            e=e+(f"<font color='Tomato'>Dirección {inter} es incorrecta.<br></font>")
            salida.setHtml(e)
        if e=="":
            self.comandos(["arp","-d",IP,inter]) 
            e=e+(f"<font color='cyan'>Dirección {IP} fue eliminada de la tabla ARP.<br></font>")
            salida.setHtml(e)   
    def ARPAY(self,salida):
        salida.setHtml(self.FormatoHTML(self.comandos(["arp","-?"])))

    ####################### Utilidad NSLookup
    def NSLOI(self,dom,p,salida):
        if p!="": self.NSLOM(p,salida)
        else:
            salida.setHtml(self.FormatoHTML(self.comandos(["nslookup",dom])))
    def NSLOM(self,para,salida):
        if "nslookup" not in para:
            para="nslookup "+para
        par=para.split(" ")
        salida.setHtml(self.FormatoHTML(self.comandos(par)))
    def NSLOA(self,salida):
        salida.setHtml(self.FormatoHTML(self.comandos(["nslookup","-?"])))