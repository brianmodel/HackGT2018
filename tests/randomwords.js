let randomDefinitions = ["the total demand for goods and services within a particular market", "short for gross domestic product", "a type of security that signifies ownership in a corporation"];

let $paragraph = $($articleText[paragraphNumber]);
let paragraphText = $paragraph.text();
let wordsInParagraph = paragraphText.split(' ');
let word0 = Math.floor(Math.random() * wordsInParagraph.length);
let word1 = Math.floor(Math.random() * wordsInParagraph.length);
while(word0 == word1) {
    word1 = Math.floor(Math.random() * wordsInParagraph.length);
}
definitionsList[paragraphNumberString] = [];
definitionsList[paragraphNumberString].push({
    term: wordsInParagraph[word0],
    number: keywordCount++,
    definition: randomDefinitions[Math.floor(Math.random() * randomDefinitions.length)]
});
definitionsList[paragraphNumberString].push({
    term: wordsInParagraph[word1],
    number: keywordCount++,
    definition: randomDefinitions[Math.floor(Math.random() * randomDefinitions.length)]
});
definitionsList[paragraphNumberString].isActive = false;
extractAndDisplayKeywords(paragraphNumber);