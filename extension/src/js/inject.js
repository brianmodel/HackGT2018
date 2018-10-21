let $articleText;
let definitionsList = {};
let keywordCount = 0;

let endpoints = {
    main: 'http://localhost:5000',
    summary: '/summary',
    keywords: '/keywords'
}
let sideBarTools = {
    createPageContainer: function () {
        let $container = $(document.createElement('div'));
        $container.attr('id', 'leftBar');
        return $container;
    },
    createSideBar: function () {
        let $sideBar = $(document.createElement('div'));
        $sideBar.attr('id', 'deconifySideBar');
        let $mutableContainer = this.createMutableContainer();
        let $tabsDiv = this.createTabsDiv();
        $sideBar.append($mutableContainer, $tabsDiv);
        return $sideBar;
    },
    createMutableContainer: function() {
        let $mutableContainer = $(document.createElement('div'));
        $mutableContainer.attr('id', 'mutableContainerSideBar');
        let $definitionsDiv = this.createDefinitionsDiv();
        let $extrasDiv = this.createExtrasDiv();
        let $summaryDiv = this.createSummaryDiv();
        let $exploreDiv = this.createExploreDiv();

        $mutableContainer.append($definitionsDiv, $extrasDiv, $summaryDiv, $exploreDiv);
        return $mutableContainer;
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
    createSummaryDiv: function() {
        let $summaryDiv = $(document.createElement('div'));
        $summaryDiv.addClass('sideBarSection');
        $summaryDiv.attr('id', 'summarySideBar');
        $summaryDiv.append($('<center><h3 class="titleSideBar">Summary</h3></center>'));

        return $summaryDiv;
    },
    createExploreDiv: function() {
        let $exploreDiv = $(document.createElement('div'));
        $exploreDiv.addClass('sideBarSection');
        $exploreDiv.attr('id', 'exploreSideBar');
        $exploreDiv.append($('<center><h3 class="titleSideBar">Explore</h3></center>'));

        return $exploreDiv;
    },
    createTabsDiv: function () {
        let $tabsDiv = $(document.createElement('div'));
        $tabsDiv.addClass('sideBarSection');
        $tabsDiv.attr('id', 'tabsSideBar');

        let $mainTab = $(document.createElement('span'));
        let $summaryTab = $(document.createElement('span'));
        let $exploreTab = $(document.createElement('span'));
        $mainTab.addClass('tabSideBar chosenTabSideBar');
        $summaryTab.addClass('tabSideBar');
        $exploreTab.addClass('tabSideBar');
        $mainTab.attr('id', 'mainTabSideBar');
        $summaryTab.attr('id', 'summaryTabSideBar');
        $exploreTab.attr('id', 'exploreTabSideBar');
        $mainTab.text("Main");
        $summaryTab.text("Summary");
        $exploreTab.text("Explore");

        $mainTab.click(showMainTab);
        $summaryTab.click(showSummaryTab);
        $exploreTab.click(showExploreTab);

        
        $tabsDiv.append($mainTab, $summaryTab, $exploreTab);

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

function showMainTab() {
    $('#summarySideBar').hide();
    $('#exploreSideBar').hide();
    $('#definitionsSideBar').show();
    $('#extrasSideBar').show();

    $('#mainTabSideBar').addClass('chosenTabSideBar');
    $('#summaryTabSideBar').removeClass('chosenTabSideBar');
    $('#exploreTabSideBar').removeClass('chosenTabSideBar');
}
function showSummaryTab() {
    $('#exploreSideBar').hide();
    $('#definitionsSideBar').hide();
    $('#extrasSideBar').hide();
    $('#summarySideBar').show();

    $('#mainTabSideBar').removeClass('chosenTabSideBar');
    $('#summaryTabSideBar').addClass('chosenTabSideBar');
    $('#exploreTabSideBar').removeClass('chosenTabSideBar');
}
function showExploreTab() {
    $('#definitionsSideBar').hide();
    $('#extrasSideBar').hide();
    $('#summarySideBar').hide();
    $('#exploreSideBar').show();

    $('#mainTabSideBar').removeClass('chosenTabSideBar');
    $('#summaryTabSideBar').removeClass('chosenTabSideBar');
    $('#exploreTabSideBar').addClass('chosenTabSideBar');
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
    $.post(endpoints.main + endpoints.summary, {
        article: articleString
    }, (summary, status) => {
        let $summary = document.createElement('p');
        $summary.id = 'summaryTextSideBar';
        $summary.innerText = summary;
        $('#summarySideBar').append($summary);
    });

}

async function getOnPageParagraphs() {
    $(window).scroll(() => {
        for (let i = 0; i < $articleText.length; i++) {
            let $paragraph = $($articleText[i]);
            let verticalPosition = $paragraph.offset().top + ($paragraph.height() / 2) - $(window).scrollTop();
            if(verticalPosition >= 0 && verticalPosition <= $(window).height()) {
                // $paragraph.css('background', 'yellow');
                extractAndDisplayKeywords(i);
            } else {
                // $paragraph.css('background', 'none');
                removeKeywordsFromSidebar(i);
            }
        }
    });
}
async function extractAndDisplayKeywords(paragraphNumber) {
    let paragraphNumberString = paragraphNumber.toString();
    console.log("PARAGRAPH NUMBER: " + paragraphNumberString);
    if(paragraphNumberString in definitionsList) {
        for(let i = 0; i < definitionsList[paragraphNumberString].length; i++) {
            let entry = definitionsList[paragraphNumberString][i];
            if(!entry.isDisplayed) {
                $('#definitionsSideBar').append(sideBarTools.createDefinitionEntry(entry.term, entry.number, entry.definition));
                entry.isDisplayed = true;
            }
            
        }
    } else if (!(paragraphNumberString in definitionsList)) {
        console.log("CALLING!! for paragraph " + paragraphNumberString);
        console.log(definitionsList);
        definitionsList[paragraphNumberString] = [];
        let $paragraph = $($articleText[paragraphNumber]);
        let paragraphText = $paragraph.text();
        $.post(endpoints.main + endpoints.keywords, {
            paragraph: paragraphText
        }, (keywords, status) => {
            console.log(keywords);
            for(let i = 0; i < keywords.length; i++) {
                let keyword = keywords[i];
                if(keyword.type === "definition") {
                    console.log("KEYWORD: " + keyword.word);
                    definitionsList[paragraphNumberString].push({
                        term: keyword.word,
                        number: keywordCount++,
                        definition: keyword.definition,
                        isDisplayed: false
                    });
                }
            }
            extractAndDisplayKeywords(paragraphNumber);
        });
    }
    return true;
}
function removeKeywordsFromSidebar(paragraphNumber) {
    let paragraphNumberString = paragraphNumber.toString();
    if (paragraphNumberString in definitionsList) {
        for (let i = 0; i < definitionsList[paragraphNumberString].length; i++) {
            let entry = definitionsList[paragraphNumberString][i];
            sideBarTools.removeDefinitionEntry(entry.number);
            entry.isDisplayed = false;
        }
    }
}






async function run() {
    createSideBar();
    await scrapeArticleParagraphs();
    getOnPageParagraphs();
    getSummary();
}

run();