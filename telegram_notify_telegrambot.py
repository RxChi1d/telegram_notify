import telegram
import asyncio
import time

def send_msg(text: str):
    bot_token = 'your bot token'
    chat_id = 0000000000 # your chat id

    async def send_message():
        bot = telegram.Bot(bot_token)
        async with bot:
            await bot.send_message(text=text, chat_id=chat_id)
    asyncio.run(send_message())
    

def timer(func, model, dataset, scene, stage):
    def format_time_cost(time_cost):
        days = time_cost // (24 * 3600)
        time_cost %= (24 * 3600)
        
        # 將剩餘的秒數轉換為時、分、秒格式
        time_str = time.strftime("%H:%M:%S", time.gmtime(time_cost))
        
        if days > 0:
            return f"{int(days)}, {time_str}"
        else:
            return time_str

    def wrapper(*args, **kwargs):
        send_msg(
            f'[{model}][{dataset}][{scene}] {stage} Start')

        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()

        format_time = format_time_cost(end - start)
        
        metrics = ''
        for key in output:
            metrics += f'{key}: {output[key]}\n'
            
        send_msg(
            f'[{model}][{dataset}][{scene}] {stage} Complete in {format_time}\n{metrics}')

        return format_time, output

    return wrapper