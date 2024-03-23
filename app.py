#Transformando texto em aúdio 
#Importar bibliotecas

from gtts import gTTS
from playsound import playsound

audio = "Café da Manhã.mp3"
language = "pt-br"

sp = gTTS (
    text='Tudo e toda pessoa contém os dois elementos, masculino e feminino. Este princípio não tem relação com incentivos à luxúria ou à libertinagem. Nem se refere a homens e mulheres propriamente. Sua afirmação se aproxima muito mais de exemplos como o da energia e seus polos “ negativo “ e “ positivo “, mas sem o tom pejorativo dado a essas duas palavras. Se refere a ânima, o intangível, como masculino e a matéria, o tangível, como feminino. Mas esse mesmo conceito se torna mais complexo quando aplicado a mente. Nela, o masculino seria tudo quanto vivenciamos conscientemente, cabendo ao subconsciente ou inconsciente o papel feminino. Porém o livro não os aborda, essa é uma interpretação psicológica.',
    lang=language
)

sp.save(audio)
playsound(audio)



