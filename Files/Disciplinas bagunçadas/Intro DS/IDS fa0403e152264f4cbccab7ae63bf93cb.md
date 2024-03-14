# IDS

- Aula 1 - 09/01/23
    - Introdução
        
        Avaliação toda semana
        
        4h por dia teoricamente
        
        descobrir sobre como usar a linguagem de programação que daniel usou pra fazer slide
        
        - Objetivos
            
            ter uma trilha clara
            
            Base sólida
            
        - Métodos de avaliação
            - Lista de exercícios no final de toda aula
                
                Bem exigente no horário de entrega
                
                até quarta feira 15h para resolver os exercícios.
                
                Sempre 1h antes da entrega vai tirar dúvidas
                
            - Sexta feira: Aula de revisão em que nós iremos explicar a resolução dos exercícios na forma de sorteio.
            - Projeto de dados: qual conjunto de dados pretende investigar. E analisar eles de alguma forma.
        - Critério avaliativo
            
            Não importa estar certo ou errado, mas sim ter tentado de verdade. Uma resposta honesta.
            
        - Aulas: Seg, Qua, Sex - 14 ~ 16
        - Seguir o livro R for Data Science
        - Slides
            - Tidy
                
                ![Untitled](IDS%20fa0403e152264f4cbccab7ae63bf93cb/Untitled.png)
                
            - Undestand
                - Transform
                    
                    ![Untitled](IDS%20fa0403e152264f4cbccab7ae63bf93cb/Untitled%201.png)
                    
                - Visualize
                    
                    ![Untitled](IDS%20fa0403e152264f4cbccab7ae63bf93cb/Untitled%202.png)
                    
                - Model
                    
                    ![Untitled](IDS%20fa0403e152264f4cbccab7ae63bf93cb/Untitled%203.png)
                    
            - Communicate
                
                ![Untitled](IDS%20fa0403e152264f4cbccab7ae63bf93cb/Untitled%204.png)
                
    - [Capítulo 2](https://r4ds.hadley.nz/data-visualize.html)
        
        
        ```r
        library("tidyverse")
        install.packages("palmerpenguins")
        library("palmerpenguins")
        penguins
        glimpse(penguins)
        view(penguins)
        ggplot(data=penguins)
        
        ggplot(
        	data = penguins,
        	mapping = aes (x = flipper_length_mm,  y = body_mass_g)
        )
        
        ggplot(
        	data = penguins,
        	mapping = aes (x = flipper_length_mm,  y = body_mass_g)
        ) + 
        geom_point()
        
        ggplot(
        	data = penguins,
        	mapping = aes (x = flipper_length_mm,  y = body_mass_g, color = species)
        ) + 
        geom_point()
        
        ggplot(
        	data = penguins,
        	mapping = aes (x = flipper_length_mm,  y = body_mass_g, color = island)
        ) + 
        geom_point()
        
        ggplot(
        	data = penguins,
        	mapping = aes (x = flipper_length_mm,  y = body_mass_g, color = sex)
        ) + 
        geom_point()
        ```
        
    - Dúvidas:
        - O que seria “modelar os dados”?
            
            Não veremos sobre, mas usa machine learning
            
        - Por que precisa do +?
            
            Ele funciona como um pipe para juntar funções juntas
            
        - Como sabemos se X gera Y ou Y causa X?
        - Como posso usar o R num notebook ou sem ser console?
            
            Pesquisar depois como fazer isso
            
    - Anotações
        
        Não mexeremos com modelagem. Primeiro precisamos de uma boa base na análise.
        
        Regra de Paretto: A ideia é ter a base para resolver 80% dos projetos
        
        primeiro visualização e transformação de dados tided
        
        depois importação e arrumação
        
        Comunicação talvez
        
        Capítulo 2 - Visualização de dados (usar ggplot2)
        
        Capítulo 4 - Transformação de dados
        
        Capítulo 6 - Tidy
        
        Capítulo 8 - Importação
        
        pesquisar o que é “tibble”
        
    - Comentários:
        
        poderia já ter os links:
        
        R
        
        RStudio
        
        Livro
        
        ![Untitled](IDS%20fa0403e152264f4cbccab7ae63bf93cb/Untitled%205.png)
        
        ![Untitled](IDS%20fa0403e152264f4cbccab7ae63bf93cb/Untitled%206.png)
        
        ![Untitled](IDS%20fa0403e152264f4cbccab7ae63bf93cb/Untitled%207.png)
        
        Me disponibilizar para ajudar ele a conferir erros.
        
        Daniel tomando uma nova aula na testa kkkkkkkkkkkkkkk
        
        Já deveria ter os pesos para o cálculo das notas
        
        install.packages("palmerpenguins")
        
        Já deveria ter os comandos no ctrl c ctrl v
        
        ou então os slides no git
        
        ![Untitled](IDS%20fa0403e152264f4cbccab7ae63bf93cb/Untitled%208.png)
        
        - Como sabemos se X gera Y ou Y causa X?
            
            Daniel vai me mandar um livro dps
            
        
        Tá bem linearzinho, tô gostando
        

[Atividade 1 - Lista de exercícios 1](IDS%20fa0403e152264f4cbccab7ae63bf93cb/Atividade%201%20-%20Lista%20de%20exerci%CC%81cios%201%205f7f789672cd42e6aa01faebf45ab1eb.md)

- Aula 2 - 11/01/23
    
    Eu estava indo pra Vila Velha
    
    - Anotações
        
        species
        island
        bill_length_mm
        bill_depth_mm
        flipper_length_mm
        body_mass_g
        sex
        year
        

[Atividade 2 - Lista de exercícios 2](IDS%20fa0403e152264f4cbccab7ae63bf93cb/Atividade%202%20-%20Lista%20de%20exerci%CC%81cios%202%20f96dd225301949e097863f7007206b9e.md)

- Aula 3 - 13/01/23
    
    Resposta das listas de exercícios
    
    SE = Standard Error
    
- Aula 4 - 16/01/23
- Aula 5 - 18/01/23
    
    Não ocorreu
    

[IA 2 - **Exercícios 2ª semana: L3 - Transformação de dados**](https://www.notion.so/IA-2-Exerc-cios-2-semana-L3-Transforma-o-de-dados-f0e806742c714cc79c1c57c908b2bdab?pvs=21) 

- Aula 6 - 20/01/23
    
    apresentação da LE 3
    
- Aula 7 - 23/01/23
    
    ```r
    table1 |>
      count(year, wt = cases)
    ```
    
    Eu tava andando de carro na primeira metade da aula
    

[**Exercícios 3ª semana: L4 - Tidying data**](https://www.notion.so/Exerc-cios-3-semana-L4-Tidying-data-aed32fce4b4649fdb394f84a5a3ba27d?pvs=21) 

- Aula 8 - 30/01/23 - Data import
    
    CSV: é um tipo específico de string que organiza dados
    
    ![Untitled](IDS%20fa0403e152264f4cbccab7ae63bf93cb/Untitled%209.png)
    
    o tipo “factor” resume uma coluna de dados repetidos. Meio que criar um índice pra cada resposta possível.
    
    ```r
    read_csv(
      "The first line of metadata
      The second line of metadata
      x,y,z
      1,2,3",
      skip = 2
    )
    ```
    
    existe uma função chamada `problems()`
    

[**Exercícios 4ª semana: L5 - Data Import**](https://www.notion.so/Exerc-cios-4-semana-L5-Data-Import-59edcdbe4d6b408c996ad0b2816acf2e?pvs=21) - 31/01/2023

- Aula 9 - 03/02/23
    
    Dados no Github
    
    Base dos dados
    
    [https://dados.gov.br/home](https://dados.gov.br/home)
    

[IDS - **Definição do Trabalho Final**](https://www.notion.so/IDS-Defini-o-do-Trabalho-Final-cde2da2c01a841d7ae5b9e1498af178d?pvs=21)

[IDS - Trabalho final](https://www.notion.so/IDS-Trabalho-final-9a818f68d56e4ae8b8609d3edf13e710?pvs=21)