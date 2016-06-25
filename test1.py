# coding=utf-8

# sudo pip install pyTelegramBotAPI --upgrade

import telebot
import random

bot = telebot.TeleBot("226208715:AAGfFKQ0R3X5O9n4SAQog8gQqWpnj4lwULE")
otherPeopleSaid = [
        u"勤奮是你生命的密碼，能譯出你一部壯麗的史詩。",
        u"讓我們將事前的憂慮，換為事前的思考和計劃吧！",
        u"人生多一份挫折，就多一份人生的感悟；人生多一次跌打，就多一條抗爭的經驗。",
        u"人生偉業的建立，不在能知，乃在能行。",
        u"任何的限制，都是從自己的內心開始的。",
        u"善於與人溝通，適度採納別人意見。",
        u"如果懼怕前面跌宕的山岩，生命就永遠只能是死水一潭。",
        u"生活不會否定任何人，就怕自己否定生活。",
        u"忙於採集的蜜蜂，無暇在人前高談闊論。",
        u"你追我趕拼搏爭先，流血流汗不留遺憾。",
        u"停止拜訪就是停止呼吸，停止增員就是消滅生機。",
        u"老虎不發威他就一隻病貓！發威了他就是王者！所以人人都可以是王者但同時也可能是病貓，關鍵在於你自己的選折！",
        u"生存是人類第一要務，而快樂卻是生存的唯一原則。快樂是一個人心靈和精神所表現出來的滿足，是最最純潔和高尚的享受。",
        u"失敗是什麼？沒有什麼，只是更走近成功一步；成功是什麼？就是走過了所有通向失敗的路，只剩下一條路，那就是成功的路。",
        u"既然人生的幕布已經拉開，就一定要積極的演出；既然腳步已經跨出，風雨坎坷也不能退步；既然我已把希望播在這裡，就一定要堅持到勝利的謝幕……",
        u"你的心應該保持這種模樣，略帶發力的緊張，不鬆懈，對待不定有坦然。損傷是承載，沉默是擴展。終結是新的開始。如此，我會為你的心產生敬意。\
          風帆，不掛在桅杆上，是一塊無用的布；桅杆，不掛上風帆，是一根平常的柱；理想，不付諸行動是虛無縹緲的霧；行動，而沒有理想，是徒走沒有盡頭的路。",
        u"生命中，好多的事是這樣，生活中，好多的情是這樣，沒有理由，也無需理由，愛就是愛，喜歡就是喜歡，沒有結果，也無須結果，心甘情願，無怨無悔。",
        u"我們的生命，就是以不斷出發的姿勢得到重生。為某些只有自己才能感知的來自內心的召喚，走在路上無法停息。",
        u"人生的快樂在於自己對生活的態度，快樂是自己的事情，只要願意，你可以隨時調換手中的遙控器，將心靈的視窗調整到快樂頻道。學會快樂，即使難過，也要微笑著面對。",
        u"我未曾見過一個早起、勤奮、謹慎、誠實的人抱怨命運不好；良好的品格，優良的習慣，堅強的意志，是不會被假設所謂的命運擊敗的。",
        u"如果有一天，你偶然看到了這些文字，我希望這幾分鐘是真正屬於你自己的，在這裡你給自己加油，打氣，繼續去完成你曾經的夢想，勇敢的去挑戰自己，歷練自己！",
        u"漫漫長路，你願一人獨撐，忍受著孤獨與寂寞，承受著體力與精神的壓迫，只任汗水溶於淚水，可腳步卻從不停歇。好樣的，縱然得不了桂冠，可堅持的你，定會贏得最後的掌聲。",
        u"生活一直都是美好的，雖然有辛苦的奔波，有人情的淡漠，也有偶爾的碰壁和受挫，有許許多多的痛和不幸，然而，這些都不能掩飾了生活的美好，生活中總有許多值得我們追求和嚮往的東西。",
        u"生活中，我們每天都在嘗試嘗試中，我們走向成功品味失敗，走過心靈的陰雨晴空運動員們，不要放棄嘗試無論失敗與否重要的是你勇於參與的精神，付出的背後是勝利無論是否成功，我們永遠讚美你，你們永遠是我們的驕傲。"
    ]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "hello world!")

@bot.message_handler(commands=['ls'])
def send_welcome(message):
    for i in range(24):
        bot.reply_to(message, u"偉人的話：" + otherPeopleSaid[i])
    
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    template1 = u"我覺得心情不好"
    template2 = u"說不定我沒辦法"
    encourage = [ 
     [u"我覺得心情不好", u"加油！明天會比今天更精彩哈哈~"],
     [u"說不定我沒辦法", u"我相信你可以的！！！！"],
     [u"QQ", u"別哭~我跟你站在同一邊~"]
    ]
    exist = False
    for each in encourage:
        if message.text in each:
            bot.reply_to(message, each[1])
            exist = True
            
            # Random to send other people's sentence
            wouldSend = random.randint(0, 24)
            if wouldSend == 0:
                print wouldSend
                bot.reply_to(message, u"送你一句帶有正能量的話哈哈~~~\n" + otherPeopleSaid[random.randint(0, 10)])
                bot.reply_to
    if not exist:
        bot.reply_to(message, "You tell me: " + message.text)
    else:
        exist = False
    bot.send_sticker
            
bot.polling()