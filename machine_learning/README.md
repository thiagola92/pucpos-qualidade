# Machine Learning
Dataset: https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset

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
| URLCharProb | |
| TLDLength | Tamanho do TLD |
| NoOfSubDomain | Número de [subdomains](https://en.wikipedia.org/wiki/Subdomain), (uma vez que você chega em um site como `steampowered.com`, ele pode te redirecionar para um subdomain dele como `store.steampowered.com`) |
| HasObfuscation | `1` == URL possui ofuscações, `0` == URL não possui,  |
| NoOfObfuscatedChar | Quantidade de ofuscações no URL (`%20`, `%3A`, ...) |
| ObfuscationRatio | Porcentagem de ofuscações no URL |
| NoOfLettersInURL | Quantidade de letras no URL |
| LetterRatioInURL | Porcentagem de letras no URL |
| NoOfDegitsInURL | Quantidade de dígitos no URL |
| DegitRatioInURL | Porcentagem de dígitos no URL |
| NoOfEqualsInURL | Quantidade de `=` no URL |
| NoOfQMarkInURL | Quantidade de `?` no URL |
| NoOfAmpersandInURL | Quantidade de `&` no URL |
| NoOfOtherSpecialCharsInURL | Quantidade de outros characters especiais (`#  %  -  _  @  !  ,  .  ~  :`) |
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

## Clean up
Colunas com valores do tipo strings precisam ser removidas, isso é necessário já que os algoritmos apenas trabalham com número. Colunas a serem removidas:  

- FILENAME
- URL
- Domain
- TLD
- Title

Qualquer informação que seja considerada útil para o algoritmo deve ser extraida **antes** disto. Por exemplo, o autor do dataset criou a coluna `IsHTTPS` pois considerou uma informação importante de se ter sobre o URL.  

