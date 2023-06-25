############## Ver interfaces #################################################################################
import socket
import requests
import netifaces
from time import sleep
import subprocess as sb
import modulos.BaseDatos
import scapy.all as scapy
from datetime import datetime
from psutil import net_if_addrs
from ipaddress import ip_network
db=modulos.BaseDatos.BaseDatos()

############## Ver interfaces #################################################################################
class Redes():
    def __init__(self) -> None:
        pass
    def obtenerDatosInter(self,Interfaz):
        NombreInterfaz="--"
        Descripcion="--"
        SSID="--"
        TipoRadio="--"
        Banda="--"
        VelocidadTransmision="--"
        VelocidadRecepcion="--"
        Senal="--"
        if "ETHERNET" not in str(Interfaz).upper() and "ETHER" not in str(Interfaz).upper():
            redes= sb.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True).stdout
            ls=redes.split("\n")
            aux=[]
            for l in ls:
                a=l.replace(" ","")
                if a != "":
                    aux.append(l)
                    s=l.split(" :")
                    if "Nombre" in s[0]: NombreInterfaz=s[1].strip()
                    if NombreInterfaz==Interfaz:
                        if "Descrip" in s[0]:Descripcion=s[1].strip()
                        elif " SSID" in s[0]: SSID=s[1].strip()
                        elif "radio" in s[0]:TipoRadio=s[1].strip()
                        elif "Banda" in s[0]: Banda=s[1].strip()
                        elif "recepc" in s[0]: VelocidadRecepcion=s[1].strip()
                        elif "transmi" in s[0]: VelocidadTransmision=s[1].strip()
                        if len(s)>1 and '%' in s[1]: Senal=s[1].strip()
        else:
            print(f"----> {Interfaz}")
            sb.run(['net','start','dot3svc'])
            redes= sb.run(["netsh", "lan", "show", "interfaces"], capture_output=True, text=True).stdout
            TipoRadio="802.1x"
            Banda="100 MHz (Categoría 5e) o 250 MHz (Categoria 6)"
            VelocidadRecepcion="1.0 Gbps"
            VelocidadTransmision="1.0 Gbps"
            Senal="100% (Cableado)"
            ls=redes.split("\n")
            aux=[]
            for l in ls:
                a=l.replace(" ","")
                if a != "":
                    aux.append(l)
                    s=l.split(" :")
                    if "Nombre" in s[0]: NombreInterfaz=s[1].strip()
                    if NombreInterfaz==Interfaz:
                        if "Descrip" in s[0]:Descripcion=s[1].strip()
        return [NombreInterfaz, Descripcion,SSID,TipoRadio, Banda, VelocidadTransmision, VelocidadRecepcion,Senal]
    def obtener_SSID(self,Interfaz):
        try:
            redes= sb.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True).stdout
            ls=redes.split("\n")
            ssids = [v.strip() for k, v in (p.split(':') for p in ls if 'SSID' in p)]
            aux=[]
            s=0
            for i in ls:
                if "Nombre de interfaz : " in i:
                    aux.append([i.replace("Nombre de interfaz : ","").strip(),ssids[s]])
                    s+=1
            for i in aux:
                if i[0]==Interfaz:
                    return i[1]
        except:
            return 'SIN CONEXION'
        return 'NO TIENE'
    def obtenerIntencidad(self,Interfaz):
        NombreInterfaz="--"
        Senal="--"
        try:
            redes= sb.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True).stdout
            ls=redes.split("\n")
            aux=[]
            for l in ls:
                a=l.replace(" ","")
                if a != "":
                    aux.append(l)
                    s=l.split(" :")
                    if "Nombre" in s[0]: NombreInterfaz=s[1].strip()
                    if NombreInterfaz==Interfaz:
                        if len(s)>1 and '%' in s[1]: Senal=s[1].strip()
        except:
            pass
        return Senal
    def Obtener_Dispositivos(self,verbose):
        if verbose==True: print("-- PROCEDIMIENTO: OBTENIENDO DISPOSITIVOS DE RED")
        addrs = net_if_addrs()
        nombre=str(addrs.keys())
        nombre=nombre.replace("dict_keys(['","")
        nombre=nombre.replace("', '","~")
        nombre=nombre.replace("'])","")
        nombres=nombre.split("~")
        #Se captura la lista de interfaces en el equipo
        interfaces = netifaces.interfaces()
        #Se recorre la lista de interfaces
        i=0
        INTER=[]
        for interface in interfaces: 
            Aux=[]
            #Se captura la informacion de cada interfaz
            datos = netifaces.ifaddresses(interface)
            #Se muestra el nombre de la interface
            Aux.append(str(nombres[i]))
            Aux.append(str(interface))
            #Se captura la lista de parametros que tiene la interface
            variables = datos.keys()
            #Se muestra la direccion de la capa de enlace de red de la interface
            Aux.append(str(datos[netifaces.AF_LINK][0]['addr']))
            #Si esta presente la informacion de IPV4 se muestra
            if netifaces.AF_INET in variables:
                Aux.append((str(datos[netifaces.AF_INET][0]['addr'])))
                Aux.append((str(datos[netifaces.AF_INET][0]['netmask'])))
                try:
                    Aux.append(str(netifaces.gateways()['default'][netifaces.AF_INET][0]))
                except:
                    Aux.append("--")
            else:
                Aux.append("--")
                Aux.append("--")
            #Si esta presente la informacion de IPv6 se muestra
            if netifaces.AF_INET in variables:
                Aux.append(str(datos[netifaces.AF_INET6][0]['addr']))
                Aux.append(str(datos[netifaces.AF_INET6][0]['netmask']))
                try:
                    Aux.append(str(netifaces.gateways()['default'][netifaces.AF_INET6][0]))
                except:
                    Aux.append("--")
            else:
                Aux.append("--")
                Aux.append("--")
            i+=1
            INTER.append(Aux)
        return INTER


    ################ Detectar dispositivos en red##############################################################
    def escanearARP(self,direccion_ip,INTERFAZ):
        print("-- PROCEDIMIENTO: ENVIANDO SOLICITUDES ARP")
        solicitud_arp = scapy.ARP(op=1,pdst=direccion_ip)
        broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        # Fusionamos
        solicitud_arp_broadcast = broadcast/solicitud_arp
        # sr              : Send and receive packets at layer 3
        #sr1              : Send packets at layer 3 and return only the first answer
        #srp              : Send and receive packets at layer 2
        #srp1             : Send and receive packets at layer 2 and return only the first answer
        escaneo = scapy.srp(solicitud_arp_broadcast,nofilter=1, timeout=20, retry=2,iface=INTERFAZ,verbose=False)
        respuesta =escaneo[0]
        i=0
        dispositivos=[]
        ips=[]
        for element in respuesta:
            aux=[]
            ips.append(str(element[1].psrc))
            aux.append(str(element[1].psrc))
            aux.append(str(element[1].hwsrc))
            i+=1
            dispositivos.append(aux)
        print(f"==== SE ENCONTRARON {len(ips)} HOSTS POR ARP ")
        return i,dispositivos,ips

    def escanearARP_U(self,direccion_ip,INTERFAZ,intentos,verbose):
        if verbose==True:print("----- SUBPROCEDIMIENTO: ESCANEAR ARP POR IPv4 ESPECIFICA")
        solicitud_arp = scapy.ARP(op=1,pdst=direccion_ip)
        broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        solicitud_arp_broadcast = broadcast/solicitud_arp
        escaneo = scapy.srp(solicitud_arp_broadcast, timeout=20,retry=intentos, nofilter=1,iface=INTERFAZ,verbose=False)
        respuesta =escaneo[0]
        direcciones=[]
        for element in respuesta:
            direcciones.append(str(element[1].psrc))
            direcciones.append(str(element[1].hwsrc))
        return direcciones
    def comprobarHistorial(self,MAC, FECHA,red):
        aux=db.consultarHISTORIAL_CONEXIONES()
        for i in aux:
            if i[5]==MAC and FECHA==i[1] and red==i[2]:
                return True
        return False
    def comprobarHistorialC(self,FECHA,NUM,red):
        aux=db.consultarHISTORIAL_NUM_CONEXIONES()
        encontrado=False
        for i in aux:
            if FECHA==i[2] and red==i[1]:
                encontrado=True
                if NUM > int(i[3]): 
                    return "M",i[0]
                else:  break
        if encontrado==False:
            return "A",0
        else:
            return "N",0
    def obtener_datos_Dispositivo(self,IPS, INTERFAZ,inf):
        rednom=inf.SSID
        red=int(db.consultar(f"SELECT ID_RED FROM RED WHERE SSID='{rednom}'")[0][0])
        print("-- PROCEDIMIENTO: OBTENIENDO DATOS DE DISPOSITIVOS")
        aux2= db.consultarCONTROL_RED_ESPECIFICA()
        Dispositivos=[]
        auxN=False
        now = datetime.now()
        Fecha=(f"{now.year}-{now.month}-{now.day}")
        for DIS in IPS:
            if len(DIS)>1:
                if inf.CAMBIOS==True or inf.SALIR==True:
                            break
                else:   
                    for i in aux2:
                        try:
                            if DIS[1] == i[8] and i[2]==inf.SSID:
                                if i[11]=="No permitido":
                                    inf.Errores.append([f"{datetime.now().hour}:{datetime.now().minute}",rednom,f"Usuario {i[5]} no permitido en la red."])
                                Dispositivos.append([DIS[0],DIS[1],i[7],i[5]])
                                if self.comprobarHistorial(DIS[1],Fecha,rednom)==False:
                                    db.insertarHISTORIAL_CONEXIONES(red,Fecha,i[5],DIS[0],DIS[1],i[7])
                                auxN=True
                                break
                        except:
                            print("[!] Error:"+str(DIS)+" "+str(i))
                    if auxN==False:
                            try:
                                aux=[]
                                aux.append(DIS[0])
                                aux.append(DIS[1])
                                try:
                                    vendor_name = self.get_mac_details(DIS[1])
                                    aux.append(vendor_name)
                                except:
                                    aux.append("Desconocido")
                                aux.append(socket.getfqdn(DIS[0]))
                                Dispositivos.append(aux)
                                now = datetime.now()
                                db.insertarCONTROL_RED_ESPECIFICA(red,str(aux[0]),'Pendiente','Ocupado',aux[1],'Pendiente',Fecha,'Pendiente',aux[3],'No verificado','Móvil',1,aux[2])
                                if self.comprobarHistorial(aux[1],Fecha,rednom)==False:
                                    db.insertarHISTORIAL_CONEXIONES(red,Fecha,aux[3],aux[0],aux[1],aux[2])
                            except Exception as e:
                                print("[!] Existio un error en la obtencion de datos:"+str(e))
                auxN=False
        print("--------------------------------------------------------------------------")        
        print("\t RESULTADO: EXISTEN "+str(len(Dispositivos))+" CONECTADOS A LAS "+str(datetime.now()))
        print("--------------------------------------------------------------------------")
        R,IDS=self.comprobarHistorialC(Fecha,len(Dispositivos),rednom)
        if R=="M":
            db.modificarHISTORIAL_NUM_CONEXIONES(IDS,red,Fecha,len(Dispositivos))
        elif R=="A":
            db.insertarHISTORIAL_NUM_CONEXIONES(red,Fecha,len(Dispositivos))
        return len(Dispositivos),Dispositivos

    def pingda(self,IP,ips_arp,inf):
        print("-- PROCEDIMIENTO: ENVIO DE PING A CADA UNO DE LOS ELEMENTOS.")
        network = ip_network(IP)
        hosts = network.hosts()
        i=0
        activos=[]
        for ip in hosts:
            if inf.CAMBIOS==True or inf.SALIR==True:
                break
            else:
                try:
                    if str(ip) not in ips_arp:
                        sb.check_output(['ping','-n','1','-w','600','-l','1',str(ip)])
                        activos.append(str(ip))
                        i+=0
                    else:
                        activos.append(str(ip))
                except:
                    pass
        print(f"====== SE ENCONTRARON {len(activos)} POR PING")
        return activos

    def ping_arp(self,PING, ARP,disposi,INTER):
        print("-- PROCEDIMIENTO: FUSIONANDO DISPOSITIVOS OBTENIDOS POR PING Y ARP")
        dispositivos=disposi
        for ip_ping in PING:
            if ip_ping not in ARP:
                aux=self.escanearARP_U(ip_ping,INTER,2,True)
                if aux == []:
                    aux=[ip_ping,"Sin Respuesta"]
                dispositivos.append(aux)
        print(f"======= AL COMBINAR SON {len(dispositivos)}")
        return dispositivos

    ################Obtener Nombre de Fabricante de MAC Adress
    def get_mac_details(self,mac_address):
        # We will use an API to get the vendor details
        url = "https://api.macvendors.com/"
        # Use get method to fetch details
        response = requests.get(url+mac_address)
        if response.status_code != 200:
            raise Exception("[!] MAC Address No valida!")
        return response.content.decode()
    ##############  Captura Seguida #############################################################################################

    def monitor(self,INTERFAZ,signal,objeto,inf):
        Salida=open('modulos/BasesDatos/sniff.pcap',"w",encoding="utf-8")
        Salida.close()
        paquetes=0
        while objeto.Cerrar==True and inf.SALIR==False:
            if objeto.Borrar==True:
                paquetes=0
                objeto.Borrar=False
            snf = scapy.sniff(iface=INTERFAZ,count=1)
            s=str(snf[0].show2)
            Salida=open('modulos/BasesDatos/sniff.pcap',"a",encoding="utf-8")
            tiempo=datetime.now()
            a=s.replace("<bound method Packet.show2 of","").replace(">>>>>","")
            Salida.write(f"{paquetes}:~{tiempo}:~{a}\n")
            paquetes=paquetes+1
            signal.emit(1)
            Salida.close()
            sleep(inf.TIEMPO_PAQ)
    def get_data(self,texto):
        datos=["","","","","","",""]
        datos[0]=texto.split(":~")[0]
        datos[1]=texto.split(":~")[1]
        datos[6]=self.Descripcion_Paquete(texto)
        texto=texto.replace(datos[0]+":~","").replace(datos[1]+":~","")
        var1 = texto.split("<")
        var2 = var1[2].split(" ")
        for i in var2:
            if "len" in i:
                datos[3]=i.replace("len=","").replace("p","")
            elif "src" in i:
                datos[4]=i.replace("src=","").replace("p","")
            elif "dst" in i:
                datos[5]=i.replace("dst=","").replace("p","")
        if (len(var1)-1)==2:
            datos[2]=var1[2].split(" ")[0]
        elif (len(var1)-1)==3:
            datos[2]=var1[3].split(" ")[0]
        elif (len(var1)-1)==4:
            aux=var1[len(var1)-1].split(" ")[0]
            if aux=="Raw" or aux=="Padding":
                datos[2]=var1[3].split(" ")[0]
            else:
                datos[2]=var1[4].split(" ")[0]
        elif (len(var1)-1)>4:
            aux=var1[2].split(" ")[0]
            if aux=="Raw":
                datos[2]=var1[3].split(" ")[0]
            else:
                datos[2]=var1[4].split(" ")[0]
        return datos
    def Comparar_Dominio(self,archivo,dominio):
        auxD=dominio
        texto=""
        encontrado=False
        with open(archivo, "r") as archivo_lectura:
            for linea in archivo_lectura:
                if auxD in linea:
                    aux=linea.split("[")
                    aux=aux[1].split("]")
                    texto=texto+auxD+" ["+str(int(aux[0])+1)+"] \n"
                    encontrado=True
                else:
                    texto=texto+linea
        if encontrado==False:
            texto=texto+auxD+" [1] \n"
        return texto
    def Descripcion_Paquete(self,texto):
        des=""
        text=texto.split(" ")
        for i in text:
                if "qname=" in i:
                    dom=self.Comparar_Dominio('modulos/BasesDatos/Dominios.txt',i.replace("'","").replace("qname=",""))
                    archivo=open('modulos/BasesDatos/Dominios.txt','w',encoding='utf-8')
                    archivo.write(dom)
                    archivo.close()
                    des="Paquete a: "+i.replace("'","").replace("qname=","")
                    return des
                if "USER_AGENT" in i:
                    des="Datos de aplicacion a "+i.replace("USER AGENT")
                    return des
                if "who-has" in i:
                    des="(Who-Has) Pregunta la dirección MAC del destino."
                    return des
                if "TCP" in i:
                    des="Paquete de intercambio de datos."
                    return des
                if "DCP" in i:
                    des="Envio de datos de datagramas sin conexión."
                    return des
                if "DHCP" in i:
                    des="Configuración dinamica de IP"
                    return des
        return des
    def formatoPaquete(self,p):
        a=p.replace(">","")
        a=a.replace("  "," ")
        a=a.replace(" <","|<")
        a=a.replace("|<","<br>")
        a=a.replace(" ","<br>&nbsp;&nbsp;&nbsp;")
        a=a.replace(":~","&nbsp;")
        return a  
    #Captura_PaquetesTemp("Wi-Fi")
    #Captura_Paquetes("Wi-Fi")