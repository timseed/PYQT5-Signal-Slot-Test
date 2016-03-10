#PYQT5 Gui

I have never had the requirement to develop a Gui in Python, and after having a look at some of the available frameworks - I have come back to Qt. This was rather a surprise to me also !! But none of the other frameworks I tried had the signal/slot (callbacks if you like) that Qt provided.

#Getting going in PyQt

The most difficult issue is to try and get Qt compiled and installed - I did this initially on a Mac (using PyVenv) and it was very painless - the general steps are as follows..

virtualenv -p /usr/local/bin/python3.4 pyqt

* install xcode
* install the Command Line Tools (open Xcode > Preferences > Downloads)
* install Qt libraries (qt-opensource-mac-x64-clang-5.2.1.dmg)
* install python 3.4
* create a virtual env (i.e. ~/.env/ariane_mail)
* unzip and compile SIP and PyQt

#Commands

```bash
cd /var/tmp
cp ~/Downloads/PyQt-gpl-5.5.1.tar.gz .
cp ~/Downloads/sip-4.17.tar.gz .
tar xvf PyQt-gpl-5.5.1.tar.gz
tar xvf sip-4.17.tar.gz
cd sip-4.17
python3 configure.py -d ~/pyqt/lib/python3.4/site-packages --arch x86_64
source ~/pyqt/bin/activate
make
make install
cd ..
```

**vi /Users/tim/Qt5.2.1/5.2.1/clang_64/mkspecs/qdevice.pri**
And make file look like

```text

    !host_build:QMAKE_MAC_SDK = macosx
    GCC_MACHINE_DUMP = x86_64-apple-darwin12.5.0
```
And now Build QT

```bash
cd PyQt-5.5.1
python3 configure.py --destdir ~/pyqt/lib/python3.4/site-packages --qmake ~/Qt5.2.1/5.2.1/clang_64/bin/qmake
make
make install 
```

#Test it all worked

```bash
~/.env/ariane_mail/bin/python -c "import PyQt5"
```


#PyQt Running - now what !!

Well the first thing to get going is the designer interface - I cheated and cleated an Alias something along the lines of...

```bash
alias design='~/Qt5.2.1/5.2.1/clang_64/bin/Designer.app/Contents/MacOS/Designer'
```

Do a simple gui and save the output.

##Convert ui to Python code

This is super easy - and the following commands should do this for you

```bash
uic5 -x <Source>.ui > <Source>.py 
```

Note **-x** will add a basic QtApplication so you can just run the code.

When you are happy with this - then you should be able to look at the example I have provided.

#My Example

Before I went any further with some development tasks, I wanted to make sure that I could do the following

* Link a Button (or QT Object) to some custom method
* Create a detached process - that could do something
* Create a custom **signal** - and attach it to a custom **slot**

What I have not yet tried is

* Sending signals from/to differenc classes
* cleanly stopping detached processes


