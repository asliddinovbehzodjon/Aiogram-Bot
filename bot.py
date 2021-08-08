from aiogram import Bot,Dispatcher,types,executor

btn=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
btn.add("Dollar-So'm","So'm-Dollar",'Rubl-Dollar','Dollar-Rubl',"So'm-Rubl","Rubl-So'm")
token=''
bot=Bot(token=token)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def first(message: types.Message):
    await bot.send_message(message.chat.id,'Salom',reply_markup=btn)
@dp.message_handler(content_types=['text'])
async def second(message: types.Message):
    text=message.text
    if text=="Dollar-So'm":
        inputs='USD'
        outputs='UZS'
    if text=="So'm-Dollar":
        outputs='USD'
        inputs='UZS'
    if text=="Dollar-Rubl":
        inputs='USD'
        outputs='RUB'
    if text=="Rubl-Dollar":
        outputs='USD'
        inputs='RUB'
    if text=="Rubl-So'm":
        inputs='RUB'
        outputs='UZS'
    if text=="So'm-Rubl":
        outputs='RUB'
        inputs='UZS'
    import requests
    import json
    url='https://v6.exchangerate-api.com/v6/{api key}/latest/'+inputs
    response=requests.get(url)
    rest=json.loads(response.text)
    result=str(rest['conversion_rates'][outputs])
    await bot.send_message(message.chat.id,result)
    





if __name__=='__main__':
    executor.start_polling(dp)