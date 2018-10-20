chrome.browserAction.onClicked.addListener(tab => {
    chrome.tabs.executeScript({
        file: 'src/js/jquery.3.3.1.min.js'
    }, () => {
        chrome.tabs.executeScript({
            file: 'src/js/inject.js'
        });
    });
});
