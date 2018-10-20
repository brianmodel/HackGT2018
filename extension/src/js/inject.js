function scrapeArticleText() {
    let $articleText = $('.StandardArticleBody_body').first();
    $articleText = $articleText.find(' > p');
    let articleString = "";
    for(let i = 0; i < $articleText.length; i++) {
        articleString += $articleText[i].innerText + "\n\n";
    }
    alert(articleString);
    console.log(articleString);

}

function createSideBar() {
    
    let $container = $(document.createElement('div'));
    $container.html($(document.body).html());
    $container.css('width', '65vw');
    $container.css('padding', '10px');
    $(document.body).html("");
    $(document.body).append($container);
    $('.TwoColumnLayout_left').css('width', '100%');
    let $sideBar = $(document.createElement('div'));
    $sideBar.attr('id', 'deconifySideBar');
    $sideBar.text("Brian Model, the legend. Brian Model, the legend. Brian Model, the legend. Brian Model, the legend. Brian Model, the legend.");
    $sideBar.css('right', '0');
    $sideBar.css('top', '0');
    $sideBar.css('display', 'block');
    $sideBar.css('width', '35vw');
    $sideBar.css('height', '100vh');
    $sideBar.css('background', 'cyan');
    $sideBar.css('position', 'fixed');
    $(document.body).append($sideBar);
    console.log("Added!")
}

createSideBar();