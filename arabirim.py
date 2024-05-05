import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QVBoxLayout, QWidget, QPushButton, QDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QProcess  # Correct import statement for QProcess
import subprocess


class ShadowLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setStyleSheet("QLabel { color: #fff; text-shadow: 2px 2px 4px #000; }")


class ImageProcessingDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Görüntü İşleme Uygulamaları")
        self.setGeometry(200, 200, 400, 300)  # Ölçüler ayarlanabilir
        self.setWindowIcon(QIcon('icon.png'))

        # Burada görüntü işleme uygulamalarının arayüzünü oluşturabilirsiniz


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dijital Görüntü İşleme Uygulaması")
        self.setGeometry(100, 100, 800, 600)

        # Sol üst köşedeki ikonu ayarla
        self.setWindowIcon(QIcon('icon.png'))

        self.create_menus()
        self.create_main_layout()

    def create_menus(self):
        self.home_menu = self.menuBar().addMenu("Anasayfa")

        exit_action = QAction("Çıkış", self)
        exit_action.triggered.connect(self.close)

        self.home_menu.addAction(exit_action)

        # Kullanım Kılavuzu menüsünü ekle
        usage_guide_action = QAction("Kullanım Kılavuzu", self)
        usage_guide_action.triggered.connect(self.show_usage_guide)
        self.menuBar().addAction(usage_guide_action)

    def create_main_layout(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Arka plan resmi
        pixmap = QPixmap("foto.jpg")
        photo_label = QLabel()
        photo_label.setPixmap(pixmap)
        main_layout.addWidget(photo_label)

        # Öğrenci bilgileri
        student_info_label = ShadowLabel("<h2 style='color: #000; text-align: center;'>Öğrenci Bilgileri</h2>"
                                         "<p style='color: #000; text-align: center;'>Adı Soyadı: <b>Mecit Mert BİŞGİN</b></p>"
                                         "<p style='color: #000; text-align: center;'>Öğrenci No: <b>221229067</b></p>")
        main_layout.addWidget(student_info_label)

        # Ana sayfa tasarımı
        header_label = ShadowLabel("<h1 style='color: #000; text-align: center;'>Dijital Görüntü İşleme Uygulaması</h1>")
        main_layout.addWidget(header_label)

        # Ödev Butonları
        self.create_assignment_buttons(main_layout)

    def create_assignment_buttons(self, layout):
        assignments = [
            {"title": "Ödev 1: Kontrants", "filename": "odev1.py", "details": "Bu ödevde istenilen ödev arabirimi oluşturuldu."},
            {"title": "Ödev 2A: Serit Tespit ", "filename": "odev2a.py",
             "details": "Bu ödevde Hought Donusumu ile gerekli tespitler yapilmistir ."},
            {"title": "Ödev 2B: Göz Tespit", "filename": "odev2.py", "details": "Ödev daha verilmedi."},
            {"title": "Ödev 3: Deblurring", "filename": "odev3.py", "details": "Ödev daha verilmedi."},
            {"title": "Ödev 4: Bolge tespit ve ozellik cikarma", "filename": "odev4.py", "details": "Ödev daha verilmedi."}
        ]

        for assignment in assignments:
            assignment_title = assignment["title"]
            assignment_filename = assignment["filename"]
            assignment_details = assignment["details"]

            button = QPushButton(assignment_title)
            button.setStyleSheet(
                "QPushButton { background-color: #4CAF50; color: white; border: 2px solid #4CAF50; border-radius: 8px; padding: 10px 20px; font-size: 16px; font-weight: bold; }"
                "QPushButton:hover { background-color: #45a049; border-color: #45a049; }"
            )
            button.clicked.connect(lambda _, filename=assignment_filename: self.run_python_script(filename))

            layout.addWidget(button)

    def run_python_script(self, filename):
        subprocess.Popen(["python", filename])  # Python komutunu ve dosya adını parametre olarak veriyoruz

    def show_usage_guide(self):
        usage_guide_dialog = QDialog(self)
        usage_guide_dialog.setWindowTitle("Kullanım Kılavuzu")

        guide_text = "Bu uygulama Dijital Görüntü İşleme dersi için geliştirilmiştir. \nMenülerden farklı ödevlere ulaşabilir ve detaylarını görebilirsiniz. "

        guide_label = QLabel(guide_text)
        layout = QVBoxLayout()
        layout.addWidget(guide_label)

        usage_guide_dialog.setLayout(layout)
        usage_guide_dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
