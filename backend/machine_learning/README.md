# Machine Learning
Dataset: https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset

## Analyzing
Antes de iniciar qualquer execução de código, é preciso fazer uma análise das colunas do nosso dataset.  

| Columns | Description |
| --- | --- |
| FILENAME | **Provavelmente** o arquivo contendo o corpo da página HTML |
| URL | URL do website |
| URLLength | Tamanho do URL |
| Domain | Tudo entre o protocol e path (https://**www.google.com**/s=example) |
| DomainLength | Tamanho do domain |
| IsDomainIP | Utiliza o IP em vez de um nome regitrado no [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) |
| TLD | [TLD](https://en.wikipedia.org/wiki/Top-level_domain) é a última parte do domain (www.google<b>.com</b>) |
| URLSimilarityIndex | O quão esse URL é similar com outros URLs conhecidos (e válidos) |
| CharContinuationRate | Frequência que characters continuão até um espaço aparecer |
| TLDLegitimateProb | Probabilidade de ser um TLD autorizado |
| URLCharProb | Probabilidade da sequência de characters na URL serem de um site legítimo  |
| TLDLength | Tamanho do TLD |
| NoOfSubDomain | Número de [subdomains](https://en.wikipedia.org/wiki/Subdomain), (uma vez que você chega em um site como `steampowered.com`, ele pode te redirecionar para um subdomain dele como `store.steampowered.com`) |
| HasObfuscation | `1` == URL possui ofuscações, `0` == URL não possui,  |
| NoOfObfuscatedChar | Quantidade de characters utilizados para ofuscações no URL (`%20`, `%3A`, ...) |
| ObfuscationRatio | Porcentagem de ofuscações no URL |
| NoOfLettersInURL | Quantidade de letras no URL |
| LetterRatioInURL | Porcentagem de letras no URL |
| NoOfDegitsInURL | Quantidade de dígitos no URL |
| DegitRatioInURL | Porcentagem de dígitos no URL |
| NoOfEqualsInURL | Quantidade de `=` no URL |
| NoOfQMarkInURL | Quantidade de `?` no URL |
| NoOfAmpersandInURL | Quantidade de `&` no URL |
| NoOfOtherSpecialCharsInURL | Quantidade de outros characters (não  "") |
| SpacialCharRatioInURL | Porcentagem de characters especiais |
| IsHTTPS | `1` == usa HTTPS, `0` == não usa,  |
| LineOfCode | Quantidade de linhas no conteúdo da página |
| LargestLineLength | Tamanho da maior linha encontrada no conteúdo da página |
| HasTitle | `1` == possui título, `0` == não possui  |
| Title | Título da página |
| DomainTitleMatchScore | Quão o título bate com o domain |
| URLTitleMatchScore | Quão o título bate com o URL |
| HasFavicon | Possui ícone de favoritos |
| Robots | `1` == possui arquivo robots.txt, `0` == não possui |
| IsResponsive | `1` == possui `<meta>` para ajudar responsividade, `0` == não possui |
| NoOfURLRedirect | Quantidade de redirects ocorridos até receber a página HTML |
| NoOfSelfRedirect | Quantidade de redirects dentro do mesmo domain até receber a página HTML |
| HasDescription | `1` == possui `<meta>` com descrição, `0` == não possui |
| NoOfPopup | Quantidade de popups (código Javascript como: `alert()`, `confirm()`, `prompt()`, `window.open()`) |
| NoOfiFrame | Quantidade de `<iframe>` |
| HasExternalFormSubmit | `0` == possui `<form>` com atributo `action` direcionando para site externo, `0` == não possui |
| HasSocialNet | `1` == possui link para qualquer social media, `0` == não possui |
| HasSubmitButton | `1` == possui `<submit>` ou `<input type="submit">`, `0` == não possui |
| HasHiddenFields | `1` == possui `<input type="hidden">`, `0` == não possui |
| HasPasswordField | `1` == possui `<input type="password">`, `0` == não possui |
| Bank | Quantidade de menções a termos utilizados para bancos |
| Pay | Quantidade de menções a termos utilizados para pagamentos |
| Crypto | Quantidade de menções a termos utilizados para cryptomoeda |
| HasCopyrightInfo | `1` == Possue copyright em algum lugar da página (`© 2024 Microsoft Corporation. All rights reserved.`), `0` == não possui |
| NoOfImage | Quantidade de imagens na página |
| NoOfCSS | Quantidade de arquivos CSS linkados na página |
| NoOfJS | Quantidade de arquivos JS linkados na página |
| NoOfSelfRef | Quantidade de links apontando para a própria página (`<a href="/about">`, `<a href="https://example.com/login">`) |
| NoOfEmptyRef | Quantidade de links apontando para nada (`<a href="#">`, `<a href="">`, `<a href>`, `<a href="javascript:void(0)">`) |
| NoOfExternalRef | Quantidade de links apontando para sites externos |
| label | `1` == website legítimo, `0` == phishing  |

### Categories

Podemos separar os dados coletados em 3 categorias:
- Dados extraidos do URL
    - URLLength, DomainLength, ...
- Dados extraidos do conteúdo da página
    - LineOfCode, HasTitle, ...
- Dados extraidos do comportamento da conexão
    - NoOfURLRedirect, NoOfSelfRedirect, ...
- Outros
    - Robots

## Preprocessing
Colunas com valores do tipo strings precisam ser removidas, isso é necessário já que os algoritmos apenas trabalham com número. Colunas a serem removidas:  

- FILENAME
- URL
- Domain
- TLD
- Title

Qualquer informação que seja considerada útil para o algoritmo deve ser extraida **antes** desta etapa e transformada em uma nova coluna. Por exemplo, o autor do dataset criou a coluna `IsHTTPS` pois considerou uma informação importante de se ter sobre o URL.  

As seguintes colunas foram removidas pois não foi possível deduzir a formula para seu valores:
- URLSimilarityIndex
- CharContinuationRate
- TLDLegitimateProb
- URLCharProb

### Categories
Seria bom fornecer funcionamento mesmo quando o usuário só tivesse parte das informações.  

Se o usuário apenas possuir a **URL**, **conteúdo da página** e **HAR file**, precisaremos ter um modelo que trabalhe bem sem as seguintes colunas:  

- Robots

Se o usuário apenas possuir a **URL** e **conteúdo da página**, precisaremos ter um modelo que trabalhe bem sem as seguintes colunas:  

- NoOfURLRedirect
- NoOfSelfRedirect

Se o usuário apenas possuir a **URL**, precisaremos ter um modelo que trabalhe bem sem as seguintes colunas:  

- LineOfCode
- LargestLineLength
- HasTitle
- DomainTitleMatchScore
- URLTitleMatchScore
- HasFavicon
- IsResponsive
- HasDescription
- NoOfPopup
- NoOfiFrame
- HasExternalFormSubmit
- HasSocialNet
- HasSubmitButton
- HasHiddenFields
- HasPasswordField
- Bank
- Pay
- Crypto
- HasCopyrightInfo
- NoOfImage
- NoOfCSS
- NoOfJS
- NoOfSelfRef
- NoOfEmptyRef
- NoOfExternalRef

## Confunsion
Para conseguir transformar uma URL em dados pro modelo, é importante entender como cada feature é calculada. Porém foram descobertas diversas complicações no dataset:

1. Quando a URL utiliza um IP address, o dataset bota o TLD como o último valor.
    - `http://198.98.58.123/` => 123
    - `http://43.128.92.128/` => 128
2. Quando a URL utiliza um IP address, o dataset conta tudo antes do penúltimo valor como subdomain.
    - `http://198.98.58.123/` => 2
    - `http://43.128.92.128/` => 2
    - `http://188.128.202.35.bc.googleusercontent.com/` => 5
3. Não foi possível descobrir a função por traz da feature `NoOfOtherSpecialCharsInURL`:
    - `https://www.dzwww.com` => 0
    - `https://www.southbankmosaics.com` => 1
    - `https://www.voicefmradio.co.uk` => 2
    - `https://maildinshaakckjnw411.web.app/` => 3
4. O campo `URLLength` parece ter um a menos do real tamanho:
    - `https://www.southbankmosaics.com` => 31 (esperava 32)
    - `https://www.uni-mainz.de` => 23 (esperava 24)
    - `https://mail-service-100960.weeblysite.com/` => 42 (esperava 43)
5. Não foi possível descobrir a função por traz da feature `LetterRatioInURL`:
    - `https://www.southbankmosaics.com` => 0.581 (esperava 0.843750)
    - `https://www.uni-mainz.de` => 0.391 (esperava 0.750000)
    - `https://www.voicefmradio.co.uk` => 0.517 (esperava 0.800000)
6. O campo `IsDomainIP` pode estar incorreto:
    - `64.47.167.72.host.secureserver.net` => 1 (esperava 0)
    - `244.33.109.208.host.secureserver.net` => 1 (esperava 0)
6. O campo `TLDLength` pode estar incorreto:
    - `https://www-realizesolucoesfinanceiras-com-br-7.rds.land:443/realizesolucoesfinanceiras` => 8 (esperava 4)
    - `https://carousell-paynow.firebaseapp.com:443/minesd/index.html` => 7 (esperava 3)