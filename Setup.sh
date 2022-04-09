#!/bin/bash
echo "Compiling the User Interface files..."
pyside-uic -d -o ./userInterface/XRDPConfiguratorMainWindow.py ./userInterface/XRDPConfiguratorMainWindow.ui
pyside-uic -d -o ./userInterface/SessionFrame.py ./userInterface/SessionFrame.ui
pyside-uic -d -o ./userInterface/PreviewWindow.py ./userInterface/PreviewWindow.ui
pyside-uic -d -o ./userInterface/NewSession.py ./userInterface/NewSession.ui
pyside-uic -d -o ./userInterface/About.py ./userInterface/About.ui
pyside-uic -d -o ./userInterface/AreYouSure.py ./userInterface/AreYouSure.ui
pyside-uic -d -o ./userInterface/InfoWindow.py ./userInterface/InfoWindow.ui
pyside-uic -d -o ./userInterface/LogoCustomization.py ./userInterface/LogoCustomization.ui
pyside-uic -d -o ./userInterface/dialogSize.py ./userInterface/dialogSize.ui
pyside-uic -d -o ./userInterface/logoPosition.py ./userInterface/logoPosition.ui
pyside-uic -d -o ./userInterface/labelsAndBoxes.py ./userInterface/labelsAndBoxes.ui
pyside-uic -d -o ./userInterface/LoginWindowSimulator.py ./userInterface/LoginWindowSimulator.ui
pyside-uic -d -o ./userInterface/DialogButtons.py ./userInterface/DialogButtons.ui
pyside-uic -d -o ./userInterface/ImageImport.py ./userInterface/ImageImport.ui
pyside-rcc --compress 9 XRDPConfigurator_resources.qrc -o XRDPConfigurator_resources_rc.py
echo "Building the libxrdpconfigurator.so helper library..."
cd libxrdpconfigurator
./buildlib.sh
cd ..
echo "All done. Run ./XRDPConfigurator.sh to start the application."
