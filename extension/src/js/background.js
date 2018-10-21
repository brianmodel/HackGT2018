chrome.browserAction.onClicked.addListener(tab => {
    chrome.tabs.executeScript({
        file: 'src/js/jquery.3.3.1.min.js'
    });
    chrome.tabs.executeScript({
        file: 'src/js/moment.2.22.2.js'
    }, () => {
        chrome.tabs.executeScript({
            file: 'src/js/chart.2.7.3.min.js'
        }, () => {
            chrome.tabs.insertCSS({
                file: 'src/css/inject.css'
            });
            chrome.tabs.executeScript({
                file: 'src/js/inject.js'
            });
        });
    });
    
    
});
