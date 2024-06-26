# Инструкция для автоматизированного тестирования счетчиков

   В репозитории содержатся файлы:
   -  test.py - автоматизированный тест для 3х счетчиков
   -  TESTCASE.md - тест кейсы с проверками
   -  BUGS.md - баг-репорты
   -  GREY-AREAS.md - основные серые зоны, которые возникли при тестировании счетчиков
   -  TASK1.md - первое задание проекта

   ## Требования перед началом  
   1. Установите Python версии 3.x.
   2. Склонируйте репозиторий с тестами с помощью команды 'git clone https://github.com/IKrysanov/Avito.git'
   3. Создать виртуальное окружение 'python -m venv venv'
   4. Включить виртуальное окружение 'source venv/Script/activate'
   5. Установить все библиотеки командой 'pip install -r requirements.txt'

   ## Структура репозитория 
   -  test.py: автоматизированный тест для счетчика CO2, для сохраненного объема воды, для сэкономленной электроэнергии  
   -  output: каталог для сохранения скриншотов счетчиков(test.py)

   ## Запуск тестов  
   1. Откройте терминал
   2. Перейдите в каталог с репозиторием, используя команду 'cd'  
   3. Запустите тест, выполнив соответсвующий python файл:  
      - 'python test.py' :  для запуска теста для счетчиков 

   ## Ожидаемый результат  
   Тест должен запуститься и сделать скриншот, который появится в папке output 