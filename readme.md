# Adobe "Popup" Killer

--

This script is not a patch or cracker. It just a simple Python script with no dependencies that will kill any app or process defined as the target in the script.

I am not a profesional who used Adobe product for commercial. I am just an ordinary user.

I have no intetion for developing the script.

Anyway, if you are an professional who use the Adobe products quite often and love adobe feature. I suggest you to purchase the license instead.

### How to run it

1. If you don't have Python installed go to [python.org](https://python.org/downloads). I'm using `Python 3.10.13` on my machine.
2. Clone this repo

```bash
git clone https://github.com/ekkyarmandi/adobe-popup-killer.git popupkiller

```

3. Change your directory to `popupkiller`

```bash
cd popupkiller

```

4. Run the script

```bash
python3 main.py --debug
```

### Edit target

If you want to midify the target you want to kill. Go to [main.py](/main.py) and find `target` variable. If you are on Linux or Unix you can check the current running process you want to kill using command below

```bash
# show all process services
$ ps aux

# filter the processes using `grep`
$ ps aux | grep <keyword>
```
