$.get('http://localhost:5000/keywords', {
    paragraph: "water"
}, (keywords, status) => {
    console.log(keywords);
    console.log(status);
});

$.get('http://localhost:5000/keywords', {
    paragraph: "After worries about higher interest rates sparked a steep sell-off in early October and again on Thursday, the S&P 500 remains down 5 percent from its Sept. 20 record high close, with top-shelf stocks including Amazon.com Inc (AMZN.O), Alphabet Inc (GOOGL.O), Netflix Inc (NFLX.O) and Facebook Inc (FB.O) showing little of their vitality from recent years."
}, (keywords, status) => {
    console.log(keywords);
    console.log(status);
});