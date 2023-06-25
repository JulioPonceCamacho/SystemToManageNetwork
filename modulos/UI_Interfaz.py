# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import modulos.Recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1079, 626)
        icon = QIcon()
        icon.addFile(u":/Logo/Imagenes/TESJo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color: transparent ;\n"
"	background:transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"	color:#fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #1f232a ;\n"
"}\n"
"\n"
"#SubMenuIzquierdo{\n"
"	background-color: #16191d ;\n"
"}\n"
"#SubMenuIzquierdo QPushButton{\n"
"	text-align:left;\n"
"	padding:5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#SubMenuCentral{\n"
"	background-color:#2c313c;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"\n"
"}\n"
" #SubMenuDerecho{\n"
"	background-color:#2c313c;\n"
"	border-radius:10px;\n"
"\n"
"}\n"
"\n"
"#frame_5, #frame_8, #SubNotificacion{\n"
"	background-color:#16191d;\n"
"	border-radius:10px;\n"
"}\n"
"#Encabezado, #Pie{\n"
"	background-color:#1f232a;\n"
"}\n"
"\n"
"QPushButton{\n"
"		padding:	2px 2px;\n"
"		border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"		background-color:#1f232a;\n"
"}\n"
"QPushButton:pressed{\n"
"		background-color:#343b47;\n"
"}\n"
""
                        "QComboBox{\n"
"		padding:	2px 2px;\n"
"		border-radius:5px;\n"
"		border: 1px solid;\n"
"		border-color:#16191d ;\n"
"		min-width:150px;\n"
"}\n"
"\n"
"stackedWidget{\n"
"border-radius:10px;\n"
"}\n"
"\n"
"\n"
" QScrollBar:vertical{\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 7px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 6px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical{	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:pressed{	\n"
"	background-color: #1f232a;\n"
"}\n"
"QScrollBar::handle:vertical:hover {	\n"
"	background-color:#343b47;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {"
                        "	\n"
"	background-color: #1f232a;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: #343b47;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical{\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color:#1f232a;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: #343b47;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    height: 7px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal"
                        " {\n"
"    background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	width: 15px;\n"
"\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	width: 15px;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"#Velocidad_C, #Subida_C, #Ping_C{\n"
"	background-color:#282a36;\n"
"	color:#f8f8f2;\n"
"	border-radius:100px;\n"
"}\n"
"\n"
"QLineEdit, QTextEdit\n"
"{\n"
"	border-radius:10px;\n"
"	background-color: #16191d ;\n"
"}\n"
"#Iconfig1,#Iconfig2,#Iconfig3,#Iconfig4,#Iconfig5,#Iconfig6,#PingAyudaBtn,#PingIniciarBtn, #Trace"
                        "rtAyudaBtn, #TracertIniciarBtn,#arp1,#arp2,#arp5,#ArpAyuda,#NSLOAyudaBtn,#NSLOIniciarBtn,#var1,#var2,#var3,#var4,#var5,#var6,#var7,#var8,#arp7, #InicioTraficoBtn, #VerDomBtn,#RestabBtn,#AplicarAjusBtn{\n"
"	border-radius:10px;\n"
"	background-color: #16191d ;\n"
"	padding: 8px 8px;\n"
"}\n"
"#GR1,#GR2,#GR3,#GR4,#GR5,#GR6,#GR7,#GRG,#GRBorrarH,#GRBorrarS,#GRBorrarP,#GRBorrarPr,#GR8{\n"
"	border-radius:10px;\n"
"	background-color: #282a36 ;\n"
"	padding: 8px 8px;\n"
"}\n"
"#Iconfig1:hover,#Iconfig2:hover,#Iconfig3:hover,#Iconfig4:hover,#Iconfig5:hover,#Iconfig6:hover{\n"
"	border-radius:10px;\n"
"	background-color: #1f232a ;\n"
"	padding: 8px 8px;\n"
"\n"
"}\n"
"#Opciones{\n"
"	border-left: 1px solid  #16191d ;\n"
"	border-radius:5px;\n"
"}\n"
"QTableWidget{\n"
"	border-radius:10px;\n"
"	background-color: #16191d \n"
"}\n"
"QHeaderView::section {\n"
"   	border-radius:10px;\n"
"	background-color: #16191d \n"
"}\n"
"#WidgetInter,#WidgetRedes,#WidgetVeloci,#WidgetDom,#WidgetSenal,#WidgetUser,#WidgetPend,#R1,#R2,#R3"
                        ",#R4,#R5,#R6,#R7,#R8,#RG{\n"
"	border-radius:10px;\n"
"	background-color:#16191d ; \n"
"}\n"
"#SalidaPaq{\n"
"	border: 1px solid;\n"
"	border-color:#16191d ;\n"
"	border-radius:10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.MenuIzquierdo = QWidget(self.centralwidget)
        self.MenuIzquierdo.setObjectName(u"MenuIzquierdo")
        self.MenuIzquierdo.setMinimumSize(QSize(45, 0))
        self.MenuIzquierdo.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout = QVBoxLayout(self.MenuIzquierdo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.SubMenuIzquierdo = QWidget(self.MenuIzquierdo)
        self.SubMenuIzquierdo.setObjectName(u"SubMenuIzquierdo")
        self.SubMenuIzquierdo.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.SubMenuIzquierdo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.SubMenuIzquierdo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Menu = QPushButton(self.frame)
        self.Menu.setObjectName(u"Menu")
        icon1 = QIcon()
        icon1.addFile(u":/Iconos2/Imagenes/icons/icon_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu.setIcon(icon1)
        self.Menu.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.Menu)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.SubMenuIzquierdo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.DashboardBtn = QPushButton(self.frame_2)
        self.DashboardBtn.setObjectName(u"DashboardBtn")
        self.DashboardBtn.setStyleSheet(u"background-color:#1f232a;")
        icon2 = QIcon()
        icon2.addFile(u":/Iconos2/Imagenes/icons/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DashboardBtn.setIcon(icon2)
        self.DashboardBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.DashboardBtn)

        self.VelocidadBtn = QPushButton(self.frame_2)
        self.VelocidadBtn.setObjectName(u"VelocidadBtn")
        icon3 = QIcon()
        icon3.addFile(u":/Iconos2/Imagenes/icons/cil-speedometer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VelocidadBtn.setIcon(icon3)
        self.VelocidadBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.VelocidadBtn)

        self.TraficoBtn = QPushButton(self.frame_2)
        self.TraficoBtn.setObjectName(u"TraficoBtn")
        icon4 = QIcon()
        icon4.addFile(u":/Iconos2/Imagenes/icons/cil-size-grip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.TraficoBtn.setIcon(icon4)
        self.TraficoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.TraficoBtn)

        self.GestionBtn = QPushButton(self.frame_2)
        self.GestionBtn.setObjectName(u"GestionBtn")
        icon5 = QIcon()
        icon5.addFile(u":/Iconos2/Imagenes/icons/cil-3d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GestionBtn.setIcon(icon5)
        self.GestionBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.GestionBtn)

        self.UtilidadesBtn = QPushButton(self.frame_2)
        self.UtilidadesBtn.setObjectName(u"UtilidadesBtn")
        icon6 = QIcon()
        icon6.addFile(u":/Iconos2/Imagenes/icons/cil-terminal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.UtilidadesBtn.setIcon(icon6)
        self.UtilidadesBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.UtilidadesBtn)

        self.RerportesBtn = QPushButton(self.frame_2)
        self.RerportesBtn.setObjectName(u"RerportesBtn")
        icon7 = QIcon()
        icon7.addFile(u":/Iconos2/Imagenes/icons/cil-notes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RerportesBtn.setIcon(icon7)
        self.RerportesBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.RerportesBtn)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.SubMenuIzquierdo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 9)
        self.AlertasBtn = QPushButton(self.frame_3)
        self.AlertasBtn.setObjectName(u"AlertasBtn")
        icon8 = QIcon()
        icon8.addFile(u":/Iconos2/Imagenes/icons/cil-alarm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AlertasBtn.setIcon(icon8)
        self.AlertasBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.AlertasBtn)

        self.AyudaBtn = QPushButton(self.frame_3)
        self.AyudaBtn.setObjectName(u"AyudaBtn")
        icon9 = QIcon()
        icon9.addFile(u":/Iconos2/Imagenes/icons/cil-loop-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AyudaBtn.setIcon(icon9)
        self.AyudaBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.AyudaBtn)

        self.AjustesBtn = QPushButton(self.frame_3)
        self.AjustesBtn.setObjectName(u"AjustesBtn")
        icon10 = QIcon()
        icon10.addFile(u":/Iconos2/Imagenes/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AjustesBtn.setIcon(icon10)
        self.AjustesBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.AjustesBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.SubMenuIzquierdo, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.MenuIzquierdo)

        self.MenuCentral = QWidget(self.centralwidget)
        self.MenuCentral.setObjectName(u"MenuCentral")
        self.MenuCentral.setMinimumSize(QSize(0, 0))
        self.MenuCentral.setMaximumSize(QSize(0, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.MenuCentral)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.SubMenuCentral = QWidget(self.MenuCentral)
        self.SubMenuCentral.setObjectName(u"SubMenuCentral")
        self.verticalLayout_7 = QVBoxLayout(self.SubMenuCentral)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.frame_5 = QFrame(self.SubMenuCentral)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.MasMenuBtn = QPushButton(self.frame_5)
        self.MasMenuBtn.setObjectName(u"MasMenuBtn")
        icon11 = QIcon()
        icon11.addFile(u":/Iconos2/Imagenes/icons/cil-exit-to-app.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MasMenuBtn.setIcon(icon11)
        self.MasMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.MasMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.ContenidoCentral = QStackedWidget(self.SubMenuCentral)
        self.ContenidoCentral.setObjectName(u"ContenidoCentral")
        self.ContenidoCentral.setStyleSheet(u"")
        self.pAyu = QWidget()
        self.pAyu.setObjectName(u"pAyu")
        self.verticalLayout_8 = QVBoxLayout(self.pAyu)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea_15 = QScrollArea(self.pAyu)
        self.scrollArea_15.setObjectName(u"scrollArea_15")
        self.scrollArea_15.setWidgetResizable(True)
        self.scrollAreaWidgetContents_26 = QWidget()
        self.scrollAreaWidgetContents_26.setObjectName(u"scrollAreaWidgetContents_26")
        self.scrollAreaWidgetContents_26.setGeometry(QRect(0, 0, 169, 551))
        self.verticalLayout_74 = QVBoxLayout(self.scrollAreaWidgetContents_26)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_26)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout_74.addWidget(self.label_3)

        self.label_115 = QLabel(self.scrollAreaWidgetContents_26)
        self.label_115.setObjectName(u"label_115")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy)
        self.label_115.setMaximumSize(QSize(100, 100))
        self.label_115.setTextFormat(Qt.RichText)
        self.label_115.setPixmap(QPixmap(u":/Logo/Imagenes/TESJo.png"))
        self.label_115.setScaledContents(True)

        self.verticalLayout_74.addWidget(self.label_115, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.scrollArea_15.setWidget(self.scrollAreaWidgetContents_26)

        self.verticalLayout_8.addWidget(self.scrollArea_15)

        self.ContenidoCentral.addWidget(self.pAyu)
        self.pAjus = QWidget()
        self.pAjus.setObjectName(u"pAjus")
        self.verticalLayout_9 = QVBoxLayout(self.pAjus)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea_16 = QScrollArea(self.pAjus)
        self.scrollArea_16.setObjectName(u"scrollArea_16")
        self.scrollArea_16.setWidgetResizable(True)
        self.scrollAreaWidgetContents_28 = QWidget()
        self.scrollAreaWidgetContents_28.setObjectName(u"scrollAreaWidgetContents_28")
        self.scrollAreaWidgetContents_28.setGeometry(QRect(0, 0, 263, 551))
        self.verticalLayout_75 = QVBoxLayout(self.scrollAreaWidgetContents_28)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.widget_60 = QWidget(self.scrollAreaWidgetContents_28)
        self.widget_60.setObjectName(u"widget_60")
        self.formLayout_4 = QFormLayout(self.widget_60)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(1)
        self.formLayout_4.setVerticalSpacing(20)
        self.formLayout_4.setContentsMargins(-1, -1, 0, 0)
        self.label_116 = QLabel(self.widget_60)
        self.label_116.setObjectName(u"label_116")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_116)

        self.Ajus1 = QComboBox(self.widget_60)
        self.Ajus1.addItem("")
        self.Ajus1.addItem("")
        self.Ajus1.setObjectName(u"Ajus1")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.Ajus1)

        self.label_117 = QLabel(self.widget_60)
        self.label_117.setObjectName(u"label_117")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_117)

        self.Ajus2 = QComboBox(self.widget_60)
        self.Ajus2.addItem("")
        self.Ajus2.addItem("")
        self.Ajus2.setObjectName(u"Ajus2")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.Ajus2)

        self.label_118 = QLabel(self.widget_60)
        self.label_118.setObjectName(u"label_118")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_118)

        self.Ajus3 = QComboBox(self.widget_60)
        self.Ajus3.addItem("")
        self.Ajus3.addItem("")
        self.Ajus3.setObjectName(u"Ajus3")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.Ajus3)

        self.label_119 = QLabel(self.widget_60)
        self.label_119.setObjectName(u"label_119")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_119)

        self.label_120 = QLabel(self.widget_60)
        self.label_120.setObjectName(u"label_120")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_120)

        self.Ajus4 = QLineEdit(self.widget_60)
        self.Ajus4.setObjectName(u"Ajus4")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.Ajus4)

        self.Ajus5 = QLineEdit(self.widget_60)
        self.Ajus5.setObjectName(u"Ajus5")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.Ajus5)


        self.verticalLayout_75.addWidget(self.widget_60)

        self.AplicarAjusBtn = QPushButton(self.scrollAreaWidgetContents_28)
        self.AplicarAjusBtn.setObjectName(u"AplicarAjusBtn")

        self.verticalLayout_75.addWidget(self.AplicarAjusBtn)

        self.scrollArea_16.setWidget(self.scrollAreaWidgetContents_28)

        self.verticalLayout_9.addWidget(self.scrollArea_16)

        self.ContenidoCentral.addWidget(self.pAjus)

        self.verticalLayout_7.addWidget(self.ContenidoCentral)


        self.horizontalLayout_12.addWidget(self.SubMenuCentral)


        self.horizontalLayout.addWidget(self.MenuCentral)

        self.PantallaPrincipal = QWidget(self.centralwidget)
        self.PantallaPrincipal.setObjectName(u"PantallaPrincipal")
        sizePolicy.setHeightForWidth(self.PantallaPrincipal.sizePolicy().hasHeightForWidth())
        self.PantallaPrincipal.setSizePolicy(sizePolicy)
        self.PantallaPrincipal.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.PantallaPrincipal)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Encabezado = QWidget(self.PantallaPrincipal)
        self.Encabezado.setObjectName(u"Encabezado")
        self.horizontalLayout_3 = QHBoxLayout(self.Encabezado)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 4, -1, 4)
        self.frame_4 = QFrame(self.Encabezado)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Logo = QLabel(self.frame_4)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(20, 20))
        self.Logo.setMaximumSize(QSize(30, 30))
        self.Logo.setPixmap(QPixmap(u":/Logo/Imagenes/logo.png"))

        self.horizontalLayout_6.addWidget(self.Logo)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_6.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_6)


        self.horizontalLayout_3.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.Encabezado)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.InterRedBtn = QPushButton(self.frame_6)
        self.InterRedBtn.setObjectName(u"InterRedBtn")
        icon12 = QIcon()
        icon12.addFile(u":/Iconos2/Imagenes/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.InterRedBtn.setIcon(icon12)

        self.horizontalLayout_5.addWidget(self.InterRedBtn)

        self.UserBtn = QPushButton(self.frame_6)
        self.UserBtn.setObjectName(u"UserBtn")
        icon13 = QIcon()
        icon13.addFile(u":/Iconos2/Imagenes/icons/cil-ethernet.png", QSize(), QIcon.Normal, QIcon.Off)
        self.UserBtn.setIcon(icon13)

        self.horizontalLayout_5.addWidget(self.UserBtn)


        self.horizontalLayout_3.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.Encabezado)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MinBtn = QPushButton(self.frame_7)
        self.MinBtn.setObjectName(u"MinBtn")
        icon14 = QIcon()
        icon14.addFile(u":/Iconos2/Imagenes/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MinBtn.setIcon(icon14)
        self.MinBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.MinBtn)

        self.MaxBtn = QPushButton(self.frame_7)
        self.MaxBtn.setObjectName(u"MaxBtn")
        icon15 = QIcon()
        icon15.addFile(u":/Iconos2/Imagenes/icons/icon_restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MaxBtn.setIcon(icon15)
        self.MaxBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.MaxBtn)

        self.SalirBtn = QPushButton(self.frame_7)
        self.SalirBtn.setObjectName(u"SalirBtn")
        icon16 = QIcon()
        icon16.addFile(u":/Iconos2/Imagenes/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SalirBtn.setIcon(icon16)
        self.SalirBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.SalirBtn)


        self.horizontalLayout_3.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.Encabezado)

        self.Cuerpo = QWidget(self.PantallaPrincipal)
        self.Cuerpo.setObjectName(u"Cuerpo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Cuerpo.sizePolicy().hasHeightForWidth())
        self.Cuerpo.setSizePolicy(sizePolicy1)
        self.horizontalLayout_7 = QHBoxLayout(self.Cuerpo)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Contenido = QWidget(self.Cuerpo)
        self.Contenido.setObjectName(u"Contenido")
        self.verticalLayout_16 = QVBoxLayout(self.Contenido)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Contenidos = QStackedWidget(self.Contenido)
        self.Contenidos.setObjectName(u"Contenidos")
        self.pTab = QWidget()
        self.pTab.setObjectName(u"pTab")
        self.verticalLayout_17 = QVBoxLayout(self.pTab)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.scrollArea_9 = QScrollArea(self.pTab)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea_9.sizePolicy().hasHeightForWidth())
        self.scrollArea_9.setSizePolicy(sizePolicy2)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 1009, 842))
        self.horizontalLayout_27 = QHBoxLayout(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.widget_19 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_39 = QVBoxLayout(self.widget_19)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.WidgetInter = QWidget(self.widget_19)
        self.WidgetInter.setObjectName(u"WidgetInter")
        self.horizontalLayout_32 = QHBoxLayout(self.WidgetInter)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_83 = QLabel(self.WidgetInter)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setPixmap(QPixmap(u":/Logo/Imagenes/WALL.png"))

        self.horizontalLayout_32.addWidget(self.label_83)

        self.DatosRed = QLabel(self.WidgetInter)
        self.DatosRed.setObjectName(u"DatosRed")
        self.DatosRed.setWordWrap(True)

        self.horizontalLayout_32.addWidget(self.DatosRed)


        self.verticalLayout_39.addWidget(self.WidgetInter)

        self.WidgetPend = QScrollArea(self.widget_19)
        self.WidgetPend.setObjectName(u"WidgetPend")
        self.WidgetPend.setWidgetResizable(True)
        self.scrollAreaWidgetContents_24 = QWidget()
        self.scrollAreaWidgetContents_24.setObjectName(u"scrollAreaWidgetContents_24")
        self.scrollAreaWidgetContents_24.setGeometry(QRect(0, 0, 538, 120))
        self.verticalLayout_51 = QVBoxLayout(self.scrollAreaWidgetContents_24)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_41 = QLabel(self.scrollAreaWidgetContents_24)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_51.addWidget(self.label_41)

        self.WidgetPend.setWidget(self.scrollAreaWidgetContents_24)

        self.verticalLayout_39.addWidget(self.WidgetPend)

        self.WidgetUser = QScrollArea(self.widget_19)
        self.WidgetUser.setObjectName(u"WidgetUser")
        self.WidgetUser.setMinimumSize(QSize(0, 400))
        self.WidgetUser.setWidgetResizable(True)
        self.scrollAreaWidgetContents_23 = QWidget()
        self.scrollAreaWidgetContents_23.setObjectName(u"scrollAreaWidgetContents_23")
        self.scrollAreaWidgetContents_23.setGeometry(QRect(0, 0, 538, 400))
        self.verticalLayout_64 = QVBoxLayout(self.scrollAreaWidgetContents_23)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.label_39 = QLabel(self.scrollAreaWidgetContents_23)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_64.addWidget(self.label_39)

        self.WidgetUser.setWidget(self.scrollAreaWidgetContents_23)

        self.verticalLayout_39.addWidget(self.WidgetUser)


        self.horizontalLayout_27.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_44 = QVBoxLayout(self.widget_20)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.WidgetVeloci = QScrollArea(self.widget_20)
        self.WidgetVeloci.setObjectName(u"WidgetVeloci")
        self.WidgetVeloci.setMinimumSize(QSize(0, 400))
        self.WidgetVeloci.setWidgetResizable(True)
        self.scrollAreaWidgetContents_21 = QWidget()
        self.scrollAreaWidgetContents_21.setObjectName(u"scrollAreaWidgetContents_21")
        self.scrollAreaWidgetContents_21.setGeometry(QRect(0, 0, 411, 400))
        self.verticalLayout_63 = QVBoxLayout(self.scrollAreaWidgetContents_21)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.label_40 = QLabel(self.scrollAreaWidgetContents_21)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_63.addWidget(self.label_40)

        self.WidgetVeloci.setWidget(self.scrollAreaWidgetContents_21)

        self.verticalLayout_44.addWidget(self.WidgetVeloci)

        self.WidgetSenal = QScrollArea(self.widget_20)
        self.WidgetSenal.setObjectName(u"WidgetSenal")
        self.WidgetSenal.setMinimumSize(QSize(0, 400))
        self.WidgetSenal.setWidgetResizable(True)
        self.scrollAreaWidgetContents_22 = QWidget()
        self.scrollAreaWidgetContents_22.setObjectName(u"scrollAreaWidgetContents_22")
        self.scrollAreaWidgetContents_22.setGeometry(QRect(0, 0, 411, 400))
        self.verticalLayout_62 = QVBoxLayout(self.scrollAreaWidgetContents_22)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.label_43 = QLabel(self.scrollAreaWidgetContents_22)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout_62.addWidget(self.label_43)

        self.WidgetSenal.setWidget(self.scrollAreaWidgetContents_22)

        self.verticalLayout_44.addWidget(self.WidgetSenal)


        self.horizontalLayout_27.addWidget(self.widget_20)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_17.addWidget(self.scrollArea_9)

        self.Contenidos.addWidget(self.pTab)
        self.pVel = QWidget()
        self.pVel.setObjectName(u"pVel")
        self.verticalLayout_18 = QVBoxLayout(self.pVel)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget = QWidget(self.pVel)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_27 = QVBoxLayout(self.widget)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.widget)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1009, 237))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.widget_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Velocidad_C = QFrame(self.frame_11)
        self.Velocidad_C.setObjectName(u"Velocidad_C")
        self.Velocidad_C.setEnabled(True)
        self.Velocidad_C.setMinimumSize(QSize(200, 200))
        self.Velocidad_C.setFrameShape(QFrame.StyledPanel)
        self.Velocidad_C.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.Velocidad_C)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Velocidad_Salida = QLabel(self.Velocidad_C)
        self.Velocidad_Salida.setObjectName(u"Velocidad_Salida")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setKerning(True)
        self.Velocidad_Salida.setFont(font1)

        self.horizontalLayout_14.addWidget(self.Velocidad_Salida, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout.addWidget(self.Velocidad_C, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_13.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.widget_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_13)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_13 = QLabel(self.frame_13)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1, Qt.AlignHCenter)

        self.Subida_C = QFrame(self.frame_13)
        self.Subida_C.setObjectName(u"Subida_C")
        self.Subida_C.setEnabled(True)
        self.Subida_C.setMinimumSize(QSize(200, 200))
        self.Subida_C.setFrameShape(QFrame.StyledPanel)
        self.Subida_C.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.Subida_C)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.Subida_Salida = QLabel(self.Subida_C)
        self.Subida_Salida.setObjectName(u"Subida_Salida")
        self.Subida_Salida.setFont(font1)

        self.horizontalLayout_16.addWidget(self.Subida_Salida, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_2.addWidget(self.Subida_C, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_13.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.widget_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_12)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Ping_C = QFrame(self.frame_12)
        self.Ping_C.setObjectName(u"Ping_C")
        self.Ping_C.setEnabled(True)
        self.Ping_C.setMinimumSize(QSize(200, 200))
        self.Ping_C.setFrameShape(QFrame.StyledPanel)
        self.Ping_C.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.Ping_C)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.Ping_Salida = QLabel(self.Ping_C)
        self.Ping_Salida.setObjectName(u"Ping_Salida")
        self.Ping_Salida.setFont(font1)

        self.horizontalLayout_15.addWidget(self.Ping_Salida, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_3.addWidget(self.Ping_C, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_14 = QLabel(self.frame_12)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_13.addWidget(self.frame_12)


        self.verticalLayout_10.addWidget(self.widget_2)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_27.addWidget(self.scrollArea_4)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_28 = QVBoxLayout(self.widget_4)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.widget_49 = QWidget(self.widget_4)
        self.widget_49.setObjectName(u"widget_49")
        self.horizontalLayout_60 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.pushButton_5 = QPushButton(self.widget_49)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        icon17 = QIcon()
        icon17.addFile(u":/INTER/Imagenes/Reportes/PROVEED.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon17)

        self.horizontalLayout_60.addWidget(self.pushButton_5)

        self.SpeedRed = QLabel(self.widget_49)
        self.SpeedRed.setObjectName(u"SpeedRed")

        self.horizontalLayout_60.addWidget(self.SpeedRed)

        self.pushButton = QPushButton(self.widget_49)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        icon18 = QIcon()
        icon18.addFile(u":/Speed/Imagenes/Speed/Servidor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon18)

        self.horizontalLayout_60.addWidget(self.pushButton)

        self.SpeedServidor = QLabel(self.widget_49)
        self.SpeedServidor.setObjectName(u"SpeedServidor")

        self.horizontalLayout_60.addWidget(self.SpeedServidor)

        self.pushButton_2 = QPushButton(self.widget_49)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        icon19 = QIcon()
        icon19.addFile(u":/Speed/Imagenes/Speed/Host.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon19)

        self.horizontalLayout_60.addWidget(self.pushButton_2)

        self.SpeedSponsor = QLabel(self.widget_49)
        self.SpeedSponsor.setObjectName(u"SpeedSponsor")

        self.horizontalLayout_60.addWidget(self.SpeedSponsor)

        self.pushButton_3 = QPushButton(self.widget_49)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        icon20 = QIcon()
        icon20.addFile(u":/Speed/Imagenes/Speed/PingSub.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon20)

        self.horizontalLayout_60.addWidget(self.pushButton_3)

        self.SpeedBajada = QLabel(self.widget_49)
        self.SpeedBajada.setObjectName(u"SpeedBajada")

        self.horizontalLayout_60.addWidget(self.SpeedBajada)

        self.pushButton_4 = QPushButton(self.widget_49)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        icon21 = QIcon()
        icon21.addFile(u":/Speed/Imagenes/Speed/PingDes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon21)

        self.horizontalLayout_60.addWidget(self.pushButton_4)

        self.SpeedSubida = QLabel(self.widget_49)
        self.SpeedSubida.setObjectName(u"SpeedSubida")

        self.horizontalLayout_60.addWidget(self.SpeedSubida)


        self.verticalLayout_28.addWidget(self.widget_49)

        self.widget_54 = QWidget(self.widget_4)
        self.widget_54.setObjectName(u"widget_54")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.PruebaVelBtn = QPushButton(self.widget_54)
        self.PruebaVelBtn.setObjectName(u"PruebaVelBtn")
        icon22 = QIcon()
        icon22.addFile(u":/INTER/Imagenes/Reportes/Speed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PruebaVelBtn.setIcon(icon22)

        self.horizontalLayout_9.addWidget(self.PruebaVelBtn)

        self.PruebaVelTBtn = QPushButton(self.widget_54)
        self.PruebaVelTBtn.setObjectName(u"PruebaVelTBtn")
        self.PruebaVelTBtn.setIcon(icon22)

        self.horizontalLayout_9.addWidget(self.PruebaVelTBtn)

        self.BorrarPruebas = QPushButton(self.widget_54)
        self.BorrarPruebas.setObjectName(u"BorrarPruebas")
        icon23 = QIcon()
        icon23.addFile(u":/INTER/Imagenes/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BorrarPruebas.setIcon(icon23)

        self.horizontalLayout_9.addWidget(self.BorrarPruebas)


        self.verticalLayout_28.addWidget(self.widget_54)


        self.verticalLayout_27.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_29 = QVBoxLayout(self.widget_3)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.widget_50 = QWidget(self.widget_3)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_61 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_82 = QLabel(self.widget_50)
        self.label_82.setObjectName(u"label_82")

        self.horizontalLayout_61.addWidget(self.label_82)

        self.FiltradoSpeed = QLineEdit(self.widget_50)
        self.FiltradoSpeed.setObjectName(u"FiltradoSpeed")

        self.horizontalLayout_61.addWidget(self.FiltradoSpeed)


        self.verticalLayout_29.addWidget(self.widget_50)

        self.scrollArea_3 = QScrollArea(self.widget_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1016, 202))
        self.verticalLayout_30 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.TablaVelocidad = QTableWidget(self.scrollAreaWidgetContents)
        self.TablaVelocidad.setObjectName(u"TablaVelocidad")
        self.TablaVelocidad.verticalHeader().setVisible(False)

        self.verticalLayout_30.addWidget(self.TablaVelocidad)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_29.addWidget(self.scrollArea_3)


        self.verticalLayout_27.addWidget(self.widget_3)


        self.verticalLayout_18.addWidget(self.widget)

        self.Contenidos.addWidget(self.pVel)
        self.pTraf = QWidget()
        self.pTraf.setObjectName(u"pTraf")
        self.verticalLayout_19 = QVBoxLayout(self.pTraf)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.PagTrafico = QLabel(self.pTraf)
        self.PagTrafico.setObjectName(u"PagTrafico")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.PagTrafico.setFont(font2)
        self.PagTrafico.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.PagTrafico)

        self.scrollArea_5 = QScrollArea(self.pTraf)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1016, 514))
        self.verticalLayout_31 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.widget_16 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_38 = QLabel(self.widget_16)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_22.addWidget(self.label_38)

        self.Filtrado = QLineEdit(self.widget_16)
        self.Filtrado.setObjectName(u"Filtrado")

        self.horizontalLayout_22.addWidget(self.Filtrado)

        self.InicioTraficoBtn = QPushButton(self.widget_16)
        self.InicioTraficoBtn.setObjectName(u"InicioTraficoBtn")

        self.horizontalLayout_22.addWidget(self.InicioTraficoBtn)

        self.VerDomBtn = QPushButton(self.widget_16)
        self.VerDomBtn.setObjectName(u"VerDomBtn")

        self.horizontalLayout_22.addWidget(self.VerDomBtn)

        self.RestabBtn = QPushButton(self.widget_16)
        self.RestabBtn.setObjectName(u"RestabBtn")

        self.horizontalLayout_22.addWidget(self.RestabBtn)


        self.verticalLayout_31.addWidget(self.widget_16)

        self.TablaPaquetes = QTableWidget(self.scrollAreaWidgetContents_2)
        if (self.TablaPaquetes.columnCount() < 7):
            self.TablaPaquetes.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.TablaPaquetes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TablaPaquetes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TablaPaquetes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TablaPaquetes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TablaPaquetes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TablaPaquetes.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TablaPaquetes.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.TablaPaquetes.rowCount() < 1):
            self.TablaPaquetes.setRowCount(1)
        self.TablaPaquetes.setObjectName(u"TablaPaquetes")
        self.TablaPaquetes.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.TablaPaquetes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.TablaPaquetes.setTextElideMode(Qt.ElideMiddle)
        self.TablaPaquetes.setWordWrap(True)
        self.TablaPaquetes.setRowCount(1)
        self.TablaPaquetes.horizontalHeader().setCascadingSectionResizes(True)
        self.TablaPaquetes.horizontalHeader().setMinimumSectionSize(150)
        self.TablaPaquetes.horizontalHeader().setDefaultSectionSize(150)
        self.TablaPaquetes.horizontalHeader().setProperty("showSortIndicator", False)
        self.TablaPaquetes.horizontalHeader().setStretchLastSection(True)
        self.TablaPaquetes.verticalHeader().setVisible(False)
        self.TablaPaquetes.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_31.addWidget(self.TablaPaquetes)

        self.SalidaPaq = QFrame(self.scrollAreaWidgetContents_2)
        self.SalidaPaq.setObjectName(u"SalidaPaq")
        self.SalidaPaq.setMaximumSize(QSize(16777215, 0))
        self.SalidaPaq.setFrameShape(QFrame.StyledPanel)
        self.SalidaPaq.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.SalidaPaq)
        self.verticalLayout_52.setSpacing(2)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_52.setContentsMargins(2, 2, 2, 2)
        self.widget_21 = QWidget(self.SalidaPaq)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.TituloSalidaPaq = QLabel(self.widget_21)
        self.TituloSalidaPaq.setObjectName(u"TituloSalidaPaq")
        sizePolicy.setHeightForWidth(self.TituloSalidaPaq.sizePolicy().hasHeightForWidth())
        self.TituloSalidaPaq.setSizePolicy(sizePolicy)
        self.TituloSalidaPaq.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.TituloSalidaPaq)

        self.SalirSalidaPaq = QPushButton(self.widget_21)
        self.SalirSalidaPaq.setObjectName(u"SalirSalidaPaq")
        self.SalirSalidaPaq.setIcon(icon11)

        self.horizontalLayout_40.addWidget(self.SalirSalidaPaq, 0, Qt.AlignRight)


        self.verticalLayout_52.addWidget(self.widget_21)

        self.TextoSalidaPaq = QTextEdit(self.SalidaPaq)
        self.TextoSalidaPaq.setObjectName(u"TextoSalidaPaq")

        self.verticalLayout_52.addWidget(self.TextoSalidaPaq)


        self.verticalLayout_31.addWidget(self.SalidaPaq)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_19.addWidget(self.scrollArea_5)

        self.Contenidos.addWidget(self.pTraf)
        self.pGest = QWidget()
        self.pGest.setObjectName(u"pGest")
        self.verticalLayout_20 = QVBoxLayout(self.pGest)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.PagGestion = QLabel(self.pGest)
        self.PagGestion.setObjectName(u"PagGestion")
        self.PagGestion.setFont(font2)
        self.PagGestion.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.PagGestion)

        self.widget_22 = QWidget(self.pGest)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.G_PR = QPushButton(self.widget_22)
        self.G_PR.setObjectName(u"G_PR")

        self.horizontalLayout_41.addWidget(self.G_PR)

        self.G_R = QPushButton(self.widget_22)
        self.G_R.setObjectName(u"G_R")

        self.horizontalLayout_41.addWidget(self.G_R)

        self.G_I = QPushButton(self.widget_22)
        self.G_I.setObjectName(u"G_I")

        self.horizontalLayout_41.addWidget(self.G_I)

        self.G_P = QPushButton(self.widget_22)
        self.G_P.setObjectName(u"G_P")

        self.horizontalLayout_41.addWidget(self.G_P)

        self.G_RD = QPushButton(self.widget_22)
        self.G_RD.setObjectName(u"G_RD")

        self.horizontalLayout_41.addWidget(self.G_RD)

        self.G_C = QPushButton(self.widget_22)
        self.G_C.setObjectName(u"G_C")

        self.horizontalLayout_41.addWidget(self.G_C)

        self.G_H = QPushButton(self.widget_22)
        self.G_H.setObjectName(u"G_H")

        self.horizontalLayout_41.addWidget(self.G_H)

        self.G_CR = QPushButton(self.widget_22)
        self.G_CR.setObjectName(u"G_CR")

        self.horizontalLayout_41.addWidget(self.G_CR)

        self.G_SU = QPushButton(self.widget_22)
        self.G_SU.setObjectName(u"G_SU")

        self.horizontalLayout_41.addWidget(self.G_SU)

        self.G_D = QPushButton(self.widget_22)
        self.G_D.setObjectName(u"G_D")

        self.horizontalLayout_41.addWidget(self.G_D)


        self.verticalLayout_20.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.pGest)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_53 = QVBoxLayout(self.widget_23)
        self.verticalLayout_53.setSpacing(1)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.widget_29 = QWidget(self.widget_23)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_44 = QLabel(self.widget_29)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_42.addWidget(self.label_44)

        self.GFiltrado = QLineEdit(self.widget_29)
        self.GFiltrado.setObjectName(u"GFiltrado")

        self.horizontalLayout_42.addWidget(self.GFiltrado)

        self.GAgregarBtn = QPushButton(self.widget_29)
        self.GAgregarBtn.setObjectName(u"GAgregarBtn")
        self.GAgregarBtn.setEnabled(True)
        icon24 = QIcon()
        icon24.addFile(u":/Iconos2/Imagenes/icons/cil-library-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GAgregarBtn.setIcon(icon24)

        self.horizontalLayout_42.addWidget(self.GAgregarBtn)

        self.GModificarBtn = QPushButton(self.widget_29)
        self.GModificarBtn.setObjectName(u"GModificarBtn")
        self.GModificarBtn.setEnabled(False)
        icon25 = QIcon()
        icon25.addFile(u":/Iconos2/Imagenes/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.GModificarBtn.setIcon(icon25)

        self.horizontalLayout_42.addWidget(self.GModificarBtn)

        self.GEliminarBtn = QPushButton(self.widget_29)
        self.GEliminarBtn.setObjectName(u"GEliminarBtn")
        self.GEliminarBtn.setEnabled(False)
        self.GEliminarBtn.setIcon(icon16)

        self.horizontalLayout_42.addWidget(self.GEliminarBtn)


        self.verticalLayout_53.addWidget(self.widget_29)

        self.P_PR = QScrollArea(self.widget_23)
        self.P_PR.setObjectName(u"P_PR")
        self.P_PR.setMaximumSize(QSize(16777215, 0))
        self.P_PR.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 991, 183))
        self.verticalLayout_54 = QVBoxLayout(self.scrollAreaWidgetContents_13)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.widget_32 = QWidget(self.scrollAreaWidgetContents_13)
        self.widget_32.setObjectName(u"widget_32")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_46 = QLabel(self.widget_32)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_43.addWidget(self.label_46)

        self.PR_FECHA = QLineEdit(self.widget_32)
        self.PR_FECHA.setObjectName(u"PR_FECHA")

        self.horizontalLayout_43.addWidget(self.PR_FECHA)

        self.label_48 = QLabel(self.widget_32)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_43.addWidget(self.label_48)

        self.PR_RED = QComboBox(self.widget_32)
        self.PR_RED.setObjectName(u"PR_RED")

        self.horizontalLayout_43.addWidget(self.PR_RED)

        self.label_97 = QLabel(self.widget_32)
        self.label_97.setObjectName(u"label_97")

        self.horizontalLayout_43.addWidget(self.label_97)

        self.PR_DEP = QComboBox(self.widget_32)
        self.PR_DEP.setObjectName(u"PR_DEP")

        self.horizontalLayout_43.addWidget(self.PR_DEP)

        self.label_45 = QLabel(self.widget_32)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_43.addWidget(self.label_45)

        self.PR_DESC = QTextEdit(self.widget_32)
        self.PR_DESC.setObjectName(u"PR_DESC")
        self.PR_DESC.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_43.addWidget(self.PR_DESC)


        self.verticalLayout_54.addWidget(self.widget_32)

        self.widget_33 = QWidget(self.scrollAreaWidgetContents_13)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_49 = QLabel(self.widget_33)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_44.addWidget(self.label_49)

        self.PR_COR = QComboBox(self.widget_33)
        self.PR_COR.addItem("")
        self.PR_COR.addItem("")
        self.PR_COR.setObjectName(u"PR_COR")

        self.horizontalLayout_44.addWidget(self.PR_COR)

        self.label_47 = QLabel(self.widget_33)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_44.addWidget(self.label_47)

        self.PR_SOL = QTextEdit(self.widget_33)
        self.PR_SOL.setObjectName(u"PR_SOL")
        self.PR_SOL.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_44.addWidget(self.PR_SOL)

        self.label_50 = QLabel(self.widget_33)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_44.addWidget(self.label_50)

        self.PR_FECHAC = QLineEdit(self.widget_33)
        self.PR_FECHAC.setObjectName(u"PR_FECHAC")

        self.horizontalLayout_44.addWidget(self.PR_FECHAC)


        self.verticalLayout_54.addWidget(self.widget_33)

        self.G_AgregarBtn = QPushButton(self.scrollAreaWidgetContents_13)
        self.G_AgregarBtn.setObjectName(u"G_AgregarBtn")

        self.verticalLayout_54.addWidget(self.G_AgregarBtn, 0, Qt.AlignHCenter)

        self.P_PR.setWidget(self.scrollAreaWidgetContents_13)

        self.verticalLayout_53.addWidget(self.P_PR)

        self.P_I = QScrollArea(self.widget_23)
        self.P_I.setObjectName(u"P_I")
        self.P_I.setMaximumSize(QSize(16777215, 0))
        self.P_I.setWidgetResizable(True)
        self.scrollAreaWidgetContents_15 = QWidget()
        self.scrollAreaWidgetContents_15.setObjectName(u"scrollAreaWidgetContents_15")
        self.scrollAreaWidgetContents_15.setGeometry(QRect(0, 0, 991, 155))
        self.verticalLayout_56 = QVBoxLayout(self.scrollAreaWidgetContents_15)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.widget_37 = QWidget(self.scrollAreaWidgetContents_15)
        self.widget_37.setObjectName(u"widget_37")
        self.horizontalLayout_48 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_57 = QLabel(self.widget_37)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_48.addWidget(self.label_57)

        self.I_ID = QLineEdit(self.widget_37)
        self.I_ID.setObjectName(u"I_ID")

        self.horizontalLayout_48.addWidget(self.I_ID)

        self.label_58 = QLabel(self.widget_37)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_48.addWidget(self.label_58)

        self.I_NOM = QLineEdit(self.widget_37)
        self.I_NOM.setObjectName(u"I_NOM")

        self.horizontalLayout_48.addWidget(self.I_NOM)

        self.label_59 = QLabel(self.widget_37)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_48.addWidget(self.label_59)

        self.I_DESC = QTextEdit(self.widget_37)
        self.I_DESC.setObjectName(u"I_DESC")
        self.I_DESC.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_48.addWidget(self.I_DESC)


        self.verticalLayout_56.addWidget(self.widget_37)

        self.widget_38 = QWidget(self.scrollAreaWidgetContents_15)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_49 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_96 = QLabel(self.widget_38)
        self.label_96.setObjectName(u"label_96")

        self.horizontalLayout_49.addWidget(self.label_96)

        self.I_DEP = QComboBox(self.widget_38)
        self.I_DEP.setObjectName(u"I_DEP")

        self.horizontalLayout_49.addWidget(self.I_DEP)

        self.label_60 = QLabel(self.widget_38)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_49.addWidget(self.label_60)

        self.I_UBI = QLineEdit(self.widget_38)
        self.I_UBI.setObjectName(u"I_UBI")

        self.horizontalLayout_49.addWidget(self.I_UBI)

        self.label_61 = QLabel(self.widget_38)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_49.addWidget(self.label_61)

        self.I_TC = QComboBox(self.widget_38)
        self.I_TC.addItem("")
        self.I_TC.addItem("")
        self.I_TC.addItem("")
        self.I_TC.setObjectName(u"I_TC")

        self.horizontalLayout_49.addWidget(self.I_TC)

        self.label_62 = QLabel(self.widget_38)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_49.addWidget(self.label_62)

        self.I_RED = QComboBox(self.widget_38)
        self.I_RED.setObjectName(u"I_RED")

        self.horizontalLayout_49.addWidget(self.I_RED)


        self.verticalLayout_56.addWidget(self.widget_38)

        self.I_ADD = QPushButton(self.scrollAreaWidgetContents_15)
        self.I_ADD.setObjectName(u"I_ADD")

        self.verticalLayout_56.addWidget(self.I_ADD, 0, Qt.AlignHCenter)

        self.P_I.setWidget(self.scrollAreaWidgetContents_15)

        self.verticalLayout_53.addWidget(self.P_I)

        self.P_D = QScrollArea(self.widget_23)
        self.P_D.setObjectName(u"P_D")
        self.P_D.setMaximumSize(QSize(16777215, 0))
        self.P_D.setWidgetResizable(True)
        self.scrollAreaWidgetContents_20 = QWidget()
        self.scrollAreaWidgetContents_20.setObjectName(u"scrollAreaWidgetContents_20")
        self.scrollAreaWidgetContents_20.setGeometry(QRect(0, 0, 991, 109))
        self.verticalLayout_61 = QVBoxLayout(self.scrollAreaWidgetContents_20)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.widget_48 = QWidget(self.scrollAreaWidgetContents_20)
        self.widget_48.setObjectName(u"widget_48")
        self.horizontalLayout_59 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_98 = QLabel(self.widget_48)
        self.label_98.setObjectName(u"label_98")

        self.horizontalLayout_59.addWidget(self.label_98)

        self.D_NOM = QLineEdit(self.widget_48)
        self.D_NOM.setObjectName(u"D_NOM")

        self.horizontalLayout_59.addWidget(self.D_NOM)

        self.label_99 = QLabel(self.widget_48)
        self.label_99.setObjectName(u"label_99")

        self.horizontalLayout_59.addWidget(self.label_99)

        self.D_DES = QTextEdit(self.widget_48)
        self.D_DES.setObjectName(u"D_DES")
        self.D_DES.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_59.addWidget(self.D_DES)


        self.verticalLayout_61.addWidget(self.widget_48)

        self.D_ADD = QPushButton(self.scrollAreaWidgetContents_20)
        self.D_ADD.setObjectName(u"D_ADD")

        self.verticalLayout_61.addWidget(self.D_ADD, 0, Qt.AlignHCenter)

        self.P_D.setWidget(self.scrollAreaWidgetContents_20)

        self.verticalLayout_53.addWidget(self.P_D)

        self.P_R = QScrollArea(self.widget_23)
        self.P_R.setObjectName(u"P_R")
        self.P_R.setMaximumSize(QSize(16777215, 0))
        self.P_R.setWidgetResizable(True)
        self.scrollAreaWidgetContents_14 = QWidget()
        self.scrollAreaWidgetContents_14.setObjectName(u"scrollAreaWidgetContents_14")
        self.scrollAreaWidgetContents_14.setGeometry(QRect(0, 0, 991, 193))
        self.verticalLayout_55 = QVBoxLayout(self.scrollAreaWidgetContents_14)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.widget_34 = QWidget(self.scrollAreaWidgetContents_14)
        self.widget_34.setObjectName(u"widget_34")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(-1, 0, -1, 0)
        self.label_51 = QLabel(self.widget_34)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_45.addWidget(self.label_51)

        self.R_Folio = QLineEdit(self.widget_34)
        self.R_Folio.setObjectName(u"R_Folio")

        self.horizontalLayout_45.addWidget(self.R_Folio)

        self.label_52 = QLabel(self.widget_34)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_45.addWidget(self.label_52)

        self.R_Descrip = QTextEdit(self.widget_34)
        self.R_Descrip.setObjectName(u"R_Descrip")
        self.R_Descrip.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_45.addWidget(self.R_Descrip)

        self.label_53 = QLabel(self.widget_34)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_45.addWidget(self.label_53)

        self.R_Fecha = QLineEdit(self.widget_34)
        self.R_Fecha.setObjectName(u"R_Fecha")

        self.horizontalLayout_45.addWidget(self.R_Fecha)


        self.verticalLayout_55.addWidget(self.widget_34)

        self.widget_35 = QWidget(self.scrollAreaWidgetContents_14)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_46 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.R_ACUDIO = QComboBox(self.widget_35)
        self.R_ACUDIO.addItem("")
        self.R_ACUDIO.addItem("")
        self.R_ACUDIO.setObjectName(u"R_ACUDIO")

        self.horizontalLayout_46.addWidget(self.R_ACUDIO)

        self.R_REMOSIT = QComboBox(self.widget_35)
        self.R_REMOSIT.addItem("")
        self.R_REMOSIT.addItem("")
        self.R_REMOSIT.setObjectName(u"R_REMOSIT")

        self.horizontalLayout_46.addWidget(self.R_REMOSIT)

        self.label_81 = QLabel(self.widget_35)
        self.label_81.setObjectName(u"label_81")

        self.horizontalLayout_46.addWidget(self.label_81)

        self.R_PROV = QComboBox(self.widget_35)
        self.R_PROV.setObjectName(u"R_PROV")

        self.horizontalLayout_46.addWidget(self.R_PROV)


        self.verticalLayout_55.addWidget(self.widget_35)

        self.widget_36 = QWidget(self.scrollAreaWidgetContents_14)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_47 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_54 = QLabel(self.widget_36)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_47.addWidget(self.label_54)

        self.R_MOT = QTextEdit(self.widget_36)
        self.R_MOT.setObjectName(u"R_MOT")
        self.R_MOT.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_47.addWidget(self.R_MOT)

        self.label_55 = QLabel(self.widget_36)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_47.addWidget(self.label_55)

        self.R_TEL = QLineEdit(self.widget_36)
        self.R_TEL.setObjectName(u"R_TEL")

        self.horizontalLayout_47.addWidget(self.R_TEL)

        self.label_56 = QLabel(self.widget_36)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_47.addWidget(self.label_56)

        self.R_ATEND = QLineEdit(self.widget_36)
        self.R_ATEND.setObjectName(u"R_ATEND")

        self.horizontalLayout_47.addWidget(self.R_ATEND)


        self.verticalLayout_55.addWidget(self.widget_36)

        self.R_ADD = QPushButton(self.scrollAreaWidgetContents_14)
        self.R_ADD.setObjectName(u"R_ADD")

        self.verticalLayout_55.addWidget(self.R_ADD, 0, Qt.AlignHCenter)

        self.P_R.setWidget(self.scrollAreaWidgetContents_14)

        self.verticalLayout_53.addWidget(self.P_R)

        self.P_P = QScrollArea(self.widget_23)
        self.P_P.setObjectName(u"P_P")
        self.P_P.setMaximumSize(QSize(16777215, 0))
        self.P_P.setWidgetResizable(True)
        self.scrollAreaWidgetContents_16 = QWidget()
        self.scrollAreaWidgetContents_16.setObjectName(u"scrollAreaWidgetContents_16")
        self.scrollAreaWidgetContents_16.setGeometry(QRect(0, 0, 991, 155))
        self.verticalLayout_57 = QVBoxLayout(self.scrollAreaWidgetContents_16)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.widget_39 = QWidget(self.scrollAreaWidgetContents_16)
        self.widget_39.setObjectName(u"widget_39")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_63 = QLabel(self.widget_39)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_50.addWidget(self.label_63)

        self.P_N = QLineEdit(self.widget_39)
        self.P_N.setObjectName(u"P_N")

        self.horizontalLayout_50.addWidget(self.P_N)

        self.label_64 = QLabel(self.widget_39)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_50.addWidget(self.label_64)

        self.P_DES = QTextEdit(self.widget_39)
        self.P_DES.setObjectName(u"P_DES")
        self.P_DES.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_50.addWidget(self.P_DES)


        self.verticalLayout_57.addWidget(self.widget_39)

        self.widget_40 = QWidget(self.scrollAreaWidgetContents_16)
        self.widget_40.setObjectName(u"widget_40")
        self.horizontalLayout_51 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_65 = QLabel(self.widget_40)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_51.addWidget(self.label_65)

        self.P_FECH = QLineEdit(self.widget_40)
        self.P_FECH.setObjectName(u"P_FECH")

        self.horizontalLayout_51.addWidget(self.P_FECH)

        self.label_66 = QLabel(self.widget_40)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_51.addWidget(self.label_66)

        self.P_TR = QComboBox(self.widget_40)
        self.P_TR.setObjectName(u"P_TR")

        self.horizontalLayout_51.addWidget(self.P_TR)

        self.label_67 = QLabel(self.widget_40)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_51.addWidget(self.label_67)

        self.P_TEL = QLineEdit(self.widget_40)
        self.P_TEL.setObjectName(u"P_TEL")

        self.horizontalLayout_51.addWidget(self.P_TEL)


        self.verticalLayout_57.addWidget(self.widget_40)

        self.P_ADD = QPushButton(self.scrollAreaWidgetContents_16)
        self.P_ADD.setObjectName(u"P_ADD")

        self.verticalLayout_57.addWidget(self.P_ADD, 0, Qt.AlignHCenter)

        self.P_P.setWidget(self.scrollAreaWidgetContents_16)

        self.verticalLayout_53.addWidget(self.P_P)

        self.P_CR = QScrollArea(self.widget_23)
        self.P_CR.setObjectName(u"P_CR")
        self.P_CR.setMaximumSize(QSize(16777215, 0))
        self.P_CR.setWidgetResizable(True)
        self.scrollAreaWidgetContents_18 = QWidget()
        self.scrollAreaWidgetContents_18.setObjectName(u"scrollAreaWidgetContents_18")
        self.scrollAreaWidgetContents_18.setGeometry(QRect(0, 0, 991, 201))
        self.verticalLayout_59 = QVBoxLayout(self.scrollAreaWidgetContents_18)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.widget_44 = QWidget(self.scrollAreaWidgetContents_18)
        self.widget_44.setObjectName(u"widget_44")
        self.horizontalLayout_55 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_78 = QLabel(self.widget_44)
        self.label_78.setObjectName(u"label_78")

        self.horizontalLayout_55.addWidget(self.label_78)

        self.CR_FECHA = QLineEdit(self.widget_44)
        self.CR_FECHA.setObjectName(u"CR_FECHA")

        self.horizontalLayout_55.addWidget(self.CR_FECHA)

        self.label_76 = QLabel(self.widget_44)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_55.addWidget(self.label_76)

        self.CR_RESP = QLineEdit(self.widget_44)
        self.CR_RESP.setObjectName(u"CR_RESP")

        self.horizontalLayout_55.addWidget(self.CR_RESP)

        self.label_77 = QLabel(self.widget_44)
        self.label_77.setObjectName(u"label_77")

        self.horizontalLayout_55.addWidget(self.label_77)

        self.CR_DEP = QComboBox(self.widget_44)
        self.CR_DEP.setObjectName(u"CR_DEP")

        self.horizontalLayout_55.addWidget(self.CR_DEP)

        self.label_79 = QLabel(self.widget_44)
        self.label_79.setObjectName(u"label_79")

        self.horizontalLayout_55.addWidget(self.label_79)

        self.CR_NOINV = QLineEdit(self.widget_44)
        self.CR_NOINV.setObjectName(u"CR_NOINV")

        self.horizontalLayout_55.addWidget(self.CR_NOINV)


        self.verticalLayout_59.addWidget(self.widget_44)

        self.widget_43 = QWidget(self.scrollAreaWidgetContents_18)
        self.widget_43.setObjectName(u"widget_43")
        self.horizontalLayout_54 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_68 = QLabel(self.widget_43)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_54.addWidget(self.label_68)

        self.CR_HOS = QLineEdit(self.widget_43)
        self.CR_HOS.setObjectName(u"CR_HOS")

        self.horizontalLayout_54.addWidget(self.CR_HOS)

        self.label_73 = QLabel(self.widget_43)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_54.addWidget(self.label_73)

        self.CR_IP = QLineEdit(self.widget_43)
        self.CR_IP.setObjectName(u"CR_IP")

        self.horizontalLayout_54.addWidget(self.CR_IP)

        self.label_74 = QLabel(self.widget_43)
        self.label_74.setObjectName(u"label_74")

        self.horizontalLayout_54.addWidget(self.label_74)

        self.CR_MAC = QLineEdit(self.widget_43)
        self.CR_MAC.setObjectName(u"CR_MAC")

        self.horizontalLayout_54.addWidget(self.CR_MAC)

        self.label_75 = QLabel(self.widget_43)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_54.addWidget(self.label_75)

        self.CR_VEND = QLineEdit(self.widget_43)
        self.CR_VEND.setObjectName(u"CR_VEND")

        self.horizontalLayout_54.addWidget(self.CR_VEND)

        self.label_88 = QLabel(self.widget_43)
        self.label_88.setObjectName(u"label_88")

        self.horizontalLayout_54.addWidget(self.label_88)

        self.CR_RED = QComboBox(self.widget_43)
        self.CR_RED.setObjectName(u"CR_RED")

        self.horizontalLayout_54.addWidget(self.CR_RED)


        self.verticalLayout_59.addWidget(self.widget_43)

        self.widget_45 = QWidget(self.scrollAreaWidgetContents_18)
        self.widget_45.setObjectName(u"widget_45")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_84 = QLabel(self.widget_45)
        self.label_84.setObjectName(u"label_84")

        self.horizontalLayout_56.addWidget(self.label_84)

        self.CR_OBS = QTextEdit(self.widget_45)
        self.CR_OBS.setObjectName(u"CR_OBS")
        self.CR_OBS.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_56.addWidget(self.CR_OBS)

        self.label_85 = QLabel(self.widget_45)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_56.addWidget(self.label_85)

        self.CR_STAT = QComboBox(self.widget_45)
        self.CR_STAT.addItem("")
        self.CR_STAT.addItem("")
        self.CR_STAT.setObjectName(u"CR_STAT")

        self.horizontalLayout_56.addWidget(self.CR_STAT)

        self.label_86 = QLabel(self.widget_45)
        self.label_86.setObjectName(u"label_86")

        self.horizontalLayout_56.addWidget(self.label_86)

        self.CR_TIP = QComboBox(self.widget_45)
        self.CR_TIP.addItem("")
        self.CR_TIP.addItem("")
        self.CR_TIP.addItem("")
        self.CR_TIP.setObjectName(u"CR_TIP")

        self.horizontalLayout_56.addWidget(self.CR_TIP)

        self.label_87 = QLabel(self.widget_45)
        self.label_87.setObjectName(u"label_87")

        self.horizontalLayout_56.addWidget(self.label_87)

        self.CR_VERFI = QComboBox(self.widget_45)
        self.CR_VERFI.addItem("")
        self.CR_VERFI.addItem("")
        self.CR_VERFI.addItem("")
        self.CR_VERFI.setObjectName(u"CR_VERFI")

        self.horizontalLayout_56.addWidget(self.CR_VERFI)


        self.verticalLayout_59.addWidget(self.widget_45)

        self.CR_ADD = QPushButton(self.scrollAreaWidgetContents_18)
        self.CR_ADD.setObjectName(u"CR_ADD")

        self.verticalLayout_59.addWidget(self.CR_ADD, 0, Qt.AlignHCenter)

        self.P_CR.setWidget(self.scrollAreaWidgetContents_18)

        self.verticalLayout_53.addWidget(self.P_CR)

        self.P_RD = QScrollArea(self.widget_23)
        self.P_RD.setObjectName(u"P_RD")
        self.P_RD.setMaximumSize(QSize(16777215, 0))
        self.P_RD.setWidgetResizable(True)
        self.scrollAreaWidgetContents_17 = QWidget()
        self.scrollAreaWidgetContents_17.setObjectName(u"scrollAreaWidgetContents_17")
        self.scrollAreaWidgetContents_17.setGeometry(QRect(0, 0, 991, 121))
        self.verticalLayout_58 = QVBoxLayout(self.scrollAreaWidgetContents_17)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.widget_42 = QWidget(self.scrollAreaWidgetContents_17)
        self.widget_42.setObjectName(u"widget_42")
        self.horizontalLayout_52 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.RD_SSID = QLabel(self.widget_42)
        self.RD_SSID.setObjectName(u"RD_SSID")

        self.horizontalLayout_52.addWidget(self.RD_SSID)

        self.RD_S = QLineEdit(self.widget_42)
        self.RD_S.setObjectName(u"RD_S")

        self.horizontalLayout_52.addWidget(self.RD_S)

        self.label_69 = QLabel(self.widget_42)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_52.addWidget(self.label_69)

        self.RD_PASS = QLineEdit(self.widget_42)
        self.RD_PASS.setObjectName(u"RD_PASS")

        self.horizontalLayout_52.addWidget(self.RD_PASS)


        self.verticalLayout_58.addWidget(self.widget_42)

        self.widget_41 = QWidget(self.scrollAreaWidgetContents_17)
        self.widget_41.setObjectName(u"widget_41")
        self.horizontalLayout_53 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_70 = QLabel(self.widget_41)
        self.label_70.setObjectName(u"label_70")

        self.horizontalLayout_53.addWidget(self.label_70)

        self.RD_SUB = QLineEdit(self.widget_41)
        self.RD_SUB.setObjectName(u"RD_SUB")

        self.horizontalLayout_53.addWidget(self.RD_SUB)

        self.label_71 = QLabel(self.widget_41)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_53.addWidget(self.label_71)

        self.RD_DAJ = QLineEdit(self.widget_41)
        self.RD_DAJ.setObjectName(u"RD_DAJ")

        self.horizontalLayout_53.addWidget(self.RD_DAJ)

        self.label_72 = QLabel(self.widget_41)
        self.label_72.setObjectName(u"label_72")

        self.horizontalLayout_53.addWidget(self.label_72)

        self.RD_PROV = QComboBox(self.widget_41)
        self.RD_PROV.setObjectName(u"RD_PROV")

        self.horizontalLayout_53.addWidget(self.RD_PROV)


        self.verticalLayout_58.addWidget(self.widget_41)

        self.RD_ADD = QPushButton(self.scrollAreaWidgetContents_17)
        self.RD_ADD.setObjectName(u"RD_ADD")

        self.verticalLayout_58.addWidget(self.RD_ADD, 0, Qt.AlignHCenter)

        self.P_RD.setWidget(self.scrollAreaWidgetContents_17)

        self.verticalLayout_53.addWidget(self.P_RD)

        self.P_SU = QScrollArea(self.widget_23)
        self.P_SU.setObjectName(u"P_SU")
        self.P_SU.setMaximumSize(QSize(16777215, 0))
        self.P_SU.setWidgetResizable(True)
        self.scrollAreaWidgetContents_19 = QWidget()
        self.scrollAreaWidgetContents_19.setObjectName(u"scrollAreaWidgetContents_19")
        self.scrollAreaWidgetContents_19.setGeometry(QRect(0, 0, 991, 155))
        self.verticalLayout_60 = QVBoxLayout(self.scrollAreaWidgetContents_19)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.widget_46 = QWidget(self.scrollAreaWidgetContents_19)
        self.widget_46.setObjectName(u"widget_46")
        self.horizontalLayout_57 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_89 = QLabel(self.widget_46)
        self.label_89.setObjectName(u"label_89")

        self.horizontalLayout_57.addWidget(self.label_89)

        self.SU_ID = QLineEdit(self.widget_46)
        self.SU_ID.setObjectName(u"SU_ID")

        self.horizontalLayout_57.addWidget(self.SU_ID)

        self.label_90 = QLabel(self.widget_46)
        self.label_90.setObjectName(u"label_90")

        self.horizontalLayout_57.addWidget(self.label_90)

        self.SU_NOM = QLineEdit(self.widget_46)
        self.SU_NOM.setObjectName(u"SU_NOM")

        self.horizontalLayout_57.addWidget(self.SU_NOM)

        self.label_91 = QLabel(self.widget_46)
        self.label_91.setObjectName(u"label_91")

        self.horizontalLayout_57.addWidget(self.label_91)

        self.SU_FECHA = QLineEdit(self.widget_46)
        self.SU_FECHA.setObjectName(u"SU_FECHA")

        self.horizontalLayout_57.addWidget(self.SU_FECHA)

        self.label_92 = QLabel(self.widget_46)
        self.label_92.setObjectName(u"label_92")

        self.horizontalLayout_57.addWidget(self.label_92)

        self.SU_SERV = QComboBox(self.widget_46)
        self.SU_SERV.addItem("")
        self.SU_SERV.addItem("")
        self.SU_SERV.setObjectName(u"SU_SERV")

        self.horizontalLayout_57.addWidget(self.SU_SERV)

        self.label_80 = QLabel(self.widget_46)
        self.label_80.setObjectName(u"label_80")

        self.horizontalLayout_57.addWidget(self.label_80)

        self.SU_TR = QComboBox(self.widget_46)
        self.SU_TR.setObjectName(u"SU_TR")

        self.horizontalLayout_57.addWidget(self.SU_TR)


        self.verticalLayout_60.addWidget(self.widget_46)

        self.widget_47 = QWidget(self.scrollAreaWidgetContents_19)
        self.widget_47.setObjectName(u"widget_47")
        self.horizontalLayout_58 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_123 = QLabel(self.widget_47)
        self.label_123.setObjectName(u"label_123")

        self.horizontalLayout_58.addWidget(self.label_123)

        self.SU_CORD = QLineEdit(self.widget_47)
        self.SU_CORD.setObjectName(u"SU_CORD")

        self.horizontalLayout_58.addWidget(self.SU_CORD)

        self.label_93 = QLabel(self.widget_47)
        self.label_93.setObjectName(u"label_93")

        self.horizontalLayout_58.addWidget(self.label_93)

        self.SU_PROVE = QLineEdit(self.widget_47)
        self.SU_PROVE.setObjectName(u"SU_PROVE")

        self.horizontalLayout_58.addWidget(self.SU_PROVE)

        self.label_94 = QLabel(self.widget_47)
        self.label_94.setObjectName(u"label_94")

        self.horizontalLayout_58.addWidget(self.label_94)

        self.SU_TEL = QLineEdit(self.widget_47)
        self.SU_TEL.setObjectName(u"SU_TEL")

        self.horizontalLayout_58.addWidget(self.SU_TEL)

        self.label_95 = QLabel(self.widget_47)
        self.label_95.setObjectName(u"label_95")

        self.horizontalLayout_58.addWidget(self.label_95)

        self.SU_OBS = QTextEdit(self.widget_47)
        self.SU_OBS.setObjectName(u"SU_OBS")
        self.SU_OBS.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_58.addWidget(self.SU_OBS)


        self.verticalLayout_60.addWidget(self.widget_47)

        self.SU_ADD = QPushButton(self.scrollAreaWidgetContents_19)
        self.SU_ADD.setObjectName(u"SU_ADD")

        self.verticalLayout_60.addWidget(self.SU_ADD, 0, Qt.AlignHCenter)

        self.P_SU.setWidget(self.scrollAreaWidgetContents_19)

        self.verticalLayout_53.addWidget(self.P_SU)

        self.SalidaGestion = QTableWidget(self.widget_23)
        self.SalidaGestion.setObjectName(u"SalidaGestion")
        self.SalidaGestion.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.SalidaGestion.setSelectionMode(QAbstractItemView.SingleSelection)
        self.SalidaGestion.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SalidaGestion.verticalHeader().setVisible(False)

        self.verticalLayout_53.addWidget(self.SalidaGestion)


        self.verticalLayout_20.addWidget(self.widget_23)

        self.Contenidos.addWidget(self.pGest)
        self.pUtil = QWidget()
        self.pUtil.setObjectName(u"pUtil")
        self.verticalLayout_21 = QVBoxLayout(self.pUtil)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.PagUtilidades = QLabel(self.pUtil)
        self.PagUtilidades.setObjectName(u"PagUtilidades")
        self.PagUtilidades.setFont(font2)
        self.PagUtilidades.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.PagUtilidades, 0, Qt.AlignTop)

        self.widget_5 = QWidget(self.pUtil)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.horizontalLayout_17 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.scrollArea_6 = QScrollArea(self.widget_5)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 998, 496))
        self.horizontalLayout_20 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.UtilitB = QWidget(self.widget_6)
        self.UtilitB.setObjectName(u"UtilitB")
        self.verticalLayout_32 = QVBoxLayout(self.UtilitB)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.IPConfBtn = QPushButton(self.UtilitB)
        self.IPConfBtn.setObjectName(u"IPConfBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.IPConfBtn.sizePolicy().hasHeightForWidth())
        self.IPConfBtn.setSizePolicy(sizePolicy3)
        self.IPConfBtn.setMaximumSize(QSize(16777215, 25))
        icon26 = QIcon()
        icon26.addFile(u":/Utilidades/Imagenes/Utilidades/ipconfig.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IPConfBtn.setIcon(icon26)
        self.IPConfBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_32.addWidget(self.IPConfBtn)

        self.PingBtn = QPushButton(self.UtilitB)
        self.PingBtn.setObjectName(u"PingBtn")
        icon27 = QIcon()
        icon27.addFile(u":/Utilidades/Imagenes/Utilidades/ping.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PingBtn.setIcon(icon27)
        self.PingBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_32.addWidget(self.PingBtn)

        self.TracerBtn = QPushButton(self.UtilitB)
        self.TracerBtn.setObjectName(u"TracerBtn")
        icon28 = QIcon()
        icon28.addFile(u":/Utilidades/Imagenes/Utilidades/route.png", QSize(), QIcon.Normal, QIcon.Off)
        self.TracerBtn.setIcon(icon28)
        self.TracerBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_32.addWidget(self.TracerBtn)

        self.ArpBtn = QPushButton(self.UtilitB)
        self.ArpBtn.setObjectName(u"ArpBtn")
        icon29 = QIcon()
        icon29.addFile(u":/Utilidades/Imagenes/Utilidades/arp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ArpBtn.setIcon(icon29)
        self.ArpBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_32.addWidget(self.ArpBtn)

        self.NSLookBtn = QPushButton(self.UtilitB)
        self.NSLookBtn.setObjectName(u"NSLookBtn")
        icon30 = QIcon()
        icon30.addFile(u":/Utilidades/Imagenes/Utilidades/nslook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NSLookBtn.setIcon(icon30)
        self.NSLookBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_32.addWidget(self.NSLookBtn)

        self.RouteBtn = QPushButton(self.UtilitB)
        self.RouteBtn.setObjectName(u"RouteBtn")
        icon31 = QIcon()
        icon31.addFile(u":/Utilidades/Imagenes/Utilidades/tracert.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RouteBtn.setIcon(icon31)
        self.RouteBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_32.addWidget(self.RouteBtn)


        self.horizontalLayout_18.addWidget(self.UtilitB)

        self.ContenidosU = QStackedWidget(self.widget_6)
        self.ContenidosU.setObjectName(u"ContenidosU")
        self.IPConfigPag = QWidget()
        self.IPConfigPag.setObjectName(u"IPConfigPag")
        self.horizontalLayout_19 = QHBoxLayout(self.IPConfigPag)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.Opciones = QFrame(self.IPConfigPag)
        self.Opciones.setObjectName(u"Opciones")
        self.Opciones.setFrameShape(QFrame.StyledPanel)
        self.Opciones.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.Opciones)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.scrollArea_8 = QScrollArea(self.Opciones)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 289, 456))
        self.verticalLayout_35 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_8 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 16777215))
        self.label_8.setWordWrap(True)

        self.verticalLayout_35.addWidget(self.label_8)

        self.Opciones_2 = QWidget(self.scrollAreaWidgetContents_6)
        self.Opciones_2.setObjectName(u"Opciones_2")
        self.gridLayout_4 = QGridLayout(self.Opciones_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setVerticalSpacing(10)
        self.Iconfig4 = QPushButton(self.Opciones_2)
        self.Iconfig4.setObjectName(u"Iconfig4")

        self.gridLayout_4.addWidget(self.Iconfig4, 5, 1, 1, 1)

        self.Iconfig6 = QPushButton(self.Opciones_2)
        self.Iconfig6.setObjectName(u"Iconfig6")

        self.gridLayout_4.addWidget(self.Iconfig6, 7, 1, 1, 1)

        self.label_15 = QLabel(self.Opciones_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_15, 5, 0, 1, 1)

        self.ParamIp = QTextEdit(self.Opciones_2)
        self.ParamIp.setObjectName(u"ParamIp")
        self.ParamIp.setMaximumSize(QSize(200, 50))

        self.gridLayout_4.addWidget(self.ParamIp, 7, 0, 1, 1)

        self.label_11 = QLabel(self.Opciones_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_11, 4, 0, 1, 1)

        self.label_9 = QLabel(self.Opciones_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_10 = QLabel(self.Opciones_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_10, 3, 0, 1, 1)

        self.Iconfig2 = QPushButton(self.Opciones_2)
        self.Iconfig2.setObjectName(u"Iconfig2")

        self.gridLayout_4.addWidget(self.Iconfig2, 3, 1, 1, 1)

        self.Iconfig1 = QPushButton(self.Opciones_2)
        self.Iconfig1.setObjectName(u"Iconfig1")

        self.gridLayout_4.addWidget(self.Iconfig1, 1, 1, 1, 1)

        self.Iconfig3 = QPushButton(self.Opciones_2)
        self.Iconfig3.setObjectName(u"Iconfig3")

        self.gridLayout_4.addWidget(self.Iconfig3, 4, 1, 1, 1)

        self.label_16 = QLabel(self.Opciones_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_16, 6, 0, 1, 1)

        self.Iconfig5 = QPushButton(self.Opciones_2)
        self.Iconfig5.setObjectName(u"Iconfig5")

        self.gridLayout_4.addWidget(self.Iconfig5, 6, 1, 1, 1)


        self.verticalLayout_35.addWidget(self.Opciones_2)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_33.addWidget(self.scrollArea_8)


        self.horizontalLayout_19.addWidget(self.Opciones)

        self.SalidaIconfig = QFrame(self.IPConfigPag)
        self.SalidaIconfig.setObjectName(u"SalidaIconfig")
        self.SalidaIconfig.setFrameShape(QFrame.StyledPanel)
        self.SalidaIconfig.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.SalidaIconfig)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.IPConfigO = QFrame(self.SalidaIconfig)
        self.IPConfigO.setObjectName(u"IPConfigO")
        self.IPConfigO.setFrameShape(QFrame.StyledPanel)
        self.IPConfigO.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.IPConfigO)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.scrollArea_7 = QScrollArea(self.IPConfigO)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 93, 69))
        self.horizontalLayout_25 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_14)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.SalidaIPConf = QTextEdit(self.frame_14)
        self.SalidaIPConf.setObjectName(u"SalidaIPConf")
        self.SalidaIPConf.setLineWrapMode(QTextEdit.NoWrap)
        self.SalidaIPConf.setOverwriteMode(False)

        self.verticalLayout_34.addWidget(self.SalidaIPConf)


        self.horizontalLayout_25.addWidget(self.frame_14)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_5)

        self.horizontalLayout_24.addWidget(self.scrollArea_7)


        self.horizontalLayout_23.addWidget(self.IPConfigO)


        self.horizontalLayout_19.addWidget(self.SalidaIconfig)

        self.ContenidosU.addWidget(self.IPConfigPag)
        self.PingPag = QWidget()
        self.PingPag.setObjectName(u"PingPag")
        self.verticalLayout_37 = QVBoxLayout(self.PingPag)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.scrollArea_10 = QScrollArea(self.PingPag)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 876, 460))
        self.horizontalLayout_28 = QHBoxLayout(self.scrollAreaWidgetContents_8)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.widget_9 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_45 = QVBoxLayout(self.widget_9)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_18 = QLabel(self.widget_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setWordWrap(True)

        self.verticalLayout_45.addWidget(self.label_18)

        self.ping1 = QTextEdit(self.widget_9)
        self.ping1.setObjectName(u"ping1")
        self.ping1.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_45.addWidget(self.ping1)

        self.widget_24 = QWidget(self.widget_9)
        self.widget_24.setObjectName(u"widget_24")
        self.formLayout = QFormLayout(self.widget_24)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.label_19 = QLabel(self.widget_24)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.ping12 = QLineEdit(self.widget_24)
        self.ping12.setObjectName(u"ping12")
        self.ping12.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ping12)

        self.label_20 = QLabel(self.widget_24)
        self.label_20.setObjectName(u"label_20")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_20)

        self.ping2 = QLineEdit(self.widget_24)
        self.ping2.setObjectName(u"ping2")
        self.ping2.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ping2)

        self.label_21 = QLabel(self.widget_24)
        self.label_21.setObjectName(u"label_21")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_21)

        self.ping3 = QLineEdit(self.widget_24)
        self.ping3.setObjectName(u"ping3")
        self.ping3.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ping3)

        self.label_22 = QLabel(self.widget_24)
        self.label_22.setObjectName(u"label_22")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_22)

        self.ping4 = QLineEdit(self.widget_24)
        self.ping4.setObjectName(u"ping4")
        self.ping4.setMinimumSize(QSize(0, 25))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ping4)


        self.verticalLayout_45.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.widget_9)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.PingAyudaBtn = QPushButton(self.widget_25)
        self.PingAyudaBtn.setObjectName(u"PingAyudaBtn")
        self.PingAyudaBtn.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_33.addWidget(self.PingAyudaBtn)

        self.PingIniciarBtn = QPushButton(self.widget_25)
        self.PingIniciarBtn.setObjectName(u"PingIniciarBtn")

        self.horizontalLayout_33.addWidget(self.PingIniciarBtn)


        self.verticalLayout_45.addWidget(self.widget_25)


        self.horizontalLayout_28.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.scrollAreaWidgetContents_8)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_38 = QVBoxLayout(self.widget_10)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_35 = QLabel(self.widget_10)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setWordWrap(True)

        self.verticalLayout_38.addWidget(self.label_35)

        self.PINGOUT = QTableWidget(self.widget_10)
        if (self.PINGOUT.columnCount() < 5):
            self.PINGOUT.setColumnCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.PINGOUT.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.PINGOUT.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.PINGOUT.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.PINGOUT.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.PINGOUT.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        if (self.PINGOUT.rowCount() < 1):
            self.PINGOUT.setRowCount(1)
        self.PINGOUT.setObjectName(u"PINGOUT")
        self.PINGOUT.setAutoScroll(True)
        self.PINGOUT.setRowCount(1)
        self.PINGOUT.horizontalHeader().setCascadingSectionResizes(True)
        self.PINGOUT.horizontalHeader().setDefaultSectionSize(100)
        self.PINGOUT.verticalHeader().setVisible(False)

        self.verticalLayout_38.addWidget(self.PINGOUT)


        self.horizontalLayout_28.addWidget(self.widget_10)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_37.addWidget(self.scrollArea_10)

        self.ContenidosU.addWidget(self.PingPag)
        self.TracertPag = QWidget()
        self.TracertPag.setObjectName(u"TracertPag")
        self.verticalLayout_43 = QVBoxLayout(self.TracertPag)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.scrollArea_11 = QScrollArea(self.TracertPag)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 876, 460))
        self.horizontalLayout_29 = QHBoxLayout(self.scrollAreaWidgetContents_9)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.widget_11 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_46 = QVBoxLayout(self.widget_11)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_24 = QLabel(self.widget_11)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setWordWrap(True)

        self.verticalLayout_46.addWidget(self.label_24)

        self.widget_26 = QWidget(self.widget_11)
        self.widget_26.setObjectName(u"widget_26")
        self.formLayout_2 = QFormLayout(self.widget_26)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setVerticalSpacing(10)
        self.label_37 = QLabel(self.widget_26)
        self.label_37.setObjectName(u"label_37")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_37)

        self.tracert0 = QLineEdit(self.widget_26)
        self.tracert0.setObjectName(u"tracert0")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.tracert0)

        self.label_25 = QLabel(self.widget_26)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_25)

        self.tracert1 = QLineEdit(self.widget_26)
        self.tracert1.setObjectName(u"tracert1")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.tracert1)

        self.label_26 = QLabel(self.widget_26)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_26)

        self.tracert2 = QLineEdit(self.widget_26)
        self.tracert2.setObjectName(u"tracert2")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.tracert2)

        self.tracert4 = QRadioButton(self.widget_26)
        self.tracert4.setObjectName(u"tracert4")
        self.tracert4.setChecked(True)
        self.tracert4.setAutoRepeat(False)
        self.tracert4.setAutoExclusive(False)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.tracert4)

        self.tracert5 = QRadioButton(self.widget_26)
        self.tracert5.setObjectName(u"tracert5")
        self.tracert5.setCheckable(True)
        self.tracert5.setAutoRepeat(False)
        self.tracert5.setAutoExclusive(False)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.tracert5)

        self.label_27 = QLabel(self.widget_26)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_27)

        self.tracert3 = QLineEdit(self.widget_26)
        self.tracert3.setObjectName(u"tracert3")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.tracert3)


        self.verticalLayout_46.addWidget(self.widget_26)

        self.TracertAyudaBtn = QPushButton(self.widget_11)
        self.TracertAyudaBtn.setObjectName(u"TracertAyudaBtn")

        self.verticalLayout_46.addWidget(self.TracertAyudaBtn)

        self.TracertIniciarBtn = QPushButton(self.widget_11)
        self.TracertIniciarBtn.setObjectName(u"TracertIniciarBtn")

        self.verticalLayout_46.addWidget(self.TracertIniciarBtn)


        self.horizontalLayout_29.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_47 = QVBoxLayout(self.widget_12)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.SalidaTracert = QTextEdit(self.widget_12)
        self.SalidaTracert.setObjectName(u"SalidaTracert")
        self.SalidaTracert.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_47.addWidget(self.SalidaTracert)


        self.horizontalLayout_29.addWidget(self.widget_12)

        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_43.addWidget(self.scrollArea_11)

        self.ContenidosU.addWidget(self.TracertPag)
        self.ARPPag = QWidget()
        self.ARPPag.setObjectName(u"ARPPag")
        self.verticalLayout_42 = QVBoxLayout(self.ARPPag)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.scrollArea_12 = QScrollArea(self.ARPPag)
        self.scrollArea_12.setObjectName(u"scrollArea_12")
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 876, 460))
        self.horizontalLayout_30 = QHBoxLayout(self.scrollAreaWidgetContents_10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.widget_13 = QWidget(self.scrollAreaWidgetContents_10)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_48 = QVBoxLayout(self.widget_13)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_28 = QLabel(self.widget_13)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setWordWrap(True)

        self.verticalLayout_48.addWidget(self.label_28)

        self.BarDis = QComboBox(self.widget_13)
        self.BarDis.setObjectName(u"BarDis")

        self.verticalLayout_48.addWidget(self.BarDis)

        self.widget_27 = QWidget(self.widget_13)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_29 = QLabel(self.widget_27)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_35.addWidget(self.label_29)

        self.arp1 = QPushButton(self.widget_27)
        self.arp1.setObjectName(u"arp1")

        self.horizontalLayout_35.addWidget(self.arp1)


        self.verticalLayout_48.addWidget(self.widget_27)

        self.widget_30 = QWidget(self.widget_13)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_30 = QLabel(self.widget_30)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_36.addWidget(self.label_30)

        self.arp6 = QLineEdit(self.widget_30)
        self.arp6.setObjectName(u"arp6")

        self.horizontalLayout_36.addWidget(self.arp6)

        self.arp2 = QPushButton(self.widget_30)
        self.arp2.setObjectName(u"arp2")

        self.horizontalLayout_36.addWidget(self.arp2)


        self.verticalLayout_48.addWidget(self.widget_30)

        self.widget_8 = QWidget(self.widget_13)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_36 = QLabel(self.widget_8)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_21.addWidget(self.label_36)

        self.arp8 = QLineEdit(self.widget_8)
        self.arp8.setObjectName(u"arp8")

        self.horizontalLayout_21.addWidget(self.arp8)

        self.arp7 = QPushButton(self.widget_8)
        self.arp7.setObjectName(u"arp7")

        self.horizontalLayout_21.addWidget(self.arp7)


        self.verticalLayout_48.addWidget(self.widget_8)

        self.widget_28 = QWidget(self.widget_13)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.widget_28)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_37.addWidget(self.label_31)

        self.arp4 = QLineEdit(self.widget_28)
        self.arp4.setObjectName(u"arp4")

        self.horizontalLayout_37.addWidget(self.arp4)

        self.arp3 = QLineEdit(self.widget_28)
        self.arp3.setObjectName(u"arp3")

        self.horizontalLayout_37.addWidget(self.arp3)


        self.verticalLayout_48.addWidget(self.widget_28)

        self.arp5 = QPushButton(self.widget_13)
        self.arp5.setObjectName(u"arp5")

        self.verticalLayout_48.addWidget(self.arp5)

        self.ArpAyuda = QPushButton(self.widget_13)
        self.ArpAyuda.setObjectName(u"ArpAyuda")

        self.verticalLayout_48.addWidget(self.ArpAyuda)


        self.horizontalLayout_30.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.scrollAreaWidgetContents_10)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.SalidaARP = QTextEdit(self.widget_14)
        self.SalidaARP.setObjectName(u"SalidaARP")
        self.SalidaARP.setLineWrapMode(QTextEdit.NoWrap)

        self.horizontalLayout_34.addWidget(self.SalidaARP)


        self.horizontalLayout_30.addWidget(self.widget_14)

        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_42.addWidget(self.scrollArea_12)

        self.ContenidosU.addWidget(self.ARPPag)
        self.RoutePag = QWidget()
        self.RoutePag.setObjectName(u"RoutePag")
        self.verticalLayout_41 = QVBoxLayout(self.RoutePag)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.scrollArea_13 = QScrollArea(self.RoutePag)
        self.scrollArea_13.setObjectName(u"scrollArea_13")
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 333, 207))
        self.horizontalLayout_31 = QHBoxLayout(self.scrollAreaWidgetContents_11)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.widget_15 = QWidget(self.scrollAreaWidgetContents_11)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_36 = QVBoxLayout(self.widget_15)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_17 = QLabel(self.widget_15)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_36.addWidget(self.label_17, 0, Qt.AlignTop)

        self.widget_7 = QWidget(self.widget_15)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.gridLayout_5 = QGridLayout(self.widget_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.var1 = QPushButton(self.widget_7)
        self.var1.setObjectName(u"var1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.var1.sizePolicy().hasHeightForWidth())
        self.var1.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.var1, 0, 0, 1, 1)

        self.var5 = QPushButton(self.widget_7)
        self.var5.setObjectName(u"var5")
        sizePolicy4.setHeightForWidth(self.var5.sizePolicy().hasHeightForWidth())
        self.var5.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.var5, 2, 0, 1, 1)

        self.var4 = QPushButton(self.widget_7)
        self.var4.setObjectName(u"var4")
        sizePolicy4.setHeightForWidth(self.var4.sizePolicy().hasHeightForWidth())
        self.var4.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.var4, 1, 1, 1, 1)

        self.var2 = QPushButton(self.widget_7)
        self.var2.setObjectName(u"var2")
        sizePolicy4.setHeightForWidth(self.var2.sizePolicy().hasHeightForWidth())
        self.var2.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.var2, 0, 1, 1, 1)

        self.var6 = QPushButton(self.widget_7)
        self.var6.setObjectName(u"var6")
        sizePolicy4.setHeightForWidth(self.var6.sizePolicy().hasHeightForWidth())
        self.var6.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.var6, 2, 1, 1, 1)

        self.var3 = QPushButton(self.widget_7)
        self.var3.setObjectName(u"var3")
        sizePolicy4.setHeightForWidth(self.var3.sizePolicy().hasHeightForWidth())
        self.var3.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.var3, 1, 0, 1, 1)

        self.var7 = QPushButton(self.widget_7)
        self.var7.setObjectName(u"var7")
        sizePolicy4.setHeightForWidth(self.var7.sizePolicy().hasHeightForWidth())
        self.var7.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.var7, 3, 0, 1, 1)

        self.var8 = QPushButton(self.widget_7)
        self.var8.setObjectName(u"var8")
        sizePolicy4.setHeightForWidth(self.var8.sizePolicy().hasHeightForWidth())
        self.var8.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.var8, 3, 1, 1, 1)


        self.verticalLayout_36.addWidget(self.widget_7)


        self.horizontalLayout_31.addWidget(self.widget_15)

        self.SalidaVar = QTextEdit(self.scrollAreaWidgetContents_11)
        self.SalidaVar.setObjectName(u"SalidaVar")
        self.SalidaVar.setLineWrapMode(QTextEdit.NoWrap)

        self.horizontalLayout_31.addWidget(self.SalidaVar)

        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_11)
        self.SalidaVar.raise_()
        self.widget_15.raise_()

        self.verticalLayout_41.addWidget(self.scrollArea_13)

        self.ContenidosU.addWidget(self.RoutePag)
        self.NSPag = QWidget()
        self.NSPag.setObjectName(u"NSPag")
        self.verticalLayout_40 = QVBoxLayout(self.NSPag)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.scrollArea_14 = QScrollArea(self.NSPag)
        self.scrollArea_14.setObjectName(u"scrollArea_14")
        self.scrollArea_14.setWidgetResizable(True)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 299, 232))
        self.horizontalLayout_26 = QHBoxLayout(self.scrollAreaWidgetContents_12)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.widget_18 = QWidget(self.scrollAreaWidgetContents_12)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_49 = QVBoxLayout(self.widget_18)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_32 = QLabel(self.widget_18)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setWordWrap(True)

        self.verticalLayout_49.addWidget(self.label_32)

        self.widget_31 = QWidget(self.widget_18)
        self.widget_31.setObjectName(u"widget_31")
        self.formLayout_3 = QFormLayout(self.widget_31)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_33 = QLabel(self.widget_31)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_33)

        self.nslo1 = QLineEdit(self.widget_31)
        self.nslo1.setObjectName(u"nslo1")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.nslo1)

        self.label_34 = QLabel(self.widget_31)
        self.label_34.setObjectName(u"label_34")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_34)

        self.nslo2 = QLineEdit(self.widget_31)
        self.nslo2.setObjectName(u"nslo2")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.nslo2)


        self.verticalLayout_49.addWidget(self.widget_31)

        self.NSLOAyudaBtn = QPushButton(self.widget_18)
        self.NSLOAyudaBtn.setObjectName(u"NSLOAyudaBtn")

        self.verticalLayout_49.addWidget(self.NSLOAyudaBtn)

        self.NSLOIniciarBtn = QPushButton(self.widget_18)
        self.NSLOIniciarBtn.setObjectName(u"NSLOIniciarBtn")

        self.verticalLayout_49.addWidget(self.NSLOIniciarBtn)


        self.horizontalLayout_26.addWidget(self.widget_18)

        self.widget_17 = QWidget(self.scrollAreaWidgetContents_12)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_50 = QVBoxLayout(self.widget_17)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.textEdit = QTextEdit(self.widget_17)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_50.addWidget(self.textEdit)


        self.horizontalLayout_26.addWidget(self.widget_17)

        self.scrollArea_14.setWidget(self.scrollAreaWidgetContents_12)

        self.verticalLayout_40.addWidget(self.scrollArea_14)

        self.ContenidosU.addWidget(self.NSPag)

        self.horizontalLayout_18.addWidget(self.ContenidosU)


        self.horizontalLayout_20.addWidget(self.widget_6)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_17.addWidget(self.scrollArea_6)


        self.verticalLayout_21.addWidget(self.widget_5)

        self.Contenidos.addWidget(self.pUtil)
        self.pReport = QWidget()
        self.pReport.setObjectName(u"pReport")
        self.verticalLayout_22 = QVBoxLayout(self.pReport)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.Reportes = QScrollArea(self.pReport)
        self.Reportes.setObjectName(u"Reportes")
        self.Reportes.setWidgetResizable(True)
        self.scrollAreaWidgetContents_25 = QWidget()
        self.scrollAreaWidgetContents_25.setObjectName(u"scrollAreaWidgetContents_25")
        self.scrollAreaWidgetContents_25.setGeometry(QRect(0, 0, 286, 1803))
        self.verticalLayout_65 = QVBoxLayout(self.scrollAreaWidgetContents_25)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.RG = QWidget(self.scrollAreaWidgetContents_25)
        self.RG.setObjectName(u"RG")
        self.horizontalLayout_65 = QHBoxLayout(self.RG)
        self.horizontalLayout_65.setSpacing(20)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_109 = QLabel(self.RG)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setPixmap(QPixmap(u":/INTER/Imagenes/Reportes/General.png"))

        self.horizontalLayout_65.addWidget(self.label_109, 0, Qt.AlignLeft)

        self.label_110 = QLabel(self.RG)
        self.label_110.setObjectName(u"label_110")
        sizePolicy.setHeightForWidth(self.label_110.sizePolicy().hasHeightForWidth())
        self.label_110.setSizePolicy(sizePolicy)
        self.label_110.setWordWrap(True)

        self.horizontalLayout_65.addWidget(self.label_110)

        self.widget_53 = QWidget(self.RG)
        self.widget_53.setObjectName(u"widget_53")
        self.verticalLayout_71 = QVBoxLayout(self.widget_53)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.GRG = QPushButton(self.widget_53)
        self.GRG.setObjectName(u"GRG")

        self.verticalLayout_71.addWidget(self.GRG)


        self.horizontalLayout_65.addWidget(self.widget_53, 0, Qt.AlignRight)


        self.verticalLayout_65.addWidget(self.RG)

        self.R1 = QWidget(self.scrollAreaWidgetContents_25)
        self.R1.setObjectName(u"R1")
        self.horizontalLayout_62 = QHBoxLayout(self.R1)
        self.horizontalLayout_62.setSpacing(20)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_103 = QLabel(self.R1)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setPixmap(QPixmap(u":/INTER/Imagenes/Reportes/CLUES.png"))

        self.horizontalLayout_62.addWidget(self.label_103, 0, Qt.AlignLeft)

        self.label_104 = QLabel(self.R1)
        self.label_104.setObjectName(u"label_104")
        sizePolicy.setHeightForWidth(self.label_104.sizePolicy().hasHeightForWidth())
        self.label_104.setSizePolicy(sizePolicy)
        self.label_104.setWordWrap(True)

        self.horizontalLayout_62.addWidget(self.label_104)

        self.widget_57 = QWidget(self.R1)
        self.widget_57.setObjectName(u"widget_57")
        self.verticalLayout_68 = QVBoxLayout(self.widget_57)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.GR3 = QPushButton(self.widget_57)
        self.GR3.setObjectName(u"GR3")

        self.verticalLayout_68.addWidget(self.GR3)


        self.horizontalLayout_62.addWidget(self.widget_57, 0, Qt.AlignRight)


        self.verticalLayout_65.addWidget(self.R1)

        self.R7 = QWidget(self.scrollAreaWidgetContents_25)
        self.R7.setObjectName(u"R7")
        self.horizontalLayout_67 = QHBoxLayout(self.R7)
        self.horizontalLayout_67.setSpacing(20)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_113 = QLabel(self.R7)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setPixmap(QPixmap(u":/INTER/Imagenes/Reportes/Inventario.png"))

        self.horizontalLayout_67.addWidget(self.label_113, 0, Qt.AlignLeft)

        self.label_114 = QLabel(self.R7)
        self.label_114.setObjectName(u"label_114")
        sizePolicy.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy)
        self.label_114.setWordWrap(True)

        self.horizontalLayout_67.addWidget(self.label_114)

        self.widget_61 = QWidget(self.R7)
        self.widget_61.setObjectName(u"widget_61")
        self.verticalLayout_73 = QVBoxLayout(self.widget_61)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.GR7 = QPushButton(self.widget_61)
        self.GR7.setObjectName(u"GR7")

        self.verticalLayout_73.addWidget(self.GR7)


        self.horizontalLayout_67.addWidget(self.widget_61, 0, Qt.AlignLeft)


        self.verticalLayout_65.addWidget(self.R7)

        self.R4 = QWidget(self.scrollAreaWidgetContents_25)
        self.R4.setObjectName(u"R4")
        self.horizontalLayout_63 = QHBoxLayout(self.R4)
        self.horizontalLayout_63.setSpacing(20)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_105 = QLabel(self.R4)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setPixmap(QPixmap(u":/INTER/Imagenes/Reportes/HOST.png"))

        self.horizontalLayout_63.addWidget(self.label_105, 0, Qt.AlignLeft)

        self.label_106 = QLabel(self.R4)
        self.label_106.setObjectName(u"label_106")
        sizePolicy.setHeightForWidth(self.label_106.sizePolicy().hasHeightForWidth())
        self.label_106.setSizePolicy(sizePolicy)
        self.label_106.setWordWrap(True)

        self.horizontalLayout_63.addWidget(self.label_106)

        self.widget_58 = QWidget(self.R4)
        self.widget_58.setObjectName(u"widget_58")
        self.verticalLayout_69 = QVBoxLayout(self.widget_58)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.GR4 = QPushButton(self.widget_58)
        self.GR4.setObjectName(u"GR4")

        self.verticalLayout_69.addWidget(self.GR4)


        self.horizontalLayout_63.addWidget(self.widget_58, 0, Qt.AlignRight)


        self.verticalLayout_65.addWidget(self.R4)

        self.R6 = QWidget(self.scrollAreaWidgetContents_25)
        self.R6.setObjectName(u"R6")
        self.horizontalLayout_66 = QHBoxLayout(self.R6)
        self.horizontalLayout_66.setSpacing(20)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_111 = QLabel(self.R6)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setPixmap(QPixmap(u":/INTER/Imagenes/Reportes/PROVEED.png"))

        self.horizontalLayout_66.addWidget(self.label_111)

        self.label_112 = QLabel(self.R6)
        self.label_112.setObjectName(u"label_112")
        sizePolicy.setHeightForWidth(self.label_112.sizePolicy().hasHeightForWidth())
        self.label_112.setSizePolicy(sizePolicy)
        self.label_112.setWordWrap(True)

        self.horizontalLayout_66.addWidget(self.label_112)

        self.widget_59 = QWidget(self.R6)
        self.widget_59.setObjectName(u"widget_59")
        self.verticalLayout_72 = QVBoxLayout(self.widget_59)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.GR6 = QPushButton(self.widget_59)
        self.GR6.setObjectName(u"GR6")

        self.verticalLayout_72.addWidget(self.GR6)


        self.horizontalLayout_66.addWidget(self.widget_59, 0, Qt.AlignLeft)


        self.verticalLayout_65.addWidget(self.R6)

        self.R2 = QWidget(self.scrollAreaWidgetContents_25)
        self.R2.setObjectName(u"R2")
        self.horizontalLayout_38 = QHBoxLayout(self.R2)
        self.horizontalLayout_38.setSpacing(20)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_42 = QLabel(self.R2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setPixmap(QPixmap(u":/INTER/Imagenes/Reportes/Speed.png"))

        self.horizontalLayout_38.addWidget(self.label_42, 0, Qt.AlignLeft)

        self.label_100 = QLabel(self.R2)
        self.label_100.setObjectName(u"label_100")
        sizePolicy.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy)
        self.label_100.setWordWrap(True)

        self.horizontalLayout_38.addWidget(self.label_100)

        self.widget_55 = QWidget(self.R2)
        self.widget_55.setObjectName(u"widget_55")
        self.verticalLayout_67 = QVBoxLayout(self.widget_55)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.GR1 = QPushButton(self.widget_55)
        self.GR1.setObjectName(u"GR1")

        self.verticalLayout_67.addWidget(self.GR1)

        self.GRBorrarP = QPushButton(self.widget_55)
        self.GRBorrarP.setObjectName(u"GRBorrarP")

        self.verticalLayout_67.addWidget(self.GRBorrarP)


        self.horizontalLayout_38.addWidget(self.widget_55, 0, Qt.AlignRight)


        self.verticalLayout_65.addWidget(self.R2)

        self.R3 = QWidget(self.scrollAreaWidgetContents_25)
        self.R3.setObjectName(u"R3")
        self.horizontalLayout_39 = QHBoxLayout(self.R3)
        self.horizontalLayout_39.setSpacing(20)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_101 = QLabel(self.R3)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setPixmap(QPixmap(u":/INTER/Imagenes/Reportes/Reportes.png"))

        self.horizontalLayout_39.addWidget(self.label_101, 0, Qt.AlignLeft)

        self.label_102 = QLabel(self.R3)
        self.label_102.setObjectName(u"label_102")
        sizePolicy.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy)
        self.label_102.setWordWrap(True)

        self.horizontalLayout_39.addWidget(self.label_102)

        self.widget_56 = QWidget(self.R3)
        self.widget_56.setObjectName(u"widget_56")
        self.verticalLayout_66 = QVBoxLayout(self.widget_56)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.GR2 = QPushButton(self.widget_56)
        self.GR2.setObjectName(u"GR2")

        self.verticalLayout_66.addWidget(self.GR2)

        self.GRBorrarS = QPushButton(self.widget_56)
        self.GRBorrarS.setObjectName(u"GRBorrarS")

        self.verticalLayout_66.addWidget(self.GRBorrarS)


        self.horizontalLayout_39.addWidget(self.widget_56)


        self.verticalLayout_65.addWidget(self.R3)

        self.R5 = QWidget(self.scrollAreaWidgetContents_25)
        self.R5.setObjectName(u"R5")
        self.horizontalLayout_64 = QHBoxLayout(self.R5)
        self.horizontalLayout_64.setSpacing(20)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_107 = QLabel(self.R5)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setPixmap(QPixmap(u":/INTER/Imagenes/Reportes/HISTORIA.png"))

        self.horizontalLayout_64.addWidget(self.label_107, 0, Qt.AlignLeft)

        self.label_108 = QLabel(self.R5)
        self.label_108.setObjectName(u"label_108")
        sizePolicy.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy)
        self.label_108.setWordWrap(True)

        self.horizontalLayout_64.addWidget(self.label_108)

        self.widget_52 = QWidget(self.R5)
        self.widget_52.setObjectName(u"widget_52")
        self.verticalLayout_70 = QVBoxLayout(self.widget_52)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.GR5 = QPushButton(self.widget_52)
        self.GR5.setObjectName(u"GR5")

        self.verticalLayout_70.addWidget(self.GR5)

        self.GRBorrarH = QPushButton(self.widget_52)
        self.GRBorrarH.setObjectName(u"GRBorrarH")

        self.verticalLayout_70.addWidget(self.GRBorrarH)


        self.horizontalLayout_64.addWidget(self.widget_52, 0, Qt.AlignLeft)


        self.verticalLayout_65.addWidget(self.R5)

        self.R8 = QWidget(self.scrollAreaWidgetContents_25)
        self.R8.setObjectName(u"R8")
        self.horizontalLayout_69 = QHBoxLayout(self.R8)
        self.horizontalLayout_69.setSpacing(20)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_122 = QLabel(self.R8)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMaximumSize(QSize(96, 96))
        self.label_122.setPixmap(QPixmap(u":/Logo/Imagenes/WALL.png"))
        self.label_122.setScaledContents(True)

        self.horizontalLayout_69.addWidget(self.label_122, 0, Qt.AlignLeft)

        self.label_121 = QLabel(self.R8)
        self.label_121.setObjectName(u"label_121")
        sizePolicy.setHeightForWidth(self.label_121.sizePolicy().hasHeightForWidth())
        self.label_121.setSizePolicy(sizePolicy)
        self.label_121.setWordWrap(True)

        self.horizontalLayout_69.addWidget(self.label_121)

        self.widget_62 = QWidget(self.R8)
        self.widget_62.setObjectName(u"widget_62")
        self.verticalLayout_76 = QVBoxLayout(self.widget_62)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.GR8 = QPushButton(self.widget_62)
        self.GR8.setObjectName(u"GR8")

        self.verticalLayout_76.addWidget(self.GR8)

        self.GRBorrarPr = QPushButton(self.widget_62)
        self.GRBorrarPr.setObjectName(u"GRBorrarPr")

        self.verticalLayout_76.addWidget(self.GRBorrarPr)


        self.horizontalLayout_69.addWidget(self.widget_62, 0, Qt.AlignRight)


        self.verticalLayout_65.addWidget(self.R8)

        self.Reportes.setWidget(self.scrollAreaWidgetContents_25)

        self.verticalLayout_22.addWidget(self.Reportes)

        self.Contenidos.addWidget(self.pReport)

        self.verticalLayout_16.addWidget(self.Contenidos)


        self.horizontalLayout_7.addWidget(self.Contenido)

        self.MenuDerecho = QWidget(self.Cuerpo)
        self.MenuDerecho.setObjectName(u"MenuDerecho")
        self.MenuDerecho.setMinimumSize(QSize(0, 0))
        self.MenuDerecho.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.MenuDerecho)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.SubMenuDerecho = QWidget(self.MenuDerecho)
        self.SubMenuDerecho.setObjectName(u"SubMenuDerecho")
        self.verticalLayout_13 = QVBoxLayout(self.SubMenuDerecho)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.SubMenuDerecho)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.DerechoBtn = QPushButton(self.frame_8)
        self.DerechoBtn.setObjectName(u"DerechoBtn")
        self.DerechoBtn.setIcon(icon11)
        self.DerechoBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.DerechoBtn, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.frame_8)

        self.ContenidoDerecho = QStackedWidget(self.SubMenuDerecho)
        self.ContenidoDerecho.setObjectName(u"ContenidoDerecho")
        self.pDisp = QWidget()
        self.pDisp.setObjectName(u"pDisp")
        self.verticalLayout_14 = QVBoxLayout(self.pDisp)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.scrollArea = QScrollArea(self.pDisp)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.DispositivosW = QWidget()
        self.DispositivosW.setObjectName(u"DispositivosW")
        self.DispositivosW.setGeometry(QRect(0, 0, 18, 478))
        self.verticalLayout_6 = QVBoxLayout(self.DispositivosW)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea.setWidget(self.DispositivosW)

        self.verticalLayout_14.addWidget(self.scrollArea)

        self.ContenidoDerecho.addWidget(self.pDisp)
        self.pUse = QWidget()
        self.pUse.setObjectName(u"pUse")
        self.verticalLayout_15 = QVBoxLayout(self.pUse)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollArea_2 = QScrollArea(self.pUse)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.UsuariosW = QWidget()
        self.UsuariosW.setObjectName(u"UsuariosW")
        self.UsuariosW.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_26 = QVBoxLayout(self.UsuariosW)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.scrollArea_2.setWidget(self.UsuariosW)

        self.verticalLayout_15.addWidget(self.scrollArea_2)

        self.ContenidoDerecho.addWidget(self.pUse)

        self.verticalLayout_13.addWidget(self.ContenidoDerecho)


        self.verticalLayout_12.addWidget(self.SubMenuDerecho)


        self.horizontalLayout_7.addWidget(self.MenuDerecho)


        self.verticalLayout_11.addWidget(self.Cuerpo)

        self.Notificacion = QWidget(self.PantallaPrincipal)
        self.Notificacion.setObjectName(u"Notificacion")
        self.Notificacion.setMinimumSize(QSize(0, 0))
        self.Notificacion.setMaximumSize(QSize(16777215, 0))
        self.verticalLayout_23 = QVBoxLayout(self.Notificacion)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.SubNotificacion = QWidget(self.Notificacion)
        self.SubNotificacion.setObjectName(u"SubNotificacion")
        self.verticalLayout_24 = QVBoxLayout(self.SubNotificacion)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.widget_51 = QWidget(self.SubNotificacion)
        self.widget_51.setObjectName(u"widget_51")
        self.horizontalLayout_68 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.widget_51)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_68.addWidget(self.label_4)

        self.BasuraNotif = QPushButton(self.widget_51)
        self.BasuraNotif.setObjectName(u"BasuraNotif")
        self.BasuraNotif.setIcon(icon23)

        self.horizontalLayout_68.addWidget(self.BasuraNotif, 0, Qt.AlignRight)

        self.CerrarNotif = QPushButton(self.widget_51)
        self.CerrarNotif.setObjectName(u"CerrarNotif")
        icon32 = QIcon()
        icon32.addFile(u":/Iconos2/Imagenes/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CerrarNotif.setIcon(icon32)
        self.CerrarNotif.setIconSize(QSize(24, 24))

        self.horizontalLayout_68.addWidget(self.CerrarNotif, 0, Qt.AlignRight)


        self.verticalLayout_24.addWidget(self.widget_51)

        self.NotificacionesW = QScrollArea(self.SubNotificacion)
        self.NotificacionesW.setObjectName(u"NotificacionesW")
        self.NotificacionesW.setWidgetResizable(True)
        self.scrollAreaWidgetContents_27 = QWidget()
        self.scrollAreaWidgetContents_27.setObjectName(u"scrollAreaWidgetContents_27")
        self.scrollAreaWidgetContents_27.setGeometry(QRect(0, 0, 991, 16))
        self.NotificacionesW.setWidget(self.scrollAreaWidgetContents_27)

        self.verticalLayout_24.addWidget(self.NotificacionesW)


        self.verticalLayout_23.addWidget(self.SubNotificacion)


        self.verticalLayout_11.addWidget(self.Notificacion)

        self.Pie = QWidget(self.PantallaPrincipal)
        self.Pie.setObjectName(u"Pie")
        self.horizontalLayout_10 = QHBoxLayout(self.Pie)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Estado = QWidget(self.Pie)
        self.Estado.setObjectName(u"Estado")
        self.horizontalLayout_11 = QHBoxLayout(self.Estado)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.Estado)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)


        self.horizontalLayout_10.addWidget(self.Estado)

        self.SizeGrip = QWidget(self.Pie)
        self.SizeGrip.setObjectName(u"SizeGrip")
        self.SizeGrip.setMaximumSize(QSize(40, 40))
        self.verticalLayout_25 = QVBoxLayout(self.SizeGrip)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.SizeGrip)
        self.label_7.setObjectName(u"label_7")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy5)
        self.label_7.setPixmap(QPixmap(u":/Iconos2/Imagenes/icons/cil-size-grip.png"))

        self.verticalLayout_25.addWidget(self.label_7)


        self.horizontalLayout_10.addWidget(self.SizeGrip)


        self.verticalLayout_11.addWidget(self.Pie)


        self.horizontalLayout.addWidget(self.PantallaPrincipal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.ContenidoCentral.setCurrentIndex(1)
        self.Contenidos.setCurrentIndex(0)
        self.ContenidoDerecho.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema MGR", None))
#if QT_CONFIG(tooltip)
        self.Menu.setToolTip(QCoreApplication.translate("MainWindow", u"Desplegar/Contraer Men\u00fa", None))
#endif // QT_CONFIG(tooltip)
        self.Menu.setText("")
#if QT_CONFIG(tooltip)
        self.DashboardBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Ir al tablero principal", None))
#endif // QT_CONFIG(tooltip)
        self.DashboardBtn.setText(QCoreApplication.translate("MainWindow", u"  Tablero Principal", None))
#if QT_CONFIG(tooltip)
        self.VelocidadBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Comprobar velocidad de red", None))
#endif // QT_CONFIG(tooltip)
        self.VelocidadBtn.setText(QCoreApplication.translate("MainWindow", u"  Velocidad de Red", None))
#if QT_CONFIG(tooltip)
        self.TraficoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Tr\u00e1fico de red", None))
#endif // QT_CONFIG(tooltip)
        self.TraficoBtn.setText(QCoreApplication.translate("MainWindow", u"  Tr\u00e1fico de red", None))
#if QT_CONFIG(tooltip)
        self.GestionBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Herramientas de Gesti\u00f3n de red", None))
#endif // QT_CONFIG(tooltip)
        self.GestionBtn.setText(QCoreApplication.translate("MainWindow", u"  Gesti\u00f3n de red", None))
#if QT_CONFIG(tooltip)
        self.UtilidadesBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Utilidades", None))
#endif // QT_CONFIG(tooltip)
        self.UtilidadesBtn.setText(QCoreApplication.translate("MainWindow", u"  Utilidades", None))
#if QT_CONFIG(tooltip)
        self.RerportesBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Reportes de red", None))
#endif // QT_CONFIG(tooltip)
        self.RerportesBtn.setText(QCoreApplication.translate("MainWindow", u"  Reportes", None))
#if QT_CONFIG(tooltip)
        self.AlertasBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Alertas y notificaciones.", None))
#endif // QT_CONFIG(tooltip)
        self.AlertasBtn.setText(QCoreApplication.translate("MainWindow", u"  Alertas", None))
#if QT_CONFIG(tooltip)
        self.AyudaBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Ayuda sobre el software", None))
#endif // QT_CONFIG(tooltip)
        self.AyudaBtn.setText(QCoreApplication.translate("MainWindow", u"  Ayuda", None))
#if QT_CONFIG(tooltip)
        self.AjustesBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n de la aplicaci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.AjustesBtn.setText(QCoreApplication.translate("MainWindow", u"  Ajustes", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"M\u00e1s men\u00fa", None))
#if QT_CONFIG(tooltip)
        self.MasMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Cerrar Men\u00fa", None))
#endif // QT_CONFIG(tooltip)
        self.MasMenuBtn.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">El presente software esta desarrollado en el lenguaje de programaci\u00f3n python a traves del framework QT6 y PySide6, por lo que su funcionamiento gr\u00e1fico y l\u00f3gico estan limitados sobre estas tecnolog\u00edas.</p><p align=\"justify\">Al haber pulsado sobre este apartado de ayuda, se debio de abrir de manera automatica un archivo PDF sobre el navegador, en caso de que no se haya abierto es porque el archivo se elimino o bien no se cuenta con un programa dentro de la computadora para abrir estos archivos.</p><p align=\"justify\">Para mas ayuda sobre el software o algun error de gran impacto, comuniquese al correo julioponcecamacho@gmail.com, el cual es el desarrollador del software realizado como proyecto de residencia.</p></body></html>", None))
        self.label_115.setText("")
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Ventana:", None))
        self.Ajus1.setItemText(0, QCoreApplication.translate("MainWindow", u"Propia del Software", None))
        self.Ajus1.setItemText(1, QCoreApplication.translate("MainWindow", u"Propia del SO", None))

        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Tema:", None))
        self.Ajus2.setItemText(0, QCoreApplication.translate("MainWindow", u"Obscuro", None))
        self.Ajus2.setItemText(1, QCoreApplication.translate("MainWindow", u"Claro", None))

        self.label_118.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Detecci\u00f3n<br/>de dispositivos:</p></body></html>", None))
        self.Ajus3.setItemText(0, QCoreApplication.translate("MainWindow", u"Preciso (ARP y Ping)", None))
        self.Ajus3.setItemText(1, QCoreApplication.translate("MainWindow", u"R\u00e1pido (Solo ARP)", None))

        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Intervalo<br> entre detecci\u00f3n:", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Tiempo para<br/>captura de<br> paquetes:</p></body></html>", None))
        self.AplicarAjusBtn.setText(QCoreApplication.translate("MainWindow", u"Aplicar Configuraci\u00f3n", None))
        self.Logo.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sistema de Monitoreo y Gesti\u00f3n de red", None))
#if QT_CONFIG(tooltip)
        self.InterRedBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Interfaz de red", None))
#endif // QT_CONFIG(tooltip)
        self.InterRedBtn.setText("")
#if QT_CONFIG(tooltip)
        self.UserBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Dispositivos en red", None))
#endif // QT_CONFIG(tooltip)
        self.UserBtn.setText("")
#if QT_CONFIG(tooltip)
        self.MinBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimizar", None))
#endif // QT_CONFIG(tooltip)
        self.MinBtn.setText("")
#if QT_CONFIG(tooltip)
        self.MaxBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Cambiar Tama\u00f1o", None))
#endif // QT_CONFIG(tooltip)
        self.MaxBtn.setText("")
#if QT_CONFIG(tooltip)
        self.SalirBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Salir", None))
#endif // QT_CONFIG(tooltip)
        self.SalirBtn.setText("")
        self.label_83.setText("")
        self.DatosRed.setText(QCoreApplication.translate("MainWindow", u"\n"
"<p align=\"center\"> Datos de Red Actual<br> ___________________________________________</p>\n"
"<b>Nombre Interfaz:</b><br>\n"
"<b>Descripci\u00f3n:</b><br>\n"
"<b>SSID:</b><br>\n"
"<b>Tipo de radio:</b><br>\n"
"<b>Banda:</b><br>\n"
"<b>Velocidad de Transmision:</b><br>\n"
"<b>Velocidad de Recepci\u00f3n:</b><br>\n"
"<b>Se\u00f1al:</b><br>\n"
"<b>Direcci\u00f3n IPv4:</b><br>\n"
"<b>Puerta de Enlace:</b><br>\n"
"<b>Sub-M\u00e1scara de red:</b><br>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Velocidad de red actual", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Dominios consultados en la red", None))
        self.Velocidad_Salida.setText(QCoreApplication.translate("MainWindow", u"0 Mbp/s", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Descarga", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Subida", None))
        self.Subida_Salida.setText(QCoreApplication.translate("MainWindow", u"0 Mbp/s", None))
        self.Ping_Salida.setText(QCoreApplication.translate("MainWindow", u"0 ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.SpeedRed.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Servidor:", None))
        self.SpeedServidor.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Sponsor", None))
        self.SpeedSponsor.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Ping Descarga:", None))
        self.SpeedBajada.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Ping Subida:", None))
        self.SpeedSubida.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.PruebaVelBtn.setText(QCoreApplication.translate("MainWindow", u"  Iniciar", None))
        self.PruebaVelTBtn.setText(QCoreApplication.translate("MainWindow", u"Iniciar para todas las Redes (Solo Wi-Fi)", None))
        self.BorrarPruebas.setText(QCoreApplication.translate("MainWindow", u"Borrar Historial", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Filtrado:", None))
        self.PagTrafico.setText(QCoreApplication.translate("MainWindow", u"Analisis del Tr\u00e1fico de red", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Filtrado:", None))
        self.InicioTraficoBtn.setText(QCoreApplication.translate("MainWindow", u"Iniciar / Detener", None))
        self.VerDomBtn.setText(QCoreApplication.translate("MainWindow", u"Ver Dominios", None))
        self.RestabBtn.setText(QCoreApplication.translate("MainWindow", u"Restablecer", None))
        ___qtablewidgetitem = self.TablaPaquetes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.TablaPaquetes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem2 = self.TablaPaquetes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Protocolo", None));
        ___qtablewidgetitem3 = self.TablaPaquetes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o", None));
        ___qtablewidgetitem4 = self.TablaPaquetes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Origen", None));
        ___qtablewidgetitem5 = self.TablaPaquetes.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Destino", None));
        ___qtablewidgetitem6 = self.TablaPaquetes.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None));
        self.TituloSalidaPaq.setText(QCoreApplication.translate("MainWindow", u"Titulo", None))
        self.SalirSalidaPaq.setText("")
        self.PagGestion.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de red", None))
        self.G_PR.setText(QCoreApplication.translate("MainWindow", u"Problemas de Red", None))
        self.G_R.setText(QCoreApplication.translate("MainWindow", u"Reportes", None))
        self.G_I.setText(QCoreApplication.translate("MainWindow", u"Inventario ", None))
        self.G_P.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        self.G_RD.setText(QCoreApplication.translate("MainWindow", u"Redes", None))
        self.G_C.setText(QCoreApplication.translate("MainWindow", u"Historial No. Conexiones", None))
        self.G_H.setText(QCoreApplication.translate("MainWindow", u"Historial Hosts", None))
        self.G_CR.setText(QCoreApplication.translate("MainWindow", u"Control Red", None))
        self.G_SU.setText(QCoreApplication.translate("MainWindow", u"Unidades", None))
        self.G_D.setText(QCoreApplication.translate("MainWindow", u"Departamentos", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Filtrar:", None))
        self.GAgregarBtn.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.GModificarBtn.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.GEliminarBtn.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"      Fecha:               ", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Red:              ", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Departamento:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"      Descripci\u00f3n", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Corregido:     ", None))
        self.PR_COR.setItemText(0, QCoreApplication.translate("MainWindow", u"No corregido", None))
        self.PR_COR.setItemText(1, QCoreApplication.translate("MainWindow", u"Corregido", None))

        self.label_47.setText(QCoreApplication.translate("MainWindow", u"     Soluci\u00f3n:      ", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"     Fecha Corecci\u00f3n:", None))
        self.G_AgregarBtn.setText(QCoreApplication.translate("MainWindow", u"Agregar Registro", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Departamento:", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Ubicaci\u00f3n:", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Tipo Conexi\u00f3n:", None))
        self.I_TC.setItemText(0, QCoreApplication.translate("MainWindow", u"Inal\u00e1mbrica", None))
        self.I_TC.setItemText(1, QCoreApplication.translate("MainWindow", u"Alambrica", None))
        self.I_TC.setItemText(2, QCoreApplication.translate("MainWindow", u"No aplica", None))

        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.I_ADD.setText(QCoreApplication.translate("MainWindow", u"Agregar Registro", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"     Descripci\u00f3n:", None))
        self.D_ADD.setText(QCoreApplication.translate("MainWindow", u"Agregar Registro", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Folio:          ", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.R_ACUDIO.setItemText(0, QCoreApplication.translate("MainWindow", u"Acudio al sitio", None))
        self.R_ACUDIO.setItemText(1, QCoreApplication.translate("MainWindow", u"No acudio al sitio", None))

        self.R_REMOSIT.setItemText(0, QCoreApplication.translate("MainWindow", u"Procedimientos en Sitio", None))
        self.R_REMOSIT.setItemText(1, QCoreApplication.translate("MainWindow", u"Procedimiento de manera Remota", None))

        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Proveedor:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Motivo:     ", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Atendio:", None))
        self.R_ADD.setText(QCoreApplication.translate("MainWindow", u"Agregar Registro", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Transmisi\u00f3n:", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.P_ADD.setText(QCoreApplication.translate("MainWindow", u"Agregar Registro", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Responsable:", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Departamento:", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"No. Inventario:", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Host:", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"MAC:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"VENDOR:", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Observaciones:", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Estado IP:", None))
        self.CR_STAT.setItemText(0, QCoreApplication.translate("MainWindow", u"Libre", None))
        self.CR_STAT.setItemText(1, QCoreApplication.translate("MainWindow", u"Ocupado", None))

        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.CR_TIP.setItemText(0, QCoreApplication.translate("MainWindow", u"M\u00f3vil", None))
        self.CR_TIP.setItemText(1, QCoreApplication.translate("MainWindow", u"Laptop", None))
        self.CR_TIP.setItemText(2, QCoreApplication.translate("MainWindow", u"Escritorio", None))

        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Verificado:", None))
        self.CR_VERFI.setItemText(0, QCoreApplication.translate("MainWindow", u"No verificado", None))
        self.CR_VERFI.setItemText(1, QCoreApplication.translate("MainWindow", u"No permitido", None))
        self.CR_VERFI.setItemText(2, QCoreApplication.translate("MainWindow", u"Verificado", None))

        self.CR_ADD.setText(QCoreApplication.translate("MainWindow", u"Agregar Host", None))
        self.RD_SSID.setText(QCoreApplication.translate("MainWindow", u"SSID:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Subida:", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Bajada:", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Proveedor:", None))
        self.RD_ADD.setText(QCoreApplication.translate("MainWindow", u"Agregar Registro", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Servicio Internet:", None))
        self.SU_SERV.setItemText(0, QCoreApplication.translate("MainWindow", u"Con Servicio", None))
        self.SU_SERV.setItemText(1, QCoreApplication.translate("MainWindow", u"Sin Servicio", None))

        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Coordinaci\u00f3n:", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Proveedor:", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Observaciones:", None))
        self.SU_ADD.setText(QCoreApplication.translate("MainWindow", u"Agregar Registro", None))
        self.PagUtilidades.setText(QCoreApplication.translate("MainWindow", u"Utilidades", None))
        self.IPConfBtn.setText(QCoreApplication.translate("MainWindow", u" IPConfig ", None))
        self.PingBtn.setText(QCoreApplication.translate("MainWindow", u" Ping       ", None))
        self.TracerBtn.setText(QCoreApplication.translate("MainWindow", u"Tracert    ", None))
        self.ArpBtn.setText(QCoreApplication.translate("MainWindow", u"ARP         ", None))
        self.NSLookBtn.setText(QCoreApplication.translate("MainWindow", u"NSLookup", None))
        self.RouteBtn.setText(QCoreApplication.translate("MainWindow", u"Varios", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-weight:600;\">Utilidad IPCondig</span></p><p align=\"justify\">Muestra todos los valores de configuraci\u00f3n de red TCP/IP actuales y actualiza la configuraci\u00f3n del Protocolo de configuraci\u00f3n din\u00e1mica de host (DHCP) y del Sistema de nombres de dominio (DNS). </p></body></html>", None))
        self.Iconfig4.setText(QCoreApplication.translate("MainWindow", u"Ejecutar Registro", None))
        self.Iconfig6.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-weight:600;\">RegisterDNS</span>:Actualiza todas las concesiones DHCP y vuelve a registrar los nombres DNS</p></body></html>", None))
        self.ParamIp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresar parametros manualmente.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">FlushDNS: Vac\u00eda la memoria cache de resoluci\u00f3n DNS</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-weight:600;\">All:</span> Muestra la configuraci\u00f3n completa de TCP/IP para todos los adaptadores. </p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-weight:600;\">DisplayDNS: </span>Muestra el contenido de la cach\u00e9 de resoluci\u00f3n de cliente DNS.</p></body></html>", None))
        self.Iconfig2.setText(QCoreApplication.translate("MainWindow", u"Ejecutar Display DNS", None))
        self.Iconfig1.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.Iconfig3.setText(QCoreApplication.translate("MainWindow", u"Ejecutar Flush", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Ayuda: </span>Muestra las opciones del comando.</p></body></html>", None))
        self.Iconfig5.setText(QCoreApplication.translate("MainWindow", u"Ejecutar Ayuda", None))
        self.SalidaIPConf.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Salida del comando</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Utilidad Ping</span></p><p>ping es el <span style=\" font-weight:600;\">comando TCP/IP principal que se usa para solucionar problemas de conectividad, facilidad de acceso y resoluci\u00f3n de nombres</span></p><p><span style=\" font-weight:600;\">Ingresa la direcci\u00f3n IP, dominio o secuencia de IPs:</span><br/></p></body></html>", None))
        self.ping1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ejem. (192.168.0.1) o (192.168.0.1,192.168.0.3) o (192.168.0.0/24) o (google.com)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Paquetes", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"TimeOut (Segundos)", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o de los paquetes", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Intervalo de Tiempo", None))
        self.PingAyudaBtn.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.PingIniciarBtn.setText(QCoreApplication.translate("MainWindow", u"Iniciar / Detener", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-weight:600;\">Env\u00edo de Paquetes</span></p></body></html>", None))
        ___qtablewidgetitem7 = self.PINGOUT.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"No.", None));
        ___qtablewidgetitem8 = self.PINGOUT.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Destino", None));
        ___qtablewidgetitem9 = self.PINGOUT.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o Paquete", None));
        ___qtablewidgetitem10 = self.PINGOUT.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Tiempo", None));
        ___qtablewidgetitem11 = self.PINGOUT.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"TTL", None));
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-weight:600;\">Utilidad Trace Route</span></p><p align=\"justify\">Tracert o Trace Route es una utilidad de l\u00ednea de comandos que se usa para determinar la ruta que toma un paquete de protocolo de Internet (IP) para alcanzar su destino.</p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n IP o Dominio", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Numero de Saltos", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Time Out (Segundos)", None))
        self.tracert4.setText(QCoreApplication.translate("MainWindow", u"No convertir direcciones a nombre", None))
        self.tracert5.setText(QCoreApplication.translate("MainWindow", u"Seguir la ruta de retorno (Solo IPv6)", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Parametros Manuales", None))
        self.TracertAyudaBtn.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.TracertIniciarBtn.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-weight:600;\">Utilidad ARP</span></p><p align=\"justify\">Muestra y modifica las entradas en la cach\u00e9 del Protocolo de resoluci\u00f3n de direcciones (ARP). La cach\u00e9 ARP contiene una o varias tablas que se usan para almacenar direcciones IP y sus direcciones f\u00edsicas Ethernet o Token Ring resueltas. </p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Mostrar Tabla ARP", None))
        self.arp1.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Consultar MAC de IP", None))
        self.arp6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IPv4", None))
        self.arp2.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Borrar IP de la tabla", None))
        self.arp8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IPv4", None))
        self.arp7.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Agregar Mac Estatica", None))
        self.arp4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IPv4", None))
        self.arp3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MAC", None))
        self.arp5.setText(QCoreApplication.translate("MainWindow", u"Agregar MAC est\u00e1tica", None))
        self.ArpAyuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Utilidades Varias", None))
        self.var1.setText(QCoreApplication.translate("MainWindow", u"Direcciones MAC", None))
        self.var5.setText(QCoreApplication.translate("MainWindow", u"Administrador de red", None))
        self.var4.setText(QCoreApplication.translate("MainWindow", u"Fast.com", None))
        self.var2.setText(QCoreApplication.translate("MainWindow", u"Enviar Solictudes ARP", None))
        self.var6.setText(QCoreApplication.translate("MainWindow", u"Administrador de tareas", None))
        self.var3.setText(QCoreApplication.translate("MainWindow", u"SpeedTest", None))
        self.var7.setText(QCoreApplication.translate("MainWindow", u"Acceder a router", None))
        self.var8.setText(QCoreApplication.translate("MainWindow", u"CMD", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Utilidad NSLookup</span></p><p align=\"justify\">Muestra informaci\u00f3n que puede usar para diagnosticar la infraestructura del Sistema de nombres de dominio (DNS). </p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Dominio:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Agregar Parametros Manualmente.", None))
        self.NSLOAyudaBtn.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.NSLOIniciarBtn.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.label_109.setText("")
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Reporte General</span></p><p>Genera un documento excel con informaci\u00f3n general de toda la bas de datos.</p><p><br/></p></body></html>", None))
        self.GRG.setText(QCoreApplication.translate("MainWindow", u"Generar Documento", None))
        self.label_103.setText("")
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Listado de las CLUES con acceso a internet.</span></p><p>Generar un documento excel con todas las CLUES que cuentan con acceso a internet.</p></body></html>", None))
        self.GR3.setText(QCoreApplication.translate("MainWindow", u"Generar Documento", None))
        self.label_113.setText("")
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Generar listado del inventario.</span></p><p>Obtener documento excel con la informaci\u00f3n de los proveedores en la base de datos.</p></body></html>", None))
        self.GR7.setText(QCoreApplication.translate("MainWindow", u"Generar Documento", None))
        self.label_105.setText("")
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Generar Listado de los dispositivos en la red</span></p><p>Generar un documento excel con todos los dispositivos capturados en las diferentes redes monitoreadas.</p></body></html>", None))
        self.GR4.setText(QCoreApplication.translate("MainWindow", u"Generar Documento", None))
        self.label_111.setText("")
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Generar Listado de proveedores.</span></p><p>Obtener documento excel con la informaci\u00f3n de los proveedores en la base de datos.</p></body></html>", None))
        self.GR6.setText(QCoreApplication.translate("MainWindow", u"Generar Documento", None))
        self.label_42.setText("")
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Reporte Pruebas de velocidad</span></p><p>Generar un documento excel a apartir de la base de datos de cada una de las pruebas de velocidad realizadas.</p><p><br/></p></body></html>", None))
        self.GR1.setText(QCoreApplication.translate("MainWindow", u"Generar Documento", None))
        self.GRBorrarP.setText(QCoreApplication.translate("MainWindow", u"Borrar Registros", None))
        self.label_101.setText("")
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Listado de reportes de servicio</span></p><p>Generar un documento excel de cada uno de los reportes de problemas de servicio que se han creado con los proveedores.</p></body></html>", None))
        self.GR2.setText(QCoreApplication.translate("MainWindow", u"Generar Documento", None))
        self.GRBorrarS.setText(QCoreApplication.translate("MainWindow", u"Borrar Registros", None))
        self.label_107.setText("")
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Generar historial de conexiones</span></p><p>Genera un historial de las conexiones encontradas por dia, generando un listado de los dispositivos capturados y el numero total de estos.</p></body></html>", None))
        self.GR5.setText(QCoreApplication.translate("MainWindow", u"Generar Documento", None))
        self.GRBorrarH.setText(QCoreApplication.translate("MainWindow", u"Borrar Historial", None))
        self.label_122.setText("")
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Generar listado de problemas de la red</span></p><p>Permite generar un documento excel con los problemas corregidos y no corregidos que se registraron en el software.</p></body></html>", None))
        self.GR8.setText(QCoreApplication.translate("MainWindow", u"Generar Documento", None))
        self.GRBorrarPr.setText(QCoreApplication.translate("MainWindow", u"Borrar registros", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa Derecho", None))
#if QT_CONFIG(tooltip)
        self.DerechoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Cerrar Men\u00fa", None))
#endif // QT_CONFIG(tooltip)
        self.DerechoBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Notificaciones", None))
        self.BasuraNotif.setText("")
#if QT_CONFIG(tooltip)
        self.CerrarNotif.setToolTip(QCoreApplication.translate("MainWindow", u"Cerrar Notificacion", None))
#endif // QT_CONFIG(tooltip)
        self.CerrarNotif.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Con internet", None))
        self.label_7.setText("")
    # retranslateUi

