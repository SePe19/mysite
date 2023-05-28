function parseTwitterNumber(number) {
    if (number >= 1000000) {
        return (number / 1000000).toFixed(1) + "M";
    } else if (number >= 1000) {
        return (number / 1000).toFixed(1) + "K";
    } else {
        return number.toString();
    }
}

// Tweet Number
function tweet_number() {
    console.log("hej 10hi fnis")
    const elements = document.querySelectorAll(".tweet-number")
    elements.forEach(function(element) {
        const tweetNumber = element.textContent
        element.textContent = parseTwitterNumber(tweetNumber)
    })
}

tweet_number()