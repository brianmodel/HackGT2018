let $articleText;

let divElements = {
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
        let $term = $(document.createElement('span'));
        $term.addClass('termSideBar');
        $term.text(term);
        let $tagNumber = $(document.createElement('span'));
        $tagNumber.addClass('tagNumberSideBar');
        $tagNumber.text("|" + number + "|");
        $entry.append($term, ":&nbsp;", $tagNumber, "&nbsp;", definition);
        return $entry;
    }
}

function createSideBar() {
    let $container = divElements.createPageContainer();
    $container.html($(document.body).html());
    $(document.body).html("");
    $(document.body).append($container);
    $('.TwoColumnLayout_left').css('width', '100%');
    let $sideBar = divElements.createSideBar();

    $(document.body).append($sideBar);
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

function getOnPageParagraphs() {
    $(window).scroll(() => {
        for (let i = 0; i < $articleText.length; i++) {
            let $currentP = $($articleText[i]);
            let verticalPosition = $currentP.offset().top + ($currentP.height() / 2) - $(window).scrollTop();
            if(verticalPosition >= 0 && verticalPosition <= $(window).height()) {
                // $currentP.css('background', 'yellow');
            } else {
                // $currentP.css('background', 'none');
            }
        }
    });
}






async function run() {
    createSideBar();
    await scrapeArticleParagraphs();
    getOnPageParagraphs();
}

run();