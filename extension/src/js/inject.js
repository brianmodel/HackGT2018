let $articleText;
let definitionsList = {};
let keywordCount = 0;

let randomDefinitions = ["the total demand for goods and services within a particular market", "short for gross domestic product", "a type of security that signifies ownership in a corporation"];
let sideBarTools = {
    createPageContainer: function () {
        let $container = $(document.createElement('div'));
        $container.attr('id', 'leftBar');
        return $container;
    },
    createSideBar: function () {
        let $sideBar = $(document.createElement('div'));
        $sideBar.attr('id', 'deconifySideBar');
        let $definitionsDiv = this.createDefinitionsDiv();
        let $extrasDiv = this.createExtrasDiv();
        let $tabsDiv = this.createTabsDiv();
        $sideBar.append($definitionsDiv, $extrasDiv, $tabsDiv);
        return $sideBar;
    },
    createDefinitionsDiv: function () {
        let $definitionsDiv = $(document.createElement('div'));
        $definitionsDiv.attr('id', 'definitionsSideBar');
        $definitionsDiv.addClass('sideBarSection');
        $definitionsDiv.append($('<center><h3 class="titleSideBar">Definitions</h3></center>'));
        return $definitionsDiv;
    },
    createExtrasDiv: function () {
        let $extrasDiv = $(document.createElement('div'));
        $extrasDiv.attr('id', 'extrasSideBar');
        $extrasDiv.addClass('sideBarSection');
        $extrasDiv.append($('<center><h3 class="titleSideBar">Extras</h3></center>'));
        return $extrasDiv;
    },
    createTabsDiv: function () {
        let $tabsDiv = $(document.createElement('div'));
        $tabsDiv.attr('id', 'tabsSideBar');
        $tabsDiv.addClass('sideBarSection');
        return $tabsDiv;
    },
    createDefinitionEntry: function (term, number, definition) {
        let $entry = $(document.createElement('p'));
        $entry.addClass('definitionEntrySideBar');
        $entry.attr("entryNumber", number);
        let $term = $(document.createElement('span'));
        $term.addClass('termSideBar');
        $term.text(term);
        let $tagNumber = $(document.createElement('span'));
        $tagNumber.addClass('tagNumberSideBar');
        $tagNumber.text("|" + number + "|");
        $entry.append($term, ":&nbsp;", $tagNumber, "&nbsp;", definition);
        return $entry;
    },
    removeDefinitionEntry: function(number) {
        $('p[entryNumber="' + number + '"]').remove();
    }
}

function createSideBar() {
    let $container = sideBarTools.createPageContainer();
    $container.html($(document.body).html());
    $(document.body).html("");
    $(document.body).append($container);
    $('.TwoColumnLayout_left').css('width', '100%');
    let $sideBar = sideBarTools.createSideBar();
    $(document.body).append($sideBar);
    // $('#definitionsSideBar').append(sideBarTools.createDefinitionEntry("Aggregate demand", 1, "the total demand for goods and services within a particular market"), sideBarTools.createDefinitionEntry("GDP", 2, "short for gross domestic product"), sideBarTools.createDefinitionEntry("Stock", 3, "a type of security that signifies ownership in a corporation"));
    console.log("Added!")
}

async function scrapeArticleParagraphs() {
    $articleText = $('.StandardArticleBody_body').first();
    $articleText = $articleText.find(' > p');
    return $articleText;
}
function getSummary() {
    let articleString = "";
    for(let i = 0; i < $articleText.length; i++) {
        articleString += $articleText[i].innerText + "\n\n";
    }
    alert(articleString);
    console.log(articleString);

}

async function getOnPageParagraphs() {
    $(window).scroll(() => {
        for (let i = 0; i < $articleText.length; i++) {
            let $paragraph = $($articleText[i]);
            let verticalPosition = $paragraph.offset().top + ($paragraph.height() / 2) - $(window).scrollTop();
            if(verticalPosition >= 0 && verticalPosition <= $(window).height()) {
                // $currentP.css('background', 'yellow');
                extractAndDisplayKeywords(i);
            } else {
                // $currentP.css('background', 'none');
                removeKeywordsFromSidebar(i);
            }
        }
    });
}
async function extractAndDisplayKeywords(paragraphNumber) {
    let paragraphNumberString = paragraphNumber.toString();
    if(paragraphNumberString in definitionsList && !definitionsList[paragraphNumberString].isActive) {
        for(let i = 0; i < definitionsList[paragraphNumberString].length; i++) {
            let entry = definitionsList[paragraphNumberString][i];
            $('#definitionsSideBar').append(sideBarTools.createDefinitionEntry(entry.term, entry.number, entry.definition));
        }
        definitionsList[paragraphNumberString].isActive = true;
    } else if (!(paragraphNumberString in definitionsList)) {
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
    }
    return true;
}
function removeKeywordsFromSidebar(paragraphNumber) {
    let paragraphNumberString = paragraphNumber.toString();
    if (paragraphNumberString in definitionsList && definitionsList[paragraphNumberString].isActive) {
        for (let i = 0; i < definitionsList[paragraphNumberString].length; i++) {
            let entry = definitionsList[paragraphNumberString][i];
            sideBarTools.removeDefinitionEntry(entry.number);
        }
        definitionsList[paragraphNumberString].isActive = false;
    }
}






async function run() {
    createSideBar();
    await scrapeArticleParagraphs();
    getOnPageParagraphs();
}

run();