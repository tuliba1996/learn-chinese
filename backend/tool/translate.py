from googletrans import Translator

translator = Translator()

a = translator.translate('下', dest='vi', src='zh-cn')
print('sdf', translator.__dict__)
print('pro', translator.token_acquirer.__dict__)
print('a', a.extra_data)
