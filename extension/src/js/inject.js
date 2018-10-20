function scrapeArticleText() {
    let articleText = $('.StandardArticleBody_body').first();
    articleText = articleText.find(' > p');
    let articleString = "";
    for(let i = 0; i < articleText.length; i++) {
        articleString += articleText[i].innerText + "\n\n";
    }
    alert(articleString);

}

scrapeArticleText();