# Machine Learning
Dataset: https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset

| Columns | Description |
| --- | --- |
| FILENAME | Identificador para a linha |
| URL | URL do website |
| URLLength | Tamanho do URL |
| Domain | Tudo entre o protocol e path (https://**www.google.com**/s=example) |
| DomainLength | Tamanho do domain |
| IsDomainIP | Utiliza o IP em vez de um nome regitrado no [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) |
| TLD | [TLD](https://en.wikipedia.org/wiki/Top-level_domain) é a última parte do domain (www.google<b>.com</b>) |
| URLSimilarityIndex | "A metric that indicates how similar a URL is to other well-known, valid URLs" |
| CharContinuationRate | "The rate at which characters continue without a space is known as the CharContinuationRate" |
| TLDLegitimateProb | "The likelihood that the TLD is authorised" |
| URLCharProb | |
| TLDLength | Tamanho do TLD |
| NoOfSubDomain | Número de [subdomains](https://en.wikipedia.org/wiki/Subdomain), (uma vez que você chega em um site como `steampowered.com`, ele pode te redirecionar para um subdomain dele como `store.steampowered.com`) |
| HasObfuscation | "0 means the URL is not obfuscated, while 1 means it is" |
| NoOfObfuscatedChar | "denotes whether HTTPS is used by the URL (0 for no, 1 for yes)" |
| ObfuscationRatio | |
| NoOfLettersInURL | |
| LetterRatioInURL | |
| NoOfDegitsInURL | |
| DegitRatioInURL | |
| NoOfEqualsInURL | |
| NoOfQMarkInURL | |
| NoOfAmpersandInURL | |
| NoOfOtherSpecialCharsInURL | |
| SpacialCharRatioInURL | |
| IsHTTPS | |
| LineOfCode | |
| LargestLineLength | |
| HasTitle | |
| Title | |
| DomainTitleMatchScore | |
| URLTitleMatchScore | |
| HasFavicon | |
| Robots | |
| IsResponsive | |
| NoOfURLRedirect | |
| NoOfSelfRedirect | |
| HasDescription | |
| NoOfPopup | |
| NoOfiFrame | |
| HasExternalFormSubmit | |
| HasSocialNet | |
| HasSubmitButton | |
| HasHiddenFields | |
| HasPasswordField | |
| Bank | |
| Pay | |
| Crypto | |
| HasCopyrightInfo | |
| NoOfImage | "The quantity of pictures on the page" |
| NoOfCSS | "The amount of CSS files that the website has links to" |
| NoOfJS | "The amount of JavaScript files that are connected on the page" |
| NoOfSelfRef | |
| NoOfEmptyRef | |
| NoOfExternalRef | |
| label | `0` == phishing, `1` == website legítimo |