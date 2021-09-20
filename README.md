# NESTED FOAM

GUI Application - Encrypt and Decrypt Data

---

### GUI

Framework = **PySide - Qt**

UI Create = **Designer**   *Generate to Python Code*

Version = **6**

### Backend & Core

Language = **Python**

Version = **3.9.5** 

### Cryptography

Package = **nested_cipher**

Version = **0.3**

---

### RUN

After Install requirements

```bash
$ python3 main.py
```

If Import Issue Try this:

1. Create **virtual environments**

   ```bash
   $ python3 -m venv ./nested_foam/venv
   ```

2. Activate **virtual environments**

3. Install **requirements** to virtual environments

4. Run With This Command in Bash

   ```bash
   $ ./nested_foam/venv/bin/python.exe main.py
   ```

   or in shell *windows*

   ```shell
   $ ./nested_foam/venv/script/python.exe main.py
   ```

   

---

### Application

> **Menu :**
>
> > **Raw Input :** Use For **Encrypt** Or **Decrypt** Your Raw Text . 
> >
> > **File Input :** Use For **Encrypt** Or **Decrypt** Your File . *type support = text, binary*
> >
> > **Key Maker :** Use For **Generate Key** This is A Simple Key Generator .
>
> **Raw Input & File Input :**
>
> > **Support Encrypt or Decrypt Data**
> >
> > For **Encrypt** or **Decrypt** Must be Use Key If Want Only **Cipher (encode, decode)** Data Put Empty Key Input .
> >
> > For File **Encoding** and **Decoding** U must Chose Source File Type . *example: for **Any file** except **text file** encode or decode must set **file type** to **binary**. You Can Text File Type Set Binary if You need*
>
> **Key Maker :**
>
> > **Support Starts & Ends Pattern**
> >
> > You Can Put Your Pattern For **Starts With** & **Ends With** Key .
> >
> > **Support Special Character :**
> >
> > > **\d :** Digit . *0-9*
> > >
> > > **\A :** Upper Alphabet . *A-Z*
> > >
> > > **\a :** Lower Alphabet . *a-z*
> > >
> > > **\s :** Symbols
> > >
> > > If use Special Char Must Scape With **one Space**
> >
> > **Example:**
> >
> > > **No Special Char**
> > >
> > > > Starts With : **xx0K**   -   Ends With : **6END%**
> > > >
> > > > results : **xx0K ... 6END%**
> > >
> > > **Special Char**
> > >
> > > > Starts With : **\d B \s**   -   Ends With : **F \A \A \D**
> > > >
> > > > results : **5B? ... FWC7**

---

### Screen Shot

![01](https://github.com/Class-Tooraj/nested_foam/blob/main/screenshot/01.jpg)

![02](https://github.com/Class-Tooraj/nested_foam/blob/main/screenshot/02.jpg)

![03](https://github.com/Class-Tooraj/nested_foam/blob/main/screenshot/03.jpg)

![04](https://github.com/Class-Tooraj/nested_foam/blob/main/screenshot/04.jpg)

![05](https://github.com/Class-Tooraj/nested_foam/blob/main/screenshot/05.jpg)

![06](https://github.com/Class-Tooraj/nested_foam/blob/main/screenshot/06.jpg)

![07](https://github.com/Class-Tooraj/nested_foam/blob/main/screenshot/07.jpg)

![08](https://github.com/Class-Tooraj/nested_foam/blob/main/screenshot/08.jpg)

![09](https://github.com/Class-Tooraj/nested_foam/blob/main/screenshot/09.jpg)

---

author : **ToorajJahangiri**

email : **toorajjahangiri@gmail.com**
