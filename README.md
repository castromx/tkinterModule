Створив свій калькулятор на бібліотеці tkinter.
Щоб не хардкодити створив ф-ю, яка буде створювати кнопки, таким чином забрав повторяючий код:
![bandicam 2023-07-02 13-47-51-000](https://github.com/castromx/tkinterModule/assets/96194271/6b299b5c-ec29-4226-886b-094dd1751e2a)
![bandicam 2023-07-02 13-48-03-367](https://github.com/castromx/tkinterModule/assets/96194271/17170e8e-8923-4dfc-a4ac-09034250a569)
Додав можливість вводу тексту з клавіатури, за допомогою обробника подій bind():
![bandicam 2023-07-02 13-48-51-066](https://github.com/castromx/tkinterModule/assets/96194271/b277db30-aed2-46ea-a28b-ab07455ec1d5)
![bandicam 2023-07-02 13-50-24-706](https://github.com/castromx/tkinterModule/assets/96194271/03304196-a975-436f-8ea3-6bb919bb59ef)
При вводі виразів, попередні операції між числами будуть виконуватись при додаванні спец. символа операції (функція calculate):
![bandicam 2023-07-02 13-38-18-193](https://github.com/castromx/tkinterModule/assets/96194271/0e197bd8-7de4-47cd-9474-f0b0214e68cf)
Та додав обробника помилок за допомогою пакету messagebox:
![bandicam 2023-07-02 12-25-14-547](https://github.com/castromx/tkinterModule/assets/96194271/56182209-72a2-4046-9366-b0bdcaf3aeac)
