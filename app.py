import streamlit as st

st.title("Playlist 🎶")
st.sidebar.title("Ache a opção perfeita")
st.sidebar.image('logo.png')





musicas = {
    "Bruno Mars": {
        "Locked Out Of Heaven": "https://www.youtube.com/watch?v=e-fA-gBCkj0",
        "Just The Way You Are": "https://www.youtube.com/watch?v=LjhCEhWiKXk",
        "That's What I Like": "https://www.youtube.com/watch?v=PMivT7MJ41M"
    },

    "Poze do Rodo": {
        "Famoso Imã": "https://www.youtube.com/watch?v=IOy0HNhEZNI",
        "Vida Louca": "https://www.youtube.com/watch?v=EXEMPLO1",
        "Me Sinto Abençoado": "https://www.youtube.com/watch?v=EXEMPLO2"
    },

    "Vários Artistas": {
        "Set DJ GM 6.0": "https://www.youtube.com/watch?v=Lu_-odNj5iU",
        "Set DJ GM 5.0": "https://www.youtube.com/watch?v=OcVY_NywmzY&list=RDOcVY_NywmzY&start_radio=1",
        "Set DJ GM 4.0": "https://www.youtube.com/watch?v=Gwtt6yklGac&list=RDGwtt6yklGac&start_radio=1"
    },

    "Japa NK": {
    "Posso Até Não Te Dar Flores": "https://www.youtube.com/watch?v=fXQj5TarYkc&list=RDfXQj5TarYkc&start_radio=1",
    "Nosso lancee É Low Profile": "https://www.youtube.com/watch?v=gJ5uJ5LiNO4&list=RDgJ5uJ5LiNO4&start_radio=1",
    "Carnívoro": "https://www.youtube.com/watch?v=hToGSAFPwds&list=RDhToGSAFPwds&start_radio=1"
}
}


artista = st.sidebar.selectbox("Escolha o artista que deseja ver as músicas", musicas.keys())
musica_artista = musicas[artista]
st.title(artista)

video, sobre = st.tabs(['video','sobre'])

with video:
    for musica in musica_artista.items():
        titulo, link = musica
        st.subheader(titulo)
        st.video(link)
with sobre:
    if artista == "Bruno Mars":
        st.title("🎤 Bruno Mars")

        st.image('bruno.png')

        st.markdown("""
        ## 🌎 Quem é Bruno Mars?

        Bruno Mars é o nome artístico de **Peter Gene Hernandez**, cantor,
        compositor, produtor musical e multi-instrumentista norte-americano.
        Ele nasceu em **8 de outubro de 1985**, na cidade de **Honolulu**,
        no estado do **Havaí (EUA)**.

        Desde muito jovem, Bruno esteve cercado pela música. Sua família era
        formada por músicos e artistas que se apresentavam em shows locais,
        o que permitiu que ele desenvolvesse suas habilidades ainda na infância.

        ---

        ## 👶 Infância e Origem

        Crescendo no Havaí, Bruno teve contato com diversos estilos musicais,
        incluindo rock, reggae, R&B, soul e música havaiana. Ainda criança,
        participava dos shows da família e ficou conhecido por suas imitações
        de Elvis Presley.

        O apelido "Bruno" surgiu quando ele era pequeno. Seu pai acreditava
        que ele se parecia com o famoso lutador Bruno Sammartino e passou a
        chamá-lo dessa forma.

        ---

        ## 🚀 Início da Carreira

        Após concluir os estudos, Bruno mudou-se para Los Angeles em busca de
        oportunidades na indústria musical. O início não foi fácil: durante
        vários anos trabalhou principalmente como compositor e produtor para
        outros artistas.

        Antes de alcançar a fama mundial como cantor, ajudou a escrever músicas
        para diversos nomes importantes da música internacional, adquirindo
        experiência e reconhecimento nos bastidores.

        ---

        ## 🌟 Ascensão ao Sucesso

        Sua carreira ganhou projeção internacional no início da década de 2010.
        Com seu estilo versátil e sua presença de palco marcante, rapidamente
        conquistou fãs em todo o mundo.

        Bruno se destacou por unir elementos modernos do pop com influências
        clássicas do funk, soul e R&B, criando uma identidade própria que o
        tornou um dos artistas mais populares de sua geração.

        ---

        ## 🎭 Estilo Artístico

        Uma das características mais admiradas de Bruno Mars é sua capacidade
        de atuar em diversas áreas da música. Além de cantar, ele também toca
        instrumentos, participa da composição de suas obras e colabora na
        produção musical.

        Seus shows são conhecidos pela energia, coreografias bem elaboradas e
        pela interação constante com o público.

        ---

        ## 🏆 Reconhecimento Mundial

        Ao longo da carreira, Bruno Mars acumulou diversos prêmios e recordes,
        tornando-se um dos artistas mais bem-sucedidos do século XXI.

        Entre seus feitos estão:
        - Múltiplos prêmios Grammy.
        - Bilhões de reproduções em plataformas digitais.
        - Turnês internacionais com grande público.
        - Reconhecimento por suas performances ao vivo.
        - Influência em diferentes gerações de artistas.

        ---

        ## 🎸 Curiosidades

        - Seu nome verdadeiro é Peter Gene Hernandez.
        - Nasceu e cresceu no Havaí.
        - Aprendeu música observando os artistas de sua família.
        - É multi-instrumentista e toca diversos instrumentos.
        - Foi compositor de sucesso antes de se tornar uma estrela mundial.
        - É conhecido por sua forte influência do funk e soul dos anos 70 e 80.

        ---

        ## 📖 Legado

        Bruno Mars é considerado um dos artistas mais influentes da música
        contemporânea. Sua capacidade de unir estilos musicais, realizar
        apresentações memoráveis e manter uma carreira consistente o transformou
        em uma referência para milhões de fãs ao redor do mundo.

        Sua trajetória demonstra como talento, dedicação e paixão pela música
        podem transformar um jovem do Havaí em um dos maiores nomes do cenário
        musical internacional.
        """)
    elif artista == "Poze do Rodo":
        with sobre:
            st.title("🎤 MC Poze do Rodo")
            st.image("poze.png")

            st.markdown("""
            ## 🌎 Quem é MC Poze do Rodo?

            MC Poze do Rodo é o nome artístico de **Marlon Brandon Coelho Couto Silva**,
            cantor e compositor brasileiro nascido no Rio de Janeiro. Ele se tornou
            um dos principais nomes do funk carioca na década de 2020, conquistando
            milhões de ouvintes em todo o Brasil.

            Conhecido por suas letras que retratam a realidade das comunidades,
            experiências pessoais e histórias de superação, Poze construiu uma
            trajetória marcada pela autenticidade e forte conexão com seu público.

            ---

            ## 👶 Infância e Origem

            Poze nasceu e cresceu no estado do Rio de Janeiro, em um ambiente
            de muitas dificuldades financeiras. Desde cedo, viveu de perto a
            realidade das comunidades cariocas, contexto que mais tarde influenciaria
            grande parte de suas composições.

            Sua vivência nas periferias brasileiras ajudou a moldar sua identidade
            artística e a forma como se comunica com os fãs.

            ---

            ## 🚀 Início da Carreira

            Antes de alcançar fama nacional, MC Poze já participava da cena do
            funk carioca e buscava espaço em bailes e produções independentes.

            Nos primeiros anos de carreira, utilizou as redes sociais e plataformas
            digitais para divulgar seu trabalho, construindo gradualmente uma base
            de fãs fiel e engajada.

            Sua persistência e identificação com o público jovem foram fundamentais
            para seu crescimento artístico.

            ---

            ## 🌟 Ascensão ao Sucesso

            O reconhecimento nacional veio quando suas músicas começaram a alcançar
            milhões de reproduções nas plataformas digitais.

            Seu estilo direto e suas letras inspiradas em vivências reais chamaram
            a atenção do público, tornando-o uma das vozes mais populares do funk
            contemporâneo.

            Com o passar dos anos, Poze passou a se apresentar em grandes eventos,
            festivais e casas de espetáculo por todo o país.

            ---

            ## 🎭 Características Artísticas

            Uma das principais marcas de MC Poze do Rodo é a forma intensa e
            emocional com que transmite suas histórias.

            Suas músicas costumam abordar temas como:

            - Superação de dificuldades.
            - Família e amizades.
            - Conquistas pessoais.
            - Realidade das comunidades.
            - Sonhos e ambições.

            Essa identificação com experiências vividas por muitos brasileiros
            contribuiu para sua enorme popularidade.

            ---

            ## 📱 Presença nas Redes Sociais

            Além da música, Poze também se tornou uma personalidade muito presente
            nas redes sociais.

            Seus seguidores acompanham de perto momentos da carreira, rotina,
            família e bastidores dos shows, fortalecendo ainda mais sua relação
            com o público.

            ---

            ## 🏆 Reconhecimento

            Ao longo de sua trajetória, MC Poze do Rodo conquistou:

            - Milhões de ouvintes nas plataformas de streaming.
            - Grande presença nas redes sociais.
            - Shows em diversas regiões do Brasil.
            - Reconhecimento como um dos principais artistas do funk carioca moderno.

            Seu crescimento ajudou a ampliar ainda mais a visibilidade do funk
            nacional para diferentes públicos.

            ---

            ## 💡 Curiosidades

            - Seu nome artístico faz referência ao bairro onde cresceu.
            - Tornou-se conhecido inicialmente através da internet e dos bailes funk.
            - É reconhecido pela forte conexão com seus fãs.
            - Compartilha frequentemente aspectos de sua vida pessoal nas redes sociais.
            - É uma das figuras mais populares do funk carioca atual.

            ---

            ## 📖 Legado

            MC Poze do Rodo representa uma nova geração de artistas que utilizam a
            música como forma de expressão e de contar suas histórias.

            Sua trajetória é vista por muitos fãs como um exemplo de perseverança,
            mostrando como a dedicação ao trabalho e a conexão com suas origens
            podem transformar uma carreira artística.

            Hoje, Poze é considerado um dos nomes mais influentes do funk brasileiro,
            acumulando milhões de admiradores e mantendo forte impacto na cultura
            musical do país.
            """)
    elif artista == "Vários Artistas":

        st.title("🎧 Sets DJ GM")

        st.image("djgm.png")

        st.markdown("""
        ## 🌎 O que são os Sets DJ GM?

        Os Sets DJ GM são projetos musicais produzidos pelo DJ GM,
        um dos produtores mais conhecidos do funk paulista atual.

        Diferente de uma música tradicional com apenas um cantor,
        os sets reúnem diversos MCs em uma única produção,
        criando uma experiência dinâmica e cheia de participações.

        ---

        ## 🎤 Quem é DJ GM?

        DJ GM é um produtor musical brasileiro que ganhou destaque
        pela qualidade de suas produções e pela capacidade de reunir
        artistas de diferentes estilos em um único projeto.

        Seu trabalho ajudou a impulsionar diversos MCs e tornou-se
        uma referência dentro do funk moderno.

        ---

        ## 🚀 Como os Sets ficaram famosos?

        Com batidas marcantes, produção moderna e participações de
        artistas populares, os Sets DJ GM passaram a acumular milhões
        de reproduções nas plataformas digitais.

        O formato chamou atenção porque permitia que vários artistas
        mostrassem seu talento na mesma música.

        ---

        ## 🌟 Impacto na cena do Funk

        Os Sets DJ GM ajudaram a fortalecer a cultura do funk
        brasileiro e serviram como vitrine para novos talentos.

        Atualmente, são considerados alguns dos projetos mais
        populares do gênero.

        ---

        ## 📖 Legado

        DJ GM tornou-se um dos nomes mais importantes da produção
        musical dentro do funk paulista, influenciando novos
        produtores e artistas de todo o Brasil.
        """)
    elif artista == "Japa NK":

        st.title("🎤 Japa NK")

        st.image("japa.png")

        st.markdown("""
        ## 🌎 Quem é Japa NK?

        Japa NK é um cantor e compositor brasileiro que ganhou destaque
        através das plataformas digitais e redes sociais, conquistando
        uma base fiel de fãs com músicas românticas e letras que retratam
        relacionamentos, sentimentos e experiências do cotidiano.

        Seu estilo mistura elementos do trap, funk melódico e música urbana,
        criando uma identidade própria que o tornou um dos nomes mais
        conhecidos entre o público jovem.

        ---

        ## 👶 Início da Vida

        Desde cedo, Japa NK demonstrou interesse pela música e pela arte.
        Inspirado por diferentes gêneros musicais, começou a desenvolver
        suas habilidades de composição ainda na juventude.

        Seu contato com a cultura das ruas e com a música urbana ajudou
        a construir o estilo que mais tarde se tornaria sua marca registrada.

        ---

        ## 🚀 Início da Carreira

        Como muitos artistas da nova geração, Japa NK utilizou a internet
        para divulgar seu trabalho.

        Seus primeiros lançamentos começaram a ganhar visibilidade graças
        ao compartilhamento nas redes sociais e ao apoio de fãs que se
        identificavam com suas letras.

        Aos poucos, seu nome passou a circular entre os artistas mais
        promissores da cena urbana brasileira.

        ---

        ## 🌟 Crescimento e Popularidade

        O crescimento de Japa NK ocorreu principalmente através das
        plataformas de streaming, onde suas músicas alcançaram milhões
        de reproduções.

        Sua capacidade de transformar emoções e experiências pessoais em
        letras acessíveis ajudou a criar uma forte conexão com o público.

        Com o passar do tempo, passou a realizar shows e ampliar sua
        presença no cenário musical nacional.

        ---

        ## 🎭 Características Artísticas

        O trabalho de Japa NK é marcado por:

        - Letras emocionais e românticas.
        - Forte identificação com o público jovem.
        - Mistura de diferentes estilos urbanos.
        - Linguagem moderna e próxima dos fãs.
        - Temas ligados a amor, saudade e relacionamentos.

        Essas características ajudaram a construir uma identidade única
        dentro da música brasileira contemporânea.

        ---

        ## 📱 Presença Digital

        Grande parte do sucesso de Japa NK está relacionada à sua forte
        presença nas redes sociais.

        Seus fãs acompanham lançamentos, bastidores, apresentações e
        momentos importantes de sua trajetória artística, fortalecendo
        ainda mais sua comunidade.

        ---

        ## 🏆 Reconhecimento

        Ao longo de sua carreira, Japa NK conquistou:

        - Milhões de reproduções em plataformas digitais.
        - Crescimento constante nas redes sociais.
        - Participações em projetos musicais de destaque.
        - Reconhecimento entre os artistas da nova geração.

        Seu trabalho continua alcançando novos públicos em todo o Brasil.

        ---

        ## 💡 Curiosidades

        - Seu nome artístico é amplamente conhecido entre os fãs da música urbana.
        - Tornou-se popular principalmente através da internet.
        - Possui forte identificação com o público jovem.
        - Suas músicas frequentemente abordam sentimentos e experiências pessoais.
        - É considerado uma das promessas da nova geração da música brasileira.

        ---

        ## 📖 Legado

        Japa NK representa uma geração de artistas que cresceram junto
        com as plataformas digitais e transformaram a internet em uma
        ferramenta para alcançar milhões de pessoas.

        Sua trajetória demonstra como talento, dedicação e proximidade
        com o público podem abrir espaço para novos artistas dentro do
        cenário musical brasileiro.

        Hoje, continua construindo sua carreira e ampliando sua influência
        entre fãs de todo o país.
        """)
    
