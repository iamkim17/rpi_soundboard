VERSION=0.1
TARGET=tkinter_mvc_template_v$(VERSION)

all: zip
	
zip: $(TARGET).zip

$(TARGET).zip: *.py images/* requirements.txt run.sh 
	python3 -m pip install -r requirements.txt
	python3 -m pip install pyinstaller
	python3 -m PyInstaller --noconfirm tkinter_mvc_template.spec
	cp -r dist $(TARGET) 
	cp run.sh $(TARGET) 
	zip -r $(TARGET).zip $(TARGET) 
	rm -rf $(TARGET) 

.PHONY clean:
	-rm -rf build
	-rm -rf dist
	-rm -rf __pycache__
	-rm $(TARGET) 
	-rm $(TARGET).zip
