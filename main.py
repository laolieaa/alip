import google.generativeai as genai
import telebot
import datetime
x = (" عمليّة طُوفان الأقصى، وفي إسرائيل عمليّة السُّيُوف الحديديَّة، كما تُشير إليها بعض المصادر بالانتفاضة الثالثة، أو الحرب الفلسطينية الإسرائيلية ويشار إليها بشكل غير رسمي باسم معركة السابع من أكتوبر، هي عمليةٌ عسكرية مُمتدة شنَّتها فصائلُ المقاومة الفلسطينية في قطاع غزة وعَلى رأسِها حركة حماس عَبر ذراعها العسكري كتائب الشهيد عز الدّين القسام في أوّل ساعات الصباح من يوم السبت (7 تشرين الأول/أكتوبر 2023 م) الموافق لـ (22 ربيع الأوَّل 1445 هـ)، إذ أعلَن القائِد العام للكتائب مُحمَّد الضيف، بدء العملية ردًّا على «الانتهاكات الإسرائيلية في باحات المَسْجِدِ الأقصى المُبَارك واعتداء المُستوطنين الإسرائيليين على المُواطنين الفلسطينيين في القُدس والضّفّة والدّاخل المُحتَل». بدأت عمليَّة طُوفَان الأقصى عبر هُجومٍ صَاروخي وَاسعِ النطاق شنّته فصائل المقاومة، إذ وجَّهت آلاف الصواريخ صوبَ مختلف المستوطنات الإسرائيليّة من ديمونا في الجنوب إلى هود هشارون في الشمال والقدس في الشرق، وتزامنَ مع إطلاق هذه الصواريخ اقتحام برّي من المُقاومين عبر السّيارات رُباعيّة الدّفع والدّراجات النّارية والطّائرات الشّراعيّة وغيرها للبلدات المتاخمة للقطاع، والتي تُعرف باسم غلاف غزة، حيث سيطروا على عددٍ من المواقع العسكريّة خاصة في سديروت، ووصلوا أوفاكيم، واقتحموا نتيفوت، وخاضوا اشتباكاتٍ عنيفة في المستوطنات الثلاثة وفي مستوطنات أخرى كما أسروا عددًا من الجنود واقتادوهم لغَزَّة فضلًا عن اغتنامِ مجموعةٍ من الآليّات العسكريّة الإسرائيليَّة.في 9 أكتوبر، أعلن جيش الاحتلال الإسرائيلي استعادته السيطرة على جميع البلدات الّتي استولت عليها فصائل المُقاومة الفلسطينيَّة في غِلاف قطاع غزّة مع استمرار بعض المناوشات المُتفرقة، وأعلن وزير الدفاع الإسرائيلي يوآف غالانت بدء ما أسمَاه حصاراً شاملاً على غزة، بما في ذلك حظر دخول الغذاء والوقود. ")
# Set up Google Generative AI
genai.configure(api_key="AIzaSyBtv6W1BL7GrcQD14P07nKdG50vHucNouU")

# Define the model generation configuration
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

# Define the safety settings for the model
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

# Create the Generative Model instance
model = genai.GenerativeModel(model_name="gemini-pro",
               generation_config=generation_config,
               safety_settings=safety_settings)

# Set up Telegram bot
token = "7021936945:AAG9q9TNK4ccE22PPkLPEddXdCdOADpSaSE"
bot = telebot.TeleBot(token)

# Handle messages from users
@bot.message_handler(func=lambda message: True)
def echo_message(message):
  # Extract the user's message
  user_message = message.text

  # Send a preliminary response
  message_id = bot.send_message(message.chat.id, "جاري الرد...").message_id

  # Construct the prompt for the model
  prompt_parts = [user_message]

  try:
    # Generate a response using the model
    response = model.generate_content(prompt_parts)

    # Add information about the bot creator
    if "من صنعك" in user_message or "من هو صاحبك" in user_message or "من أنشأك" in user_message  or "من مطورك " in user_message  or "من مبرمج البوت " in user_message  or "من مبرمجك " in user_message  or "من مطور البوت " in user_message:
      bot.send_message(message.chat.id, "أنا نموذج لغوي كبير تم صناعتي من قبل المطور بلاك وصديقه انوبيس")

    # Add information about the engineer
    elif" من هو بلاك" in user_message or "من هو المطور بلاك" in user_message  or "بلاك   " in user_message:
      bot.send_message(message.chat.id, "المطور بلاك هوا مطور بوتات كثيره مثل بوتات اختراق وبوتات chatgptوهو الذي صنعني وهو مطوري وهذا هو معرفه تيليجرام @M_1_1K.")

    # Add local time and date in Riyadh/Saudi Arabia timezone
    elif "الوقت" in user_message or "التاريخ" in user_message:
      now = datetime.datetime.now()
      time = now.strftime("%H:%M")
      date = now.strftime("%Y-%m-%d")
      bot.send_message(message.chat.id, f"الوقت المحلي: {time} بتوقيت الرياض / السعودية\nالتاريخ المحلي: {date}")

    # Add information about Palestine
    elif "فلسطين" in user_message:
      bot.send_message(message.chat.id, "فلسطين هي دولة عربية حرة، وعاصمتها القدس.")

    elif "طوفان الأقصى" in user_message:
        bot.send_message(message.chat.id, x)

    # Add information about Israel
    elif "إسرائيل" in user_message  or "اسرائيل " in user_message:
      bot.send_message(message.chat.id, "إسرائيل هي مجرد احتلال صهيوني أمريكي.")

    else:
      # Generate a response using the model
      response = model.generate_content(prompt_parts)
      # Send the response back to the user
      bot.send_message(message.chat.id, response.text)

    # Delete the preliminary response
    bot.delete_message(message.chat.id, message_id)

  except Exception:
    # Handle the exception and send an error message to the user
    bot.send_message(message.chat.id, "عذراً، لا يمكنني الإجابة على سؤالك.")
    bot.delete_message(message.chat.id, message_id)

# Start the bot
bot.polling()